# AI & Agentic Application Security

AI systems add untrusted-instruction and tool-boundary risks.

## Model input is untrusted

Treat as untrusted:
- user prompts;
- web pages;
- retrieved documents;
- email;
- files;
- tool output;
- code comments;
- third-party APIs.

Prompt injection cannot be solved by "tell the model to ignore malicious instructions" alone.

## Tool permissions

Each tool should have:
- narrow capability;
- least privilege;
- explicit input schema;
- server-side authorization;
- bounded resource use;
- sensitive-action confirmation where appropriate;
- audit trail.

The model is not the authorization boundary.

## Data exfiltration

Prevent tools/models from freely reading:
- credentials;
- unrelated tenant data;
- arbitrary local files;
- production secrets.

Then prevent arbitrary outbound channels from carrying protected data.

## RAG

Review:
- document authorization;
- tenant-aware retrieval;
- poisoning;
- embedding/vector store isolation;
- metadata filtering;
- source trust;
- output attribution.

## Excessive agency

For high-impact actions:
- human confirmation;
- transaction limits;
- allowlisted destinations;
- preview/plan;
- idempotency;
- rollback.

## Output handling

Model output is untrusted when passed into:
- shell;
- SQL;
- HTML;
- file path;
- code execution;
- URLs;
- tool parameters.

Use normal sink-specific security controls.

## Secrets and system prompts

Do not place live secrets in prompts/system instructions.
Assume prompt text may be exposed indirectly.

## Cost / availability

Bound:
- token usage;
- tool loops;
- recursive agents;
- file sizes;
- external calls;
- model retries.

## Agent identity

If multiple agents/services act on behalf of users, preserve:
- initiating user;
- effective identity;
- delegated permissions;
- audit attribution;
- approval context.
