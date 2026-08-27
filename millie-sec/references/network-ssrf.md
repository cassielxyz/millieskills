# SSRF, Network & Egress

Any server-side feature that fetches a user-influenced URL can cross a trust boundary.

Examples:
- webhook tester;
- URL preview;
- image import;
- PDF generator;
- proxy;
- callback;
- feed import;
- cloud integration;
- AI tool.

## Preferred design

Best defense:
- do not allow arbitrary destinations.

Next:
- explicit destination allowlist;
- fixed scheme;
- fixed port where practical;
- parse with standard URL library;
- resolve host;
- block disallowed address classes;
- re-check redirect destinations;
- restrict outbound network at infrastructure layer.

## Address classes to consider

Based on environment, reject destinations such as:
- loopback;
- private RFC1918;
- link-local;
- unique/local IPv6;
- metadata-service addresses;
- multicast/unspecified/reserved.

Do not rely on string-prefix IP checks.

## DNS

Consider:
- multiple answers;
- IPv6;
- rebinding/time-of-check differences;
- redirects;
- encoded/alternate address forms.

## Egress defense

For sensitive services, infrastructure egress controls can reduce impact even if application URL
validation fails.

## Response handling

Bound:
- response size;
- timeout;
- redirects;
- content type;
- decompression;
- parser behavior.

Do not expose arbitrary fetched response headers/body back to users without considering sensitive
internal data.
