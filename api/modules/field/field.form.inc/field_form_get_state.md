# field_form_get_state()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 516–519 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L516-L519)
- **Module/theme:** field

## Signature

```php
function field_form_get_state($parents, $field_name, $langcode, &$form_state)
```

## Documentation

```text
Retrieves processing information about a field from $form_state.

@param $parents
  The array of #parents where the field lives in the form.
@param $field_name
  The field name.
@param $langcode
  The language in which the field values are entered.
@param $form_state
  The form state.

@return
  An array with the following key/data pairs:
  - field: the field definition array,
  - instance: the field instance definition array,
  - items_count: the number of widgets to display for the field,
  - array_parents: the location of the field's widgets within the $form
    structure. This entry is populated at '#after_build' time.
  - errors: the array of field validation errors reported on the field. This
    entry is populated at field_attach_form_validate() time.

@see field_form_set_state()
```

## Code

```php
function field_form_get_state($parents, $field_name, $langcode, &$form_state) {
  $form_state_parents = _field_form_state_parents($parents, $field_name, $langcode);
  return drupal_array_get_nested_value($form_state, $form_state_parents);
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
