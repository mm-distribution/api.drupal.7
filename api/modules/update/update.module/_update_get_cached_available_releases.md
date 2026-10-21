# _update_get_cached_available_releases()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 489–504 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L489-L504)
- **Module/theme:** update

## Signature

```php
function _update_get_cached_available_releases()
```

## Documentation

```text
Returns all currently cached data about available releases for all projects.

@return
  Array of data about available releases, keyed by project shortname.
```

## Code

```php
function _update_get_cached_available_releases() {
  $data = array();
  $cache_items = _update_get_cache_multiple('available_releases');
  foreach ($cache_items as $cid => $cache) {
    $cache->data['last_fetch'] = $cache->created;
    if ($cache->expire < REQUEST_TIME) {
      $cache->data['fetch_status'] = UPDATE_FETCH_PENDING;
    }
    // The project shortname is embedded in the cache ID, even if there's no
    // data for this project in the DB at all, so use that for the indexes in
    // the array.
    $parts = explode('::', $cid, 2);
    $data[$parts[1]] = $cache->data;
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
