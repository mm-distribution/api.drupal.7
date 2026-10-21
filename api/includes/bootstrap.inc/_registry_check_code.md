# _registry_check_code()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3539–3606 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3539-L3606)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function _registry_check_code($type, $name = NULL)
```

## Documentation

```text
Checks for a resource in the registry.

@param $type
  The type of resource we are looking up, or one of the constants
  REGISTRY_RESET_LOOKUP_CACHE or REGISTRY_WRITE_LOOKUP_CACHE, which
  signal that we should reset or write the cache, respectively.
@param $name
  The name of the resource, or NULL if either of the REGISTRY_* constants
  is passed in.

@return
  TRUE if the resource was found, FALSE if not.
  NULL if either of the REGISTRY_* constants is passed in as $type.
```

## Code

```php
function _registry_check_code($type, $name = NULL) {
  static $lookup_cache, $cache_update_needed;

  if ($type == 'class' && class_exists($name) || $type == 'interface' && interface_exists($name) || $type == 'trait' && trait_exists($name)) {
    return TRUE;
  }

  if (!isset($lookup_cache)) {
    $lookup_cache = array();
    if ($cache = cache_get('lookup_cache', 'cache_bootstrap')) {
      $lookup_cache = $cache->data;
    }
  }

  // When we rebuild the registry, we need to reset this cache so
  // we don't keep lookups for resources that changed during the rebuild.
  if ($type == REGISTRY_RESET_LOOKUP_CACHE) {
    $cache_update_needed = TRUE;
    $lookup_cache = NULL;
    return;
  }

  // Called from drupal_page_footer, we write to permanent storage if there
  // changes to the lookup cache for this request.
  if ($type == REGISTRY_WRITE_LOOKUP_CACHE) {
    if ($cache_update_needed) {
      cache_set('lookup_cache', $lookup_cache, 'cache_bootstrap');
    }
    return;
  }

  // $type is either 'interface' or 'class', so we only need the first letter to
  // keep the cache key unique.
  $cache_key = $type[0] . $name;
  if (isset($lookup_cache[$cache_key])) {
    if ($lookup_cache[$cache_key]) {
      include_once DRUPAL_ROOT . '/' . $lookup_cache[$cache_key];
    }
    return (bool) $lookup_cache[$cache_key];
  }

  // This function may get called when the default database is not active, but
  // there is no reason we'd ever want to not use the default database for
  // this query.
  $file = Database::getConnection('default', 'default')
    ->select('registry', 'r', array('target' => 'default'))
    ->fields('r', array('filename'))
    // Use LIKE here to make the query case-insensitive.
    ->condition('r.name', db_like($name), 'LIKE')
    ->condition('r.type', $type)
    ->execute()
    ->fetchField();

  // Flag that we've run a lookup query and need to update the cache.
  $cache_update_needed = TRUE;

  // Misses are valuable information worth caching, so cache even if
  // $file is FALSE.
  $lookup_cache[$cache_key] = $file;

  if ($file) {
    include_once DRUPAL_ROOT . '/' . $file;
    return TRUE;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
