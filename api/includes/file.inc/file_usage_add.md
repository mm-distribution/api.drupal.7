# file_usage_add()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 713–724 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L713-L724)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_usage_add(stdClass $file, $module, $type, $id, $count = 1)
```

## Documentation

```text
Records that a module is using a file.

This usage information will be queried during file_delete() to ensure that
a file is not in use before it is physically removed from disk.

Examples:
- A module that associates files with nodes, so $type would be
  'node' and $id would be the node's nid. Files for all revisions are stored
  within a single nid.
- The User module associates an image with a user, so $type would be 'user'
  and the $id would be the user's uid.

@param $file
  A file object.
@param $module
  The name of the module using the file.
@param $type
  The type of the object that contains the referenced file.
@param $id
  The unique, numeric ID of the object containing the referenced file.
@param $count
  (optional) The number of references to add to the object. Defaults to 1.

@see file_usage_list()
@see file_usage_delete()
```

## Code

```php
function file_usage_add(stdClass $file, $module, $type, $id, $count = 1) {
  db_merge('file_usage')
    ->key(array(
      'fid' => $file->fid,
      'module' => $module,
      'type' => $type,
      'id' => $id,
    ))
    ->fields(array('count' => $count))
    ->expression('count', 'count + :count', array(':count' => $count))
    ->execute();
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
