# _update_cache_get()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 803–811 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L803-L811)
- **Module/theme:** update
- **Topics:** [update_status_cache](../../../topics/update_status_cache.md)

## Signature

```php
function _update_cache_get($cid)
```

## Documentation

```text
Retrieves data from the private update status cache table.

@param $cid
  The cache ID to retrieve.

@return
  An array of data for the given cache ID, or NULL if the ID was not found.

@see _update_cache_set()
```

## Code

```php
function _update_cache_get($cid) {
  $cache = db_query("SELECT data, created, expire, serialized FROM {cache_update} WHERE cid = :cid", array(':cid' => $cid))->fetchObject();
  if (isset($cache->data)) {
    if ($cache->serialized) {
      $cache->data = unserialize($cache->data);
    }
  }
  return $cache;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
