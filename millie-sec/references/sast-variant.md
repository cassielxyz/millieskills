# SAST & Variant Analysis

## Static analysis layers

1. compiler/type/language diagnostics;
2. framework-specific checks;
3. pattern SAST;
4. taint/data-flow analysis;
5. query-based analysis;
6. manual semantic audit.

## Taint model

For security-relevant paths identify:
- untrusted source;
- normalization;
- validation;
- authorization;
- sanitizer/encoder;
- sink.

Do not call generic validation a sanitizer without sink-specific proof.

## Semgrep

Useful for:
- patterns;
- taint;
- CI;
- custom rules;
- variant hunting.

When creating a project-specific rule:
- start from a known bad instance;
- create positive/negative fixtures;
- use taint mode for source-to-sink classes where appropriate;
- avoid overly broad regex-only rules.

## CodeQL

Useful for:
- semantic data-flow;
- cross-function queries;
- variant analysis;
- large codebases.

Treat query output as candidate evidence requiring context.

## Variant analysis

After confirming a root cause:
1. define the exact vulnerable pattern;
2. find the known instance with the search/query;
3. generalize one dimension at a time;
4. review every new match;
5. continue until additional generalization becomes noise.

Expansion axes:
- sibling sink APIs;
- alternate wrappers;
- renamed helper;
- related routes/controllers;
- same authorization rule duplicated elsewhere;
- alternate parser/file format;
- different tenant/object type.

## False-negative traps

Static tools often struggle with:
- reflection;
- dynamic dispatch;
- generated routes;
- templates;
- ORM abstractions;
- framework magic;
- external consumers;
- native/FFI;
- runtime policy.

Use manual/runtime evidence to close gaps.
