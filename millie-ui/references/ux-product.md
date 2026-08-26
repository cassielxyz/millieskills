# UX & Product Interaction

Visual quality cannot rescue a poor task model.

## 1. Primary-job map

Define:
- entry condition;
- user goal;
- success condition;
- major decision points;
- failure/recovery paths;
- destructive actions;
- resumability.

## 2. Information architecture

Group by user mental model, not database schema.

Use:
- progressive disclosure;
- stable labels;
- visible location;
- local context;
- clear hierarchy.

Avoid:
- hiding frequent actions in overflow;
- nesting navigation deeper than the content model requires;
- creating separate pages for states that can be resolved locally;
- putting unrelated settings together because they share storage code.

## 3. Recognition over recall

Prefer visible choices, recent items, examples, previews, and context.

Do not make users remember:
- IDs;
- previous state;
- hidden formatting rules;
- error causes;
- navigation location.

## 4. Error prevention

Prefer:
- constraints;
- smart defaults;
- inline validation at an appropriate point;
- disabled impossible actions;
- previews for destructive transformations;
- reversible actions and undo.

Do not disable a submit button with no explanation of what remains invalid.

## 5. System status

User action needs feedback.

Rough mental model:
- immediate visual acknowledgement for input;
- visible progress when waiting becomes noticeable;
- explicit success when completion is not obvious;
- useful recovery when failure occurs.

## 6. Destructive actions

Use consequence-based treatment:
- low-cost reversible: act + undo;
- moderate: explicit destructive styling and clear copy;
- high-cost/irreversible: confirmation that names the object/consequence.

Avoid confirmation dialogs for every trivial action.

## 7. Onboarding

Teach by helping the user reach value, not by presenting a tour of every feature.

Good:
- progressive onboarding;
- contextual help;
- sample content when truthful;
- useful empty state;
- clear first success.

## 8. Empty state

Answer:
- why is this empty?
- is it expected?
- what should appear?
- what can the user do?
- is there a permission/filter issue?

## 9. Wizards / long flows

Use steps when:
- fields depend on previous choices;
- sections are cognitively distinct;
- there are many fields;
- users benefit from progress/resume.

Preserve progress across recoverable errors.

## 10. Keyboard power-user UX

For pro tools:
- shortcuts;
- command palette;
- focus model;
- predictable tab order;
- visible shortcut hints where helpful.

Do not make expert shortcuts the only path.
