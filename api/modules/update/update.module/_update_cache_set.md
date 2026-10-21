# _update_cache_set()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 773–790 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L773-L790)
- **Module/theme:** update
- **Topics:** [update_status_cache](../../../topics/update_status_cache.md)

## Signature

```php
function _update_cache_set($cid, $data, $expire)
```

## Documentation

```text
Stores data in the private update status cache table.

@param $cid
  The cache ID to save the data with.
@param $data
  The data to store.
@param $expire
  One of the following values:
  - CACHE_PERMANENT: Indicates that the item should never be removed except
    by explicitly using _update_cache_clear().
  - A Unix timestamp: Indicates that the item should be kept at least until
    the given time, after which it will be invalidated.

@see _update_cache_get()
```

## Code

```php
function _update_cache_set($cid, $data, $expire) {
  $fields = array(
    'created' => REQUEST_TIME,
    'expire' => $expire,
  );
  if (!is_string($data)) {
    $fields['data'] = serialize($data);
    $fields['serialized'] = 1;
  }
  else {
    $fields['data'] = $data;
    $fields['serialized'] = 0;
  }
  db_merge('cache_update')
    ->key(array('cid' => $cid))
    ->fields($fields)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
