# Rationalizations to Reject

Reject these immediately unless backed by explicit evidence.

## Access control

- "The UI hides the button."
- "Nobody knows the endpoint."
- "The ID is hard to guess."
- "Only internal users can call it."
- "The frontend sends the tenant ID correctly."
- "Admins are trusted, so authorization is unnecessary."

## Injection / parsing

- "We validate input already."
- "The ORM makes all strings safe."
- "Nobody would upload that kind of file."
- "The extension is `.jpg`, so it is an image."
- "We escaped it once upstream."

## Dependencies

- "It is a popular package."
- "The CVSS is low."
- "There is no public exploit."
- "The lockfile is enough to guarantee safety."
- "The vulnerable function probably isn't used."

## Secrets / crypto

- "The key is only in Git history."
- "The mobile app can hide the API secret."
- "Base64 is encryption."
- "TLS verification is annoying in development."
- "We use SHA-256, so password storage is strong."

## Dynamic testing

- "The scanner exited zero."
- "One DAST tool found nothing."
- "The route wasn't discovered, so it must be safe."
- "The WAF blocked the proof, so the code is fixed."

## Testing

- "The security test is flaky, disable it."
- "The build passes, therefore the security patch works."
- "The PoC no longer returns 200, so it is fixed" without checking failure semantics.

## Cloud

- "The bucket name is obscure."
- "The service is in a private subnet, so auth is unnecessary."
- "The IAM wildcard is easier."
- "Production firewall will save us."

## AI / agents

- "The model won't follow malicious instructions."
- "The system prompt says not to reveal secrets."
- "Only the model calls the tool."
- "RAG documents are trusted because they came from users."
- "The agent needs admin rights to be useful."

## Process

- "Security can be added after launch."
- "No finding means no risk."
- "100% secure."
