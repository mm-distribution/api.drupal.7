# file_field_update()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 254–307 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L254-L307)
- **Module/theme:** file
- **Implements:** [hook_field_update()](../../field/field.api.php/hook_field_update.md)

## Signature

```php
function file_field_update($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_update().

Checks for files that have been removed from the object.
```

## Code

```php
function file_field_update($entity_type, $entity, $field, $instance, $langcode, &$items) {
  // Check whether the field is defined on the object.
  if (!isset($entity->{$field['field_name']})) {
    // We cannot check for removed files if the field is not defined.
    return;
  }

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // On new revisions, all files are considered to be a new usage and no
  // deletion of previous file usages are necessary.
  if (!empty($entity->revision)) {
    foreach ($items as $item) {
      $file = (object) $item;
      file_usage_add($file, 'file', $entity_type, $id);
    }
    return;
  }

  // Build a display of the current FIDs.
  $current_fids = array();
  foreach ($items as $item) {
    $current_fids[] = $item['fid'];
  }

  // Compare the original field values with the ones that are being saved. Use
  // $entity->original to check this when possible, but if it isn't available,
  // create a bare-bones entity and load its previous values instead.
  if (isset($entity->original)) {
    $original = $entity->original;
  }
  else {
    $original = entity_create_stub_entity($entity_type, array($id, $vid, $bundle));
    field_attach_load($entity_type, array($id => $original), FIELD_LOAD_CURRENT, array('field_id' => $field['id']));
  }
  $original_fids = array();
  if (!empty($original->{$field['field_name']}[$langcode])) {
    foreach ($original->{$field['field_name']}[$langcode] as $original_item) {
      $original_fids[] = $original_item['fid'];
      if (isset($original_item['fid']) && !in_array($original_item['fid'], $current_fids)) {
        // Decrement the file usage count by 1 and delete the file if possible.
        file_field_delete_file($original_item, $field, $entity_type, $id);
      }
    }
  }

  // Add new usage entries for newly added files.
  foreach ($items as $item) {
    if (!in_array($item['fid'], $original_fids)) {
      $file = (object) $item;
      file_usage_add($file, 'file', $entity_type, $id);
    }
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
