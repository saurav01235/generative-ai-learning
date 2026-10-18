# 24-Week Generative AI Engineering Roadmap

**Goal:** Build practical skills for Senior Data Engineer, AI Engineer,
and GenAI-focused roles, with an emphasis on secure, measurable,
production-ready systems.

## Starting point and constraints

-   **Experience:** 6 years in Data Engineering; Data Platform Engineer.
-   **Existing stack:** Azure, Azure Databricks, and Cribl.
-   **Study time:** 7--9 hours per week for 24 weeks (about 168--216
    hours).
-   **Development environment:** VS Code on a personal laptop.
-   **Cloud access:** Azure AI access is through a company-managed
    environment. Use only approved endpoints, identities, data, and
    services.
-   **Portfolio safety:** Never publish company-confidential
    information, source code, logs, customer data, credentials, or
    internal architecture. Use public or synthetic data.

## How to use this roadmap

1.  Work through the weeks in order, but adjust the pace if a topic
    needs more practice.
2.  Build something every week. Prefer a small working implementation
    over passive course completion.
3.  Keep notes on decisions, evaluation results, failures, and
    trade-offs.
4.  Push only sanitized code and synthetic/public examples to GitHub.
5.  At the end of each phase, review what works, what is measured, and
    what would be needed for production.

## Weekly study rhythm

A practical 7--9 hour schedule:

-   **Two weekday sessions --- 1 hour each:** Learn concepts and take
    notes.
-   **One weekday session --- 1 hour:** Implement a small feature.
-   **Weekend build session --- 4--6 hours:** Integrate, test, document,
    and commit.
-   **End of week --- 15 minutes:** Write a short progress note and
    choose the next task.

------------------------------------------------------------------------

## Phase 1 --- LLM foundations (Weeks 1--4)

### Week 1 --- LLM basics and structured outputs

**Learn** - Tokens, context windows, inference, system/user
instructions, prompting, temperature, and structured outputs. - Why LLM
responses can be incomplete or invalid and why application-side
validation matters.

**Build** - A Python incident-summary extractor using Pydantic. - Define
a provider-independent `ModelClient` interface and a deterministic demo
client. - Parse and validate JSON output; allow only known severity
values. - Log latency and token counts as synthetic/demo metrics when no
approved model is connected.

**Acceptance criteria** - Tests cover valid output, empty input,
malformed JSON, invalid severity, missing fields, and
prompt-injection-style input. - The demo works without cloud
credentials. - README explains how to replace the demo client with an
approved model adapter.

### Week 2 --- Embeddings and semantic search

**Learn** - Embeddings, cosine similarity, vector indexes, and semantic
search limitations.

**Build** - Index 500--2,000 public or synthetic documents with FAISS or
another lightweight vector store. - Create a small query script and
inspect top-k results.

**Acceptance criteria** - A repeatable indexing script exists. - You
have a small set of example queries and expected relevant documents. -
Notes describe cases where semantic search retrieves the wrong result.

### Week 3 --- Retrieval-augmented generation (RAG)

**Learn** - Document parsing, chunking, retrieval, context assembly,
citations, and grounding.

**Build** - A question-answering prototype over your indexed
documents. - Include source references and an explicit "I don't know"
path when evidence is insufficient.

**Acceptance criteria** - Answers identify supporting documents or
chunks. - The app distinguishes retrieved evidence from generated
explanation. - At least a few unanswerable questions are tested.

### Week 4 --- Evaluation fundamentals

**Learn** - Retrieval quality, answer correctness, groundedness,
latency, and cost. - Why a few impressive demos are not evidence of
reliable performance.

**Build** - Create 30--50 evaluation questions with expected evidence or
answers. - Compare at least two chunking or retrieval strategies.

**Acceptance criteria** - A baseline and an improved run are recorded. -
A short report explains the metrics, failures, and trade-offs. -
Evaluation can be rerun from documented instructions.

------------------------------------------------------------------------

## Phase 2 --- Azure and Databricks (Weeks 5--8)

### Week 5 --- Approved model endpoints and cloud integration

**Learn** - Azure model endpoints, authentication, quotas, deployment
configuration, and provider abstraction.

**Build** - Add a provider-specific adapter behind your `ModelClient`
interface, but only after your company platform team approves the
endpoint and access method. - Keep the local demo client available for
development and tests.

**Acceptance criteria** - Credentials are not hard-coded or committed. -
Authentication and error handling are documented. - The app can switch
between demo and approved client through configuration.

### Week 6 --- Azure AI Search and hybrid retrieval

