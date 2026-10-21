# drupal_exit()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2883–2891 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2883-L2891)

## Signature

```php
function drupal_exit($destination = NULL)
```

## Documentation

```text
Performs end-of-request tasks.

In some cases page requests need to end without calling drupal_page_footer().
In these cases, call drupal_exit() instead. There should rarely be a reason
to call exit instead of drupal_exit();

@param $destination
  If this function is called from drupal_goto(), then this argument
  will be a fully-qualified URL that is the destination of the redirect.
  This should be passed along to hook_exit() implementations.
```

## Code

```php
function drupal_exit($destination = NULL) {
  if (drupal_get_bootstrap_phase() == DRUPAL_BOOTSTRAP_FULL) {
    if (!defined('MAINTENANCE_MODE') || MAINTENANCE_MODE != 'update') {
      module_invoke_all('exit', $destination);
    }
    drupal_session_commit();
  }
  exit;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
