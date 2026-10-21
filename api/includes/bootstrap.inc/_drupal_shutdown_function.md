# _drupal_shutdown_function()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3877–3901 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3877-L3901)

## Signature

```php
function _drupal_shutdown_function()
```

## Documentation

```text
Executes registered shutdown functions.
```

## Code

```php
function _drupal_shutdown_function() {
  $callbacks = &drupal_register_shutdown_function();

  // Set the CWD to DRUPAL_ROOT as it is not guaranteed to be the same as it
  // was in the normal context of execution.
  chdir(DRUPAL_ROOT);

  try {
    // Manually iterate over the array instead of using a foreach loop.
    // A foreach operates on a copy of the array, so any shutdown functions that
    // were added from other shutdown functions would never be called.
    while ($callback = current($callbacks)) {
      call_user_func_array($callback['callback'], $callback['arguments']);
      next($callbacks);
    }
  }
  catch (Exception $exception) {
    // If we are displaying errors, then do so with no possibility of a further uncaught exception being thrown.
   require_once DRUPAL_ROOT . '/includes/errors.inc';
   if (error_displayable()) {
      print '<h1>Uncaught exception thrown in shutdown function.</h1>';
      print '<p>' . _drupal_render_exception_safe($exception) . '</p><hr />';
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
