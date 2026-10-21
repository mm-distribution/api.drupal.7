# file_field_insert()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 239–247 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L239-L247)
- **Module/theme:** file
- **Implements:** [hook_field_insert()](../../field/field.api.php/hook_field_insert.md)

## Signature

```php
function file_field_insert($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_insert().
```

## Code

```php
function file_field_insert($entity_type, $entity, $field, $instance, $langcode, &$items) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Add a new usage of each uploaded file.
  foreach ($items as $item) {
    $file = (object) $item;
    file_usage_add($file, 'file', $entity_type, $id);
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
