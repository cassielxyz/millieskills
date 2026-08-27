# AI / Agent Security Workflow

## Map agent authority

For each model/agent:
- input sources;
- system/developer instructions;
- tools;
- tool credentials;
- file access;
- network access;
- databases/RAG;
- approval gates;
- autonomous loops;
- subagents;
- persistent memory.

## Threat paths

Review:
- prompt injection from user/web/email/docs;
- tool misuse;
- cross-tenant retrieval;
- secret/prompt leakage;
- unsafe output passed to code/shell/SQL/HTML;
- poisoned RAG/data;
- excessive agency;
- unbounded cost/loops;
- identity confusion/delegation.

## Security model

The model is not the authorization boundary.

Enforce outside the model:
- tool ACLs;
- server authz;
- tenant filters;
- resource limits;
- destination allowlists;
- approval for high-impact operations.

## Tests

Create adversarial but safe tests:
- untrusted document requests a forbidden tool action;
- model tries to access unrelated tenant content;
- tool output contains hostile instructions;
- generated output attempts dangerous sink;
- recursive action exceeds budget.

Expected result is controlled refusal/containment at the system/tool boundary.

## Exit

Record residual model-behavior uncertainty separately from deterministic control coverage.
