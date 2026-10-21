# drupal_page_get_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1359–1374 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1359-L1374)

## Signature

```php
function drupal_page_get_cache($check_only = FALSE)
```

## Documentation

```text
Retrieves the current page from the cache.

Note: we do not serve cached pages to authenticated users, or to anonymous
users when $_SESSION is non-empty. $_SESSION may contain status messages
from a form submission, the contents of a shopping cart, or other user-
specific content that should not be cached and displayed to other users.

@param $check_only
  (optional) Set to TRUE to only return whether a previous call found a
  cache entry.

@return
  The cache object, if the page was found in the cache, NULL otherwise.
```

## Code

```php
function drupal_page_get_cache($check_only = FALSE) {
  global $base_root;
  static $cache_hit = FALSE;

  if ($check_only) {
    return $cache_hit;
  }

  if (drupal_page_is_cacheable()) {
    $cache = cache_get($base_root . request_uri(), 'cache_page');
    if ($cache !== FALSE) {
      $cache_hit = TRUE;
    }
    return $cache;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
