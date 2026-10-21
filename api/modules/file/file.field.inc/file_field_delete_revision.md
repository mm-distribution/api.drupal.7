# file_field_delete_revision()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 324–332 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L324-L332)
- **Module/theme:** file
- **Implements:** [hook_field_delete_revision()](../../field/field.api.php/hook_field_delete_revision.md)

## Signature

```php
function file_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_delete_revision().
```

## Code

```php
function file_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  foreach ($items as $delta => $item) {
    // Decrement the file usage count by 1 and delete the file if possible.
    if (file_field_delete_file($item, $field, $entity_type, $id)) {
      $items[$delta] = NULL;
    }
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
