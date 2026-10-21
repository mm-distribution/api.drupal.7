# file_field_presave()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 215–234 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L215-L234)
- **Module/theme:** file
- **Implements:** [hook_field_presave()](../../field/field.api.php/hook_field_presave.md)

## Signature

```php
function file_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_presave().
```

## Code

```php
function file_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items) {
  // Make sure that each file which will be saved with this object has a
  // permanent status, so that it will not be removed when temporary files are
  // cleaned up.
  foreach ($items as $delta => $item) {
    if (empty($item['fid'])) {
      unset($items[$delta]);
      continue;
    }
    $file = file_load($item['fid']);
    if (empty($file)) {
      unset($items[$delta]);
      continue;
    }
    if (!$file->status) {
      $file->status = FILE_STATUS_PERMANENT;
      file_save($file);
    }
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
