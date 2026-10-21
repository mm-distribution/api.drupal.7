# modules/field/field.default.inc

- **Source:** [local](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · 269 lines
- **Module/theme:** field

## File documentation

```text
@file
Default 'implementations' of hook_field_*(): common field housekeeping.

Those implementations are special, as field.module does not define any field
types. Those functions take care of default stuff common to all field types.
They are called through the _field_invoke_default() iterator, generally in
the corresponding field_attach_[operation]() function.
```

## Functions (derived index)

- [field_default_extract_form_values()](field_default_extract_form_values.md) — Extracts field values from submitted form values.
- [field_default_validate()](field_default_validate.md) — Generic field validation handler.
- [field_default_submit()](field_default_submit.md)
- [field_default_insert()](field_default_insert.md) — Default field 'insert' operation.
- [field_default_prepare_view()](field_default_prepare_view.md) — Invokes hook_field_formatter_prepare_view() on the relevant formatters.
- [field_default_view()](field_default_view.md) — Builds a renderable array for one field on one entity instance.
- [field_default_prepare_translation()](field_default_prepare_translation.md) — Copies source field values into the entity to be prepared.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
