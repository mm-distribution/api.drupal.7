# _field_form_state_parents()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 546–565 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L546-L565)
- **Module/theme:** field

## Signature

```php
function _field_form_state_parents($parents, $field_name, $langcode)
```

## Documentation

```text
Returns the location of processing information within $form_state.
```

## Code

```php
function _field_form_state_parents($parents, $field_name, $langcode) {
  // To ensure backwards compatibility on regular entity forms for widgets that
  // still access $form_state['field'][$field_name] directly,
  // - top-level fields (empty $parents) are placed directly under
  //   $form_state['fields'][$field_name].
  // - Other fields are placed under
  //   $form_state['field']['#parents'][...$parents...]['#fields'][$field_name]
  //   to avoid clashes between field names and $parents parts.
  // @todo Remove backwards compatibility in Drupal 8, and use a unique
  // $form_state['field'][...$parents...]['#fields'][$field_name] structure.
  if (!empty($parents)) {
    $form_state_parents = array_merge(array('#parents'), $parents, array('#fields'));
  }
  else {
    $form_state_parents = array();
  }
  $form_state_parents = array_merge(array('field'), $form_state_parents, array($field_name, $langcode));

  return $form_state_parents;
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
