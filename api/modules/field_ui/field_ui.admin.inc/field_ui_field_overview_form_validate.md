# field_ui_field_overview_form_validate()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 661–664 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L661-L664)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_overview_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for field_ui_field_overview_form().

@see field_ui_field_overview_form_submit()
```

## Code

```php
function field_ui_field_overview_form_validate($form, &$form_state) {
  _field_ui_field_overview_form_validate_add_new($form, $form_state);
  _field_ui_field_overview_form_validate_add_existing($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
