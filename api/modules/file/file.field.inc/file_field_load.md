# file_field_load()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 170–194 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L170-L194)
- **Module/theme:** file
- **Implements:** [hook_field_load()](../../field/field.api.php/hook_field_load.md)

## Signature

```php
function file_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age)
```

## Documentation

```text
Implements hook_field_load().
```

## Code

```php
function file_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age) {

  $fids = array();
  foreach ($entities as $id => $entity) {
    // Load the files from the files table.
    foreach ($items[$id] as $delta => $item) {
      if (!empty($item['fid'])) {
        $fids[] = $item['fid'];
      }
    }
  }
  $files = file_load_multiple($fids);

  foreach ($entities as $id => $entity) {
    foreach ($items[$id] as $delta => $item) {
      // If the file does not exist, mark the entire item as empty.
      if (empty($item['fid']) || !isset($files[$item['fid']])) {
        unset($items[$id][$delta]);
      }
      else {
        $items[$id][$delta] = array_merge((array) $files[$item['fid']], $item);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
