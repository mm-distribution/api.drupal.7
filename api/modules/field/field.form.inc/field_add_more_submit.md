# field_add_more_submit()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 443–458 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L443-L458)
- **Module/theme:** field

## Signature

```php
function field_add_more_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the "Add another item" button of a field form.

This handler is run regardless of whether JS is enabled or not. It makes
changes to the form state. If the button was clicked with JS disabled, then
the page is reloaded with the complete rebuilt form. If the button was
clicked with JS enabled, then ajax_form_callback() calls field_add_more_js()
to return just the changed part of the form.
```

## Code

```php
function field_add_more_submit($form, &$form_state) {
  $button = $form_state['triggering_element'];

  // Go one level up in the form, to the widgets container.
  $element = drupal_array_get_nested_value($form, array_slice($button['#array_parents'], 0, -1));
  $field_name = $element['#field_name'];
  $langcode = $element['#language'];
  $parents = $element['#field_parents'];

  // Increment the items count.
  $field_state = field_form_get_state($parents, $field_name, $langcode, $form_state);
  $field_state['items_count']++;
  field_form_set_state($parents, $field_name, $langcode, $form_state, $field_state);

  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
