# _update_get_cache_multiple()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 822–837 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L822-L837)
- **Module/theme:** update
- **Topics:** [update_status_cache](../../../topics/update_status_cache.md)

## Signature

```php
function _update_get_cache_multiple($cid_prefix)
```

## Documentation

```text
Returns an array of cache items with a given cache ID prefix.

@param string $cid_prefix
  The cache ID prefix.

@return
  Associative array of cache items, keyed by cache ID.
```

## Code

```php
function _update_get_cache_multiple($cid_prefix) {
  $data = array();
  $result = db_select('cache_update')
    ->fields('cache_update', array('cid', 'data', 'created', 'expire', 'serialized'))
    ->condition('cache_update.cid', $cid_prefix . '::%', 'LIKE')
    ->execute();
  foreach ($result as $cache) {
    if ($cache) {
      if ($cache->serialized) {
        $cache->data = unserialize($cache->data);
      }
      $data[$cache->cid] = $cache;
    }
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