**Learn** - Keyword search, vector search, hybrid search, metadata
filters, and ranking.

**Build** - Move or reproduce your RAG retrieval layer using Azure AI
Search if approved access is available. - Compare keyword, vector, and
hybrid retrieval on the same evaluation set.

**Acceptance criteria** - Retrieval results and settings are
reproducible. - Filters are tested. - The report compares relevance and
latency.

### Week 7 --- Databricks and data pipelines

**Learn** - Delta tables, Spark, Unity Catalog concepts, incremental
ingestion, and index synchronization.

**Build** - Create a restartable ingestion pipeline that handles new
documents, updates, and deletes. - Use Databricks Vector Search only if
available and approved; otherwise keep a local implementation and
document the intended cloud architecture.

**Acceptance criteria** - Re-running the pipeline does not create
duplicate records. - Updates and deletes propagate correctly. - Pipeline
state and failure behavior are documented.

### Week 8 --- MLflow, tracing, and evaluation

**Learn** - Prompt/version tracking, traces, evaluation runs, and
release gates.

**Build** - Add structured traces and automated evaluation to your RAG
app. - Use MLflow or the approved equivalent where available.

**Acceptance criteria** - You can inspect a run and identify
prompt/model/retrieval configuration. - Evaluation runs can be compared
over time. - A failing quality check can block a release or produce a
clear warning.

------------------------------------------------------------------------

## Phase 3 --- Production engineering (Weeks 9--12)

### Week 9 --- Security and governance

**Learn** - Entra ID, managed identities, RBAC, Key Vault, network
boundaries, data classification, and threat modeling.

**Build** - Write a threat model for your RAG application. - Document
authentication, authorization, secrets handling, data retention, and
logging decisions.

**Acceptance criteria** - Access is least-privilege by design. -
Sensitive content and credentials are excluded from source control and
unnecessary logs. - Security assumptions and unresolved questions are
visible.

### Week 10 --- Advanced RAG

**Learn** - Hybrid retrieval, reranking, query rewriting, parent-child
chunking, metadata filtering, and retrieval failure analysis.

**Build** - Test at least two advanced retrieval techniques against your
baseline.

**Acceptance criteria** - The evaluation set is unchanged for a fair
comparison. - Quality, latency, and estimated cost are compared. - The
chosen design is justified with evidence.

### Week 11 --- LLM operations and monitoring

**Learn** - Retries, rate limits, caching, token budgets, timeouts,
fallbacks, and operational metrics.

**Build** - Add safe retry behavior, request limits, error handling, and
a monitoring dashboard or report. - Write a runbook for common failures.

**Acceptance criteria** - Tests cover timeout, rate limit, malformed
response, and dependency failure. - Logs and metrics support
troubleshooting without leaking sensitive content. - A load or stress
test records latency and failure rates.

### Week 12 --- Packaging, CI/CD, and deployment

**Learn** - Docker, automated tests, deployment pipelines,
configuration, and infrastructure-as-code concepts.

**Build** - Containerize the application and add CI checks. - Deploy
only to an approved environment; otherwise document the deployment steps
and validate locally.

**Acceptance criteria** - A clean checkout can be installed and tested
using the README. - CI runs tests and basic quality checks. - Deployment
and rollback steps are documented.

------------------------------------------------------------------------

## Phase 4 --- Agents and tool use (Weeks 13--16)

### Week 13 --- Tool calling

**Learn** - Typed tool schemas, validation, retries, idempotency, and
permission boundaries.

**Build** - Add a small set of read-only tools, such as searching a
knowledge base or looking up a synthetic incident.

**Acceptance criteria** - Tool inputs and outputs are validated. -
Invalid requests fail safely. - Tool calls are logged with appropriate
redaction.

### Week 14 --- Agent workflows

**Learn** - Agent state, routing, orchestration, workflow graphs, and
when a deterministic workflow is preferable to an agent.

**Build** - Create an incident-triage assistant over synthetic telemetry
and runbooks. - Have it retrieve evidence and call read-only tools
before producing a summary.

**Acceptance criteria** - The workflow has clear boundaries and a
bounded set of tools. - The output includes evidence and uncertainty. -
A deterministic fallback exists for important paths.

### Week 15 --- Agent evaluation and security

**Learn** - Prompt injection, tool misuse, data exfiltration risks,
agent evaluation, and human approval patterns.

**Build** - Create adversarial and normal test cases. - Test whether
untrusted content can change tool permissions or override the intended
workflow.

