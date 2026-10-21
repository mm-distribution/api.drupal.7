# hook_field_delete_revision()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 663–672 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L663-L672)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Define custom revision delete behavior for this module's field types.

This hook is invoked just before the data is deleted from field storage
in field_attach_delete_revision(), and will only be called for fieldable
types that are versioned.

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
function hook_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  foreach ($items as $delta => $item) {
    // For hook_file_references, remember that this file is being deleted.
    $item['file_field_name'] = $field['field_name'];
    if (file_field_delete_file($item, $field, $entity_type, $id)) {
      $items[$delta] = NULL;
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_delete_revision()".

- [file_field_delete_revision()](../../file/file.field.inc/file_field_delete_revision.md) — `modules/file/file.field.inc`
- [image_field_delete_revision()](../../image/image.field.inc/image_field_delete_revision.md) — `modules/image/image.field.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
