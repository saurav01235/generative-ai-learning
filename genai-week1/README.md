
# GenAI Week 1 — Incident Summary Extractor

A small Python project exploring structured outputs, input validation,
provider-independent model interfaces, and safe operational logging.

## Goal

Build the application foundations for an AI-powered incident summarizer.
The current version uses a deterministic demo client and does not call
a real LLM.

## Architecture

- `IncidentSummary`: Pydantic schema for validated incident output.
- `ModelClient`: protocol defining the model client contract.
- `DemoModelClient`: deterministic JSON fixture for local development.
- `extract_summary()`: validates input, calls the client, parses JSON,
  validates the response, and records operational events.

## Requirements

- Python 3.11 or 3.12
- pip
- Git

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python src/genai_week1/app.py
```

## Tests

```bash
python -m pytest -v
```

The tests cover valid output, invalid severity, missing fields,
malformed JSON, empty input, client failures, and operational logging.

## Observability

The application records success/failure events and elapsed duration
in milliseconds. Incident text, prompts, and raw responses are not
written to the application logs by this implementation.

Latency from `DemoModelClient` is local application execution time,
not real model inference latency.

## Security and limitations

- The demo client returns a fixed fixture; it does not summarize the
  supplied incident text.
- Pydantic validates structure and constraints, not factual correctness.
- The prompt's untrusted-input instruction is not a complete prompt
  injection defense.
- No real model endpoint or credentials are required.
- A production integration would require approved model access,
  appropriate access controls, data handling review, and more tests.

## Next steps

- Add a real model adapter when an approved endpoint is available.
- Build a representative evaluation dataset.
- Add controlled retry/timeout behavior and more detailed metrics.
- Evaluate summary correctness and groundedness.

## Learning outcomes

- Pydantic data contracts
- Python protocols and dependency inversion
- Automated testing with pytest
- Error handling and operational logging