**Acceptance criteria** - The test suite includes injection attempts and
unauthorized actions. - The agent cannot perform destructive actions. -
Findings and mitigations are documented.

### Week 16 --- Model selection and fine-tuning trade-offs

**Learn** - Model quality, latency, cost, context size, RAG versus
fine-tuning, and LoRA/QLoRA concepts.

**Build** - Compare a small number of suitable models or configurations
using the same evaluation set, where approved access permits. - If
fine-tuning is impractical, write a decision memo explaining why.

**Acceptance criteria** - A model comparison covers quality, latency,
cost, and operational constraints. - The decision to use RAG, prompting,
or fine-tuning is evidence-based.

------------------------------------------------------------------------

## Phase 5 --- Capstone project (Weeks 17--20)

### Week 17 --- Design the capstone

**Build** - Choose one focused business problem. - Write requirements,
non-goals, data assumptions, a system architecture diagram, and
architecture decision records (ADRs).

**Acceptance criteria** - The MVP is small enough to finish in four
weeks. - Security, evaluation, and operational requirements are part of
the design from the start.

### Week 18 --- Build the data and retrieval pipeline

**Build** - Implement ingestion, validation, transformation, indexing,
incremental updates, and failure recovery.

**Acceptance criteria** - Pipeline runs are repeatable and observable. -
Tests cover duplicates, updates, malformed records, and recovery.

### Week 19 --- Build the application

**Build** - Implement an API or small UI, model/retrieval integration,
authentication where available, evaluation, and observability.

**Acceptance criteria** - Main user journeys work end to end. - Failures
return useful, safe errors. - Evaluation can run automatically.

### Week 20 --- Test and present the capstone

**Build** - Test quality, latency, cost, load, and dependency
failures. - Write a technical case study with measured results and
limitations.

**Acceptance criteria** - Results are based on recorded tests rather
than estimates presented as facts. - README includes architecture,
setup, evaluation, security notes, and limitations. - A short demo is
ready.

------------------------------------------------------------------------

## Phase 6 --- Interview and career preparation (Weeks 21--24)

### Week 21 --- Senior data engineering interviews

**Practice** - SQL, Spark, distributed systems, CDC, streaming, data
modeling, reliability, and performance tuning.

**Deliverable** - A set of solved practice problems and concise
explanations of trade-offs.

### Week 22 --- GenAI system design

**Practice** - Enterprise RAG, data copilots, model serving, ingestion
and indexing, security, evaluation, and observability.

**Deliverable** - Four architecture walkthroughs with diagrams, failure
modes, scaling choices, and cost/quality trade-offs.

### Week 23 --- Senior engineering communication

**Practice** - Design reviews, incident retrospectives, stakeholder
communication, prioritization, and explaining trade-offs.

**Deliverable** - A 10-minute project presentation and answers to likely
review questions.

### Week 24 --- Portfolio and job materials

**Build** - Polish GitHub repositories, READMEs, architecture diagrams,
demo recordings, CV bullets, and project case studies.

**Acceptance criteria** - Two or three projects are easy to run or
understand. - Each project explains the problem, architecture,
decisions, evaluation results, limitations, and next steps. - No
confidential employer data or implementation details are exposed.

------------------------------------------------------------------------

## Portfolio projects

### Project 1 --- Enterprise Knowledge Copilot (Weeks 1--8)

**Stack:** Python, Pydantic, a vector store, Azure AI Search/Databricks
where approved, and an approved LLM endpoint if available.

**Features** - Document ingestion and chunking - Embeddings and hybrid
retrieval - Answers with citations and an abstain path - Evaluation
dataset and baseline/improved comparison - Incremental indexing and
documented access controls

### Project 2 --- AI Observability and Incident Assistant (Weeks 9--16)

**Stack:** Python, synthetic logs/events/runbooks, retrieval, typed
read-only tools, and tracing.

**Features** - Incident summaries and evidence collection - Runbook
retrieval - Read-only tool calls - Prompt-injection and authorization
tests - Traceability, quality metrics, latency, and cost reporting

**Cribl connection:** Use a Cribl-inspired telemetry shape or
public/synthetic events to demonstrate how operational data can support
incident workflows. Do not export or publish company telemetry.

### Project 3 --- Governed Data Platform Copilot (Weeks 17--20)

**Stack:** Python, synthetic datasets, SQL validation, metadata/lineage
examples, and a model adapter.

**Features** - Schema discovery - SQL generation with validation -
Read-only query execution against synthetic data - Authorization checks,
audit records, and lineage context - Clear handling of ambiguous or
unsupported requests

