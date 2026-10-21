# hook_field_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 462–472 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L462-L472)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Define custom presave behavior for this module's field types.

Make changes or additions to field values by altering the $items parameter by
reference. There is no return value.

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
```

## Code

```php
function hook_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items) {
  if ($field['type'] == 'number_decimal') {
    // Let PHP round the value to ensure consistent behavior across storage
    // backends.
    foreach ($items as $delta => $item) {
      if (isset($item['value'])) {
        $items[$delta]['value'] = round($item['value'], $field['settings']['scale']);
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_presave()".

- [file_field_presave()](../../file/file.field.inc/file_field_presave.md) — `modules/file/file.field.inc`
- [image_field_presave()](../../image/image.field.inc/image_field_presave.md) — `modules/image/image.field.inc`
- [number_field_presave()](../modules/number/number.module/number_field_presave.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_presave()](../../taxonomy/taxonomy.module/taxonomy_field_presave.md) — `modules/taxonomy/taxonomy.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
