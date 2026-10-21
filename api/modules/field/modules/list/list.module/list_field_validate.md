# list_field_validate()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 390–403 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L390-L403)
- **Module/theme:** list
- **Implements:** [hook_field_validate()](../../../field.api.php/hook_field_validate.md)

## Signature

```php
function list_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Implements hook_field_validate().

Possible error codes:
- 'list_illegal_value': The value is not part of the list of allowed values.
```

## Code

```php
function list_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  // Flatten the array before validating to account for optgroups.
  $allowed_values = options_array_flatten(list_allowed_values($field, $instance, $entity_type, $entity));
  foreach ($items as $delta => $item) {
    if (!empty($item['value'])) {
      if (!empty($allowed_values) && !isset($allowed_values[$item['value']])) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'list_illegal_value',
          'message' => t('%name: illegal value.', array('%name' => $instance['label'])),
        );
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
