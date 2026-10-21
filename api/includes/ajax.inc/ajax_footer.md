# ajax_footer()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 618–631 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L618-L631)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_footer()
```

## Documentation

```text
Performs end-of-Ajax-request tasks.

This function is the equivalent of drupal_page_footer(), but for Ajax
requests.

@see drupal_page_footer()
```

## Code

```php
function ajax_footer() {
  // Even for Ajax requests, invoke hook_exit() implementations. There may be
  // modules that need very fast Ajax responses, and therefore, run Ajax
  // requests with an early bootstrap.
  if (drupal_get_bootstrap_phase() == DRUPAL_BOOTSTRAP_FULL && (!defined('MAINTENANCE_MODE') || MAINTENANCE_MODE != 'update')) {
    module_invoke_all('exit');
  }

  // Commit the user session. See above comment about the possibility of this
  // function running without session.inc loaded.
  if (function_exists('drupal_session_commit')) {
    drupal_session_commit();
  }
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
