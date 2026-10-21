# file_usage_list()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 673–684 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L673-L684)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_usage_list(stdClass $file)
```

## Documentation

```text
Determines where a file is used.

@param $file
  A file object.

@return
  A nested array with usage data. The first level is keyed by module name,
  the second by object type and the third by the object id. The value
  of the third level contains the usage count.

@see file_usage_add()
@see file_usage_delete()
```

## Code

```php
function file_usage_list(stdClass $file) {
  $result = db_select('file_usage', 'f')
    ->fields('f', array('module', 'type', 'id', 'count'))
    ->condition('fid', $file->fid)
    ->condition('count', 0, '>')
    ->execute();
  $references = array();
  foreach ($result as $usage) {
    $references[$usage->module][$usage->type][$usage->id] = $usage->count;
  }
  return $references;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
