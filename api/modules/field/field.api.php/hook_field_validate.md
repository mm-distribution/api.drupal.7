# hook_field_validate()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 430–441 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L430-L441)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Validate this module's field data.

If there are validation problems, add to the $errors array (passed by
reference). There is no return value.

@param $entity_type
  The type of $entity.
@param $entity
  The entity for the operation.
@param $field
  The field structure for the operation.
@param $instance
  The instance structure for $field on $entity's bundle.
@param $langcode
  The language associated with $items.
@param $items
  $entity->{$field['field_name']}[$langcode], or an empty array if unset.
@param $errors
  The array of errors (keyed by field name, language code, and delta) that
  have already been reported for the entity. The function should add its
  errors to this array. Each error is an associative array with the following
  keys and values:
  - error: An error code (should be a string prefixed with the module name).
  - message: The human readable message to be displayed.
```

## Code

```php
function hook_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  foreach ($items as $delta => $item) {
    if (!empty($item['value'])) {
      if (!empty($field['settings']['max_length']) && drupal_strlen($item['value']) > $field['settings']['max_length']) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'text_max_length',
          'message' => t('%name: the value may not be longer than %max characters.', array('%name' => $instance['label'], '%max' => $field['settings']['max_length'])),
        );
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_validate()".

- [field_test_field_validate()](../tests/field_test.field.inc/field_test_field_validate.md) — `modules/field/tests/field_test.field.inc`
- [list_field_validate()](../modules/list/list.module/list_field_validate.md) — `modules/field/modules/list/list.module`
- [number_field_validate()](../modules/number/number.module/number_field_validate.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_validate()](../../taxonomy/taxonomy.module/taxonomy_field_validate.md) — `modules/taxonomy/taxonomy.module`
- [text_field_validate()](../modules/text/text.module/text_field_validate.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
