# Google Stitch Integration

This is conditional. Use only when Stitch MCP/tools are configured or the user explicitly asks for a
Stitch workflow.

## Standalone fallback
Millie remains fully functional without Stitch. Do not invent MCP calls.

## Generate flow
1. understand product/surface mode;
2. check/create project via actual available Stitch tools;
3. check design system;
4. if a design system exists, do not contradict it with duplicate ad-hoc theme instructions;
5. enhance vague prompt into precise UI/UX terminology;
6. choose text vs image generation and device type;
7. request meaningful variants only when comparison helps;
8. inspect generated screen and feedback;
9. bring selected result back to project;
10. productionize semantics, states, responsiveness, accessibility and data contracts.

## DESIGN.md synchronization
Stitch design workflows use DESIGN.md as a source of truth. Avoid two divergent design documents.
If the project uses `.stitch/DESIGN.md`, establish whether root `DESIGN.md` mirrors, references, or is
canonical before editing.

## Code -> design / design -> code
Use when supported for collaborative iteration, but verify extraction/generated code rather than
assuming it preserves production architecture.

## Confirmation
Respect any external-tool operation that requires user approval before uploading/publishing a design
system or project data.
