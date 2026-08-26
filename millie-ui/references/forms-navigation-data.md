# Forms, Navigation & Data

## Navigation pattern selection

Top nav:
- shallow public hierarchy;
- limited primary destinations.

Sidebar/pane:
- application hierarchy;
- frequent switching;
- many tools/sections.

Bottom/tab navigation:
- few primary mobile destinations.

Breadcrumb:
- deep hierarchy/location.

Command palette:
- expert/keyboard complement, not only navigation path.

Master-detail:
- repeated inspection of list items.

## Forms

Prefer single column unless short fields form a natural group.

Use steps when complexity/dependency justifies them.

Every control:
- visible label;
- instructions where needed;
- correct semantic type;
- error relationship;
- focus state;
- disabled/loading state.

Use autocomplete/inputmode where relevant.

Preserve values after errors.

Do not use placeholder as label.

## Validation

- prevent impossible choices;
- validate at a point useful to the user;
- avoid error spam while typing;
- error copy says what happened and how to fix it.

Long form:
- consider error summary with links;
- preserve position and values.

## Tables

For comparison:
- aligned columns;
- units;
- sorting/filtering state;
- empty/error/loading;
- responsive local overflow or column prioritization;
- row actions discoverable by keyboard/touch.

## Data visualization

Choose chart by question:
- trend -> line/area;
- category comparison -> bar;
- part-to-whole -> use sparingly, often bar is clearer;
- distribution -> histogram/box;
- correlation -> scatter;
- status -> direct label/number when chart adds no insight.

Rules:
- real data only;
- label units/time range;
- show freshness;
- accessible palette;
- avoid rainbow categorical color when position/label can work;
- provide textual/table alternative for important data;
- do not use 3D chart effects for ordinary quantitative comparison.
