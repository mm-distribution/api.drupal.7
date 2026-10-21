# file_field_delete_file()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 357–371 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L357-L371)
- **Module/theme:** file

## Signature

```php
function file_field_delete_file($item, $field, $entity_type, $id, $count = 1)
```

## Documentation

```text
Decrements the usage count for a file and attempts to delete it.

This function only has an effect if the file being deleted is used only by
File module.

@param $item
  The field item that contains a file array.
@param $field
  The field structure for the operation.
@param $entity_type
  The type of $entity.
@param $id
  The entity ID which contains the file being deleted.
@param $count
  (optional) The number of references to decrement from the object
  containing the file. Defaults to 1.

@return
  Boolean TRUE if the file was deleted, or an array of remaining references
  if the file is still in use by other modules. Boolean FALSE if an error
  was encountered.
```

## Code

```php
function file_field_delete_file($item, $field, $entity_type, $id, $count = 1) {
  // To prevent the file field from deleting files it doesn't know about, check
  // the file reference count. Temporary files can be deleted because they
  // are not yet associated with any content at all.
  $file = (object) $item;
  $file_usage = file_usage_list($file);
  if ($file->status == 0 || !empty($file_usage['file'])) {
    file_usage_delete($file, 'file', $entity_type, $id, $count);
    return file_delete($file);
  }

  // Even if the file is not deleted, return TRUE to indicate the file field
  // record can be removed from the field database tables.
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
