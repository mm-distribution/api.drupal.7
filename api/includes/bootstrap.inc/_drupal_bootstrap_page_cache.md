# _drupal_bootstrap_page_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2741–2792 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2741-L2792)

## Signature

```php
function _drupal_bootstrap_page_cache()
```

## Documentation

```text
Attempts to serve a page from the cache.
```

## Code

```php
function _drupal_bootstrap_page_cache() {
  global $user;

  // Allow specifying special cache handlers in settings.php, like
  // using memcached or files for storing cache information.
  require_once DRUPAL_ROOT . '/includes/cache.inc';
  foreach (variable_get('cache_backends', array()) as $include) {
    require_once DRUPAL_ROOT . '/' . $include;
  }
  // Check for a cache mode force from settings.php.
  if (variable_get('page_cache_without_database')) {
    $cache_enabled = TRUE;
  }
  else {
    drupal_bootstrap(DRUPAL_BOOTSTRAP_VARIABLES, FALSE);
    $cache_enabled = variable_get('cache');
  }
  drupal_block_denied(ip_address());
  // If there is no session cookie and cache is enabled (or forced), try
  // to serve a cached page.
  if (!isset($_COOKIE[session_name()]) && $cache_enabled) {
    // Make sure there is a user object because its timestamp will be
    // checked, hook_boot might check for anonymous user etc.
    $user = drupal_anonymous_user();
    // Get the page from the cache.
    $cache = drupal_page_get_cache();
    // If there is a cached page, display it.
    if (is_object($cache)) {
      header('X-Drupal-Cache: HIT');
      // Restore the metadata cached with the page.
      $_GET['q'] = $cache->data['path'];
      drupal_set_title($cache->data['title'], PASS_THROUGH);
      date_default_timezone_set(drupal_get_user_timezone());
      // If the skipping of the bootstrap hooks is not enforced, call
      // hook_boot.
      if (variable_get('page_cache_invoke_hooks', TRUE)) {
        bootstrap_invoke_all('boot');
      }
      drupal_serve_page_from_cache($cache);
      // If the skipping of the bootstrap hooks is not enforced, call
      // hook_exit.
      if (variable_get('page_cache_invoke_hooks', TRUE)) {
        bootstrap_invoke_all('exit');
      }
      // We are done.
      exit;
    }
    else {
      header('X-Drupal-Cache: MISS');
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