### Minimum deliverables for every project

-   `README.md` with problem statement, setup, and usage
-   Architecture diagram
-   Tests and a small evaluation dataset
-   Evaluation results with limitations
-   Security and privacy notes
-   Reproducible setup instructions
-   Short demo video or screenshots using only safe data

------------------------------------------------------------------------

## Week 1 starter repository

Suggested structure:

``` text
week-01-llm-fundamentals/
├── src/
│   └── genai_week1/
│       ├── __init__.py
│       └── app.py
├── tests/
│   └── test_app.py
├── .gitignore
├── requirements.txt
└── README.md

genai-engineering-roadmap/
├── README.md
├── genai_24_week_roadmap.md
├── week-01-llm-fundamentals/
├── week-02-embeddings-search/
├── week-03-rag/
├── week-04-evaluation/
└── projects/
    ├── enterprise-knowledge-copilot/
    ├── incident-assistant/
    └── data-platform-copilot/
```

Suggested `.gitignore`:

``` gitignore
.venv/
__pycache__/
.pytest_cache/
.env
*.py[cod]
```

Week 1 implementation checklist: - \[ \] Create a Python 3.11 or 3.12
virtual environment. - \[ \] Install `pydantic` and `pytest`. - \[ \]
Define a typed `ModelClient` protocol. - \[ \] Implement a deterministic
`DemoModelClient`. - \[ \] Validate structured incident summaries with
Pydantic. - \[ \] Add tests for valid output, empty input, malformed
JSON, invalid severity, missing fields, and prompt-injection-style
input. - \[ \] Run `python -m pytest -q`. - \[ \] Document how to add an
approved provider adapter later. - \[ \] Commit the sanitized project to
GitHub.

**Company-managed Azure access checklist** - Ask the platform/AI
enablement team for the approved endpoint and SDK. - Confirm the
supported identity/authentication method, required roles, network/VPN
requirements, and quota limits. - Confirm which data may be sent to the
model and how prompts, responses, and traces may be logged or
retained. - Confirm cost controls and approved deployment
environments. - Do not use unapproved endpoints, personal keys, or
sensitive company data in experiments.

------------------------------------------------------------------------

## Recommended learning resources

-   [Hugging Face LLM
    Course](https://huggingface.co/learn/llm-course/chapter1/1) --- LLM
    and transformer foundations.
-   [Microsoft Learn: Develop generative AI
    apps](https://learn.microsoft.com/en-us/training/paths/develop-generative-ai-apps/)
    --- Azure-oriented application development.
-   [Azure AI Search: RAG
    overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=docs)
    --- retrieval architecture.
-   [DeepLearning.AI: Building and Evaluating Advanced
    RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)
    --- retrieval improvements and evaluation.
-   [Databricks MLflow GenAI evaluation and
    monitoring](https://learn.microsoft.com/en-us/azure/databricks/mlflow3/genai/eval-monitor/)
    --- evaluation and tracing in Databricks.
-   [DeepLearning.AI: Evaluating AI
    Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)
    --- agent evaluation.
-   [Cribl documentation](https://docs.cribl.io/) --- telemetry pipeline
    concepts and product documentation.
-   [Pydantic documentation](https://docs.pydantic.dev/latest/) ---
    typed data validation.

Course availability, product features, and certification details can
change; verify current documentation before committing to a specific
certification or service.

## Progress tracker

Use this checklist in GitHub and tick items as you complete them.

-   [ ] Weeks 1--4: LLM foundations, embeddings, RAG, evaluation
-   [ ] Weeks 5--8: Azure/Databricks integration, hybrid retrieval,
    tracing
-   [ ] Weeks 9--12: Security, advanced RAG, operations, deployment
-   [ ] Weeks 13--16: Tool calling, agent workflows, safety, model
    selection
-   [ ] Weeks 17--20: Capstone design, pipeline, app, testing and case
    study
-   [ ] Weeks 21--24: Interviews, system design, communication,
    portfolio polish

## Definition of success

By the end of 24 weeks, aim to have: - Two or three well-documented,
safe-to-share projects. - A repeatable evaluation process and evidence
of quality/latency/cost trade-offs. - A working understanding of RAG,
tool use, LLMOps, governance, and production integration. - Architecture
diagrams, ADRs, tests, runbooks, and demos that show senior-level
engineering judgment. - Clear interview stories about design decisions,
failures, trade-offs, and measurable outcomes.

**Guiding principle:** Do not aim merely to build a chatbot. Aim to
demonstrate that you can build a governed, testable, observable
AI-enabled data product.
