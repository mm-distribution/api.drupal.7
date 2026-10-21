# file_load_multiple()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 591–593 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L591-L593)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_load_multiple($fids = array(), $conditions = array())
```

## Documentation

```text
Loads file objects from the database.

@param $fids
  An array of file IDs.
@param $conditions
  (deprecated) An associative array of conditions on the {file_managed}
  table, where the keys are the database fields and the values are the
  values those fields must have. Instead, it is preferable to use
  EntityFieldQuery to retrieve a list of entity IDs loadable by
  this function.

@return
  An array of file objects, indexed by fid.

@todo Remove $conditions in Drupal 8.

@see hook_file_load()
@see file_load()
@see entity_load()
@see EntityFieldQuery
```

## Code

```php
function file_load_multiple($fids = array(), $conditions = array()) {
  return entity_load('file', $fids, $conditions);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
