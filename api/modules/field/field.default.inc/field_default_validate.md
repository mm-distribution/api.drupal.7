# field_default_validate()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 74–87 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L74-L87)
- **Module/theme:** field

## Signature

```php
function field_default_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Generic field validation handler.

Possible error codes:
- 'field_cardinality': The number of values exceeds the field cardinality.

@see _hook_field_validate()

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
  $entity->{$field['field_name']}[$langcode], or an empty array if unset.
@param $errors
  The array of errors, keyed by field name and by value delta, that have
  already been reported for the entity. The function should add its errors
  to this array. Each error is an associative array, with the following
  keys and values:
  - 'error': an error code (should be a string, prefixed with the module name)
  - 'message': the human readable message to be displayed.
```

## Code

```php
function field_default_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  // Filter out empty values.
  $items = _field_filter_items($field, $items);

  // Check that the number of values doesn't exceed the field cardinality.
  // For form submitted values, this can only happen with 'multiple value'
  // widgets.
  if ($field['cardinality'] != FIELD_CARDINALITY_UNLIMITED && count($items) > $field['cardinality']) {
    $errors[$field['field_name']][$langcode][0][] = array(
      'error' => 'field_cardinality',
      'message' => t('%name: this field cannot hold more than @count values.', array('%name' => $instance['label'], '@count' => $field['cardinality'])),
    );
  }
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
