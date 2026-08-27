# Files, Uploads, Archives & Parsers

Untrusted files are programs for parsers.

## Upload policy

Define:
- allowed purpose;
- allowed types;
- maximum size;
- storage location;
- execution policy;
- retrieval policy;
- scanning/transformation needs.

Validate content, not filename extension alone.

## Storage

Prefer:
- generated storage names;
- non-executable storage;
- outside web root where appropriate;
- separate origin/domain for untrusted active content;
- authorization on retrieval.

## MIME/content

Client MIME is untrusted.
Use parser/magic/content validation where appropriate.

## Images/documents/media

Treat native parsers/converters as attack surfaces.
Keep dependencies patched and isolate high-risk transformations when practical.

## Archives

Defend against:
- traversal/zip-slip;
- symlink escape;
- excessive nested entries;
- decompression bombs;
- huge total expanded size;
- duplicate/conflicting paths.

Extract into controlled temporary root with quotas.

## XML

Disable external entities/network/file resolution unless explicitly needed and safely isolated.

## Deserialization

Avoid native object deserialization of untrusted input.
Prefer explicit schema-bound data.

## Path traversal

Resolve canonical target and prove it remains under the authorized root.
Re-check symlinks/race considerations where relevant.

## Download

Set safe `Content-Disposition`/type and authorization.
Do not let untrusted filenames create header injection.
