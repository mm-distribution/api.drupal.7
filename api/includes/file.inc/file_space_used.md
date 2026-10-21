# file_space_used()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1438–1446 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1438-L1446)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_space_used($uid = NULL, $status = FILE_STATUS_PERMANENT)
```

## Documentation

```text
Determines total disk space used by a single user or the whole filesystem.

@param $uid
  Optional. A user id, specifying NULL returns the total space used by all
  non-temporary files.
@param $status
  Optional. The file status to consider. The default is to only
  consider files in status FILE_STATUS_PERMANENT.

@return
  An integer containing the number of bytes used.
```

## Code

```php
function file_space_used($uid = NULL, $status = FILE_STATUS_PERMANENT) {
  $query = db_select('file_managed', 'f');
  $query->condition('f.status', $status);
  $query->addExpression('SUM(f.filesize)', 'filesize');
  if (isset($uid)) {
    $query->condition('f.uid', $uid);
  }
  return $query->execute()->fetchField();
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
