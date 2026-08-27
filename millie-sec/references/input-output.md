# Input, Output, Parsing & Injection

"Validate input" is not a complete defense. Defense depends on the sink.

## SQL / database query injection

Prefer:
- parameterized queries;
- ORM bindings;
- strict allowlists for non-parameterizable identifiers.

Do not construct query syntax by concatenating untrusted strings.

## Command/process execution

Prefer:
- direct argument arrays;
- fixed executable;
- strict allowlists;
- no shell interpretation when unnecessary;
- least-privilege subprocess.

Never solve command injection with a small character blocklist.

## HTML / XSS

Use:
- framework auto-escaping;
- context-aware encoding;
- safe DOM APIs;
- sanitization only for intentionally allowed rich HTML;
- CSP as defense-in-depth.

Treat URL, HTML attribute, JavaScript and CSS contexts differently.

## Template/expression injection

Do not evaluate user-controlled templates/code.
If templating is a product feature:
- sandbox strongly;
- expose minimal capabilities;
- bound resources;
- isolate secrets/files/network.

## NoSQL/ORM filters

Avoid directly accepting arbitrary operator objects/filters from untrusted clients.
Map user choices into trusted query structure.

## Path handling

- canonicalize;
- resolve beneath an allowed root;
- reject escapes;
- avoid trusting filename alone;
- handle symlinks.

## XML / structured parsers

Disable external entity/network/file resolution unless required and safely constrained.
Bound recursion/size.

## Serialization

Avoid unsafe object deserialization of untrusted data.
Use simple data formats and explicit schemas.

## Output

Security-sensitive output includes:
- HTML;
- shell;
- SQL;
- logs;
- CSV/formula contexts;
- HTTP headers;
- redirects;
- file paths;
- model/tool prompts.

Encode or constrain at the sink.
