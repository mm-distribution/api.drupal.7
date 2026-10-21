# file_field_delete()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 312–319 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L312-L319)
- **Module/theme:** file
- **Implements:** [hook_field_delete()](../../field/field.api.php/hook_field_delete.md)

## Signature

```php
function file_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_delete().
```

## Code

```php
function file_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Delete all file usages within this entity.
  foreach ($items as $delta => $item) {
    file_field_delete_file($item, $field, $entity_type, $id, 0);
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
