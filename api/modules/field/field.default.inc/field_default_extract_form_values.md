# field_default_extract_form_values()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 35–44 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L35-L44)
- **Module/theme:** field

## Signature

```php
function field_default_extract_form_values($entity_type, $entity, $field, $instance, $langcode, &$items, $form, &$form_state)
```

## Documentation

```text
Extracts field values from submitted form values.

@param $entity_type
  The type of $entity.
@param $entity
  The entity for the operation.
@param $field
  The field structure for the operation.
@param $instance
  The instance structure for $field on $entity's bundle.
@param $langcode
  The language associated to $items.
@param $items
  The field values. This parameter is altered by reference to receive the
  incoming form values.
@param $form
  The form structure where field elements are attached to. This might be a
  full form structure, or a sub-element of a larger form.
@param $form_state
  The form state.
```

## Code

```php
function field_default_extract_form_values($entity_type, $entity, $field, $instance, $langcode, &$items, $form, &$form_state) {
  $path = array_merge($form['#parents'], array($field['field_name'], $langcode));
  $key_exists = NULL;
  $values = drupal_array_get_nested_value($form_state['values'], $path, $key_exists);
  if ($key_exists) {
    // Remove the 'value' of the 'add more' button.
    unset($values['add_more']);
    $items = $values;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
