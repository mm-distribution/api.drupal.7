# field_form_set_state()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 538–541 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L538-L541)
- **Module/theme:** field

## Signature

```php
function field_form_set_state($parents, $field_name, $langcode, &$form_state, $field_state)
```

## Documentation

```text
Stores processing information about a field in $form_state.

@param $parents
  The array of #parents where the field lives in the form.
@param $field_name
  The field name.
@param $langcode
  The language in which the field values are entered.
@param $form_state
  The form state.
@param $field_state
  The array of data to store. See field_form_get_state() for the structure
  and content of the array.

@see field_form_get_state()
```

## Code

```php
function field_form_set_state($parents, $field_name, $langcode, &$form_state, $field_state) {
  $form_state_parents = _field_form_state_parents($parents, $field_name, $langcode);
  drupal_array_set_nested_value($form_state, $form_state_parents, $field_state);
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
