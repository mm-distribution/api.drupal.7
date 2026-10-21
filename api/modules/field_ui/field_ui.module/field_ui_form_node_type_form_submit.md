# field_ui_form_node_type_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 405–409 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L405-L409)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_form_node_type_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for the 'Save and add fields' button.

@see field_ui_form_node_type_form_alter()
```

## Code

```php
function field_ui_form_node_type_form_submit($form, &$form_state) {
  if ($form_state['triggering_element']['#parents'][0] === 'save_continue') {
    $form_state['redirect'] = _field_ui_bundle_admin_path('node', $form_state['values']['type']) .'/fields';
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
