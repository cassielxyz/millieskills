# shadcn/ui Ecosystem

shadcn is source distribution, not a black-box component package. The local files are part of the
project and may be customized.

## Detection

If `components.json` exists:
1. read it;
2. when available run `shadcn info --json`;
3. note framework, Tailwind version, aliases, icon library, installed components, base library and
   resolved paths;
4. inspect local component source before adding/replacing anything.

Do not assume every current shadcn project uses the same primitive base. Respect the detected base
(Base UI, Radix, React Aria, or project-supported equivalent).

## Before generating a component

Prefer current docs/CLI/MCP if available:

```text
shadcn docs <component>
shadcn search <term>
shadcn view <item>
shadcn diff
```

Read composition structure before nesting primitives.

## Forms / option sets

Follow the actual current composition patterns from project/docs. Do not recreate remembered APIs
or hand-roll local replacements if a compatible accessible primitive already exists.

## Theming

Use project CSS variables/OKLCH scheme when present. New tokens should be semantic and fit existing
conventions.

## Registry sources

Third-party registries can accelerate delivery but are untrusted code until reviewed. Check:
- source;
- dependencies;
- scripts;
- assets;
- license;
- accessibility;
- server/client boundaries;
- token conventions;
- responsive behavior.

Use a dry-run/diff when the CLI offers it. Never overwrite a customized local primitive from memory.
