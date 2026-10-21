# drupal_page_footer()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2849–2869 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2849-L2869)

## Signature

```php
function drupal_page_footer()
```

## Documentation

```text
Performs end-of-request tasks.

This function sets the page cache if appropriate, and allows modules to
react to the closing of the page by calling hook_exit().
```

## Code

```php
function drupal_page_footer() {
  global $user;

  module_invoke_all('exit');

  // Commit the user session, if needed.
  drupal_session_commit();

  if (variable_get('cache', 0) && ($cache = drupal_page_set_cache())) {
    drupal_serve_page_from_cache($cache);
  }
  else {
    ob_flush();
  }

  _registry_check_code(REGISTRY_WRITE_LOOKUP_CACHE);
  drupal_cache_system_paths();
  module_implements_write_cache();
  drupal_file_scan_write_cache();
  system_run_automated_cron();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
