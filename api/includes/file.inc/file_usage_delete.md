# file_usage_delete()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 751–779 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L751-L779)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_usage_delete(stdClass $file, $module, $type = NULL, $id = NULL, $count = 1)
```

## Documentation

```text
Removes a record to indicate that a module is no longer using a file.

The file_delete() function is typically called after removing a file usage
to remove the record from the file_managed table and delete the file itself.

@param $file
  A file object.
@param $module
  The name of the module using the file.
@param $type
  (optional) The type of the object that contains the referenced file. May
  be omitted if all module references to a file are being deleted.
@param $id
  (optional) The unique, numeric ID of the object containing the referenced
  file. May be omitted if all module references to a file are being deleted.
@param $count
  (optional) The number of references to delete from the object. Defaults to
  1. 0 may be specified to delete all references to the file within a
  specific object.

@see file_usage_add()
@see file_usage_list()
@see file_delete()
```

## Code

```php
function file_usage_delete(stdClass $file, $module, $type = NULL, $id = NULL, $count = 1) {
  // Delete rows that have a exact or less value to prevent empty rows.
  $query = db_delete('file_usage')
    ->condition('module', $module)
    ->condition('fid', $file->fid);
  if ($type && $id) {
    $query
      ->condition('type', $type)
      ->condition('id', $id);
  }
  if ($count) {
    $query->condition('count', $count, '<=');
  }
  $result = $query->execute();

  // If the row has more than the specified count decrement it by that number.
  if (!$result && $count > 0) {
    $query = db_update('file_usage')
      ->condition('module', $module)
      ->condition('fid', $file->fid);
    if ($type && $id) {
      $query
        ->condition('type', $type)
        ->condition('id', $id);
    }
    $query->expression('count', 'count - :count', array(':count' => $count));
    $query->execute();
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
