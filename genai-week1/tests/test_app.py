
import pytest
from pydantic import ValidationError
import logging

from genai_week1.app import (
    DemoModelClient,
    IncidentSummary,
    ModelClientError,
    SummaryOutputError,
    extract_summary,
)


VALID_JSON = """
{
  "title": "Orders pipeline failure",
  "severity": "high",
  "summary": "Database timeouts delayed the sales dashboard.",
  "affected_system": "orders pipeline",
  "action_required": true
}
"""


class FakeModelClient:
    """A controllable client for testing."""

    def __init__(self, response: str):
        self.response = response
        self.last_prompt = None

    def generate(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response


class FailingModelClient:
    def generate(self, prompt: str) -> str:
        raise TimeoutError("Simulated timeout")


def test_valid_incident_summary():
    incident = IncidentSummary.model_validate_json(VALID_JSON)

    assert incident.severity == "high"
    assert incident.action_required is True


def test_invalid_severity_is_rejected():
    with pytest.raises(ValidationError):
        IncidentSummary(
            title="Orders pipeline failure",
            severity="urgent",
            summary="Database timeouts delayed the sales dashboard.",
            affected_system="orders pipeline",
            action_required=True,
        )


def test_title_too_short_is_rejected():
    with pytest.raises(ValidationError):
        IncidentSummary(
            title="X",
            severity="high",
            summary="Database timeouts delayed the sales dashboard.",
            affected_system="orders pipeline",
            action_required=True,
        )


def test_missing_required_field_is_rejected():
    with pytest.raises(ValidationError):
        IncidentSummary.model_validate_json(
            """
            {
              "title": "Orders pipeline failure",
              "severity": "high",
              "summary": "Database timeouts delayed the sales dashboard.",
              "action_required": true
            }
            """
        )


def test_malformed_json_is_rejected():
    with pytest.raises(ValidationError):
        IncidentSummary.model_validate_json(
            '{"title": "Orders pipeline", "severity": '
        )


def test_empty_json_object_is_rejected():
    with pytest.raises(ValidationError):
        IncidentSummary.model_validate_json("{}")


def test_extract_summary_returns_validated_output():
    client = FakeModelClient(VALID_JSON)

    result = extract_summary(
        "The orders pipeline failed due to database timeouts.",
        client,
    )

    assert isinstance(result, IncidentSummary)
    assert result.severity == "high"
    assert "untrusted data" in client.last_prompt


def test_empty_input_is_rejected_before_client_call():
    client = FakeModelClient(VALID_JSON)

    with pytest.raises(ValueError, match="must not be empty"):
        extract_summary("   ", client)

    assert client.last_prompt is None


def test_invalid_model_output_is_rejected():
    client = FakeModelClient(
        '{"title": "Bad incident", "severity": "urgent"}'
    )

    with pytest.raises(SummaryOutputError):
        extract_summary("A pipeline failed.", client)


def test_model_client_failure_is_wrapped():
    with pytest.raises(ModelClientError):
        extract_summary("A pipeline failed.", FailingModelClient())


def test_demo_client_returns_valid_fixture():
    result = extract_summary(
        "Example incident text.",
        DemoModelClient(),
    )

    assert result.title == "Orders pipeline failure"
    assert result.severity == "high"


def test_successful_extraction_logs_duration(caplog):
    client = FakeModelClient(VALID_JSON)

    with caplog.at_level(logging.INFO):
        result = extract_summary("A pipeline failed.", client)

    assert isinstance(result, IncidentSummary)
    assert "incident_extraction_succeeded" in caplog.text
    assert "duration_ms=" in caplog.text
    assert "FakeModelClient" in caplog.text
