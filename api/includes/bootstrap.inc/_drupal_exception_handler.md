# _drupal_exception_handler()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2686–2706 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2686-L2706)

## Signature

```php
function _drupal_exception_handler($exception)
```

## Documentation

```text
Provides custom PHP exception handling.

Uncaught exceptions are those not enclosed in a try/catch block. They are
always fatal: the execution of the script will stop as soon as the exception
handler exits.

@param $exception
  The exception object that was thrown.
```

## Code

```php
function _drupal_exception_handler($exception) {
  require_once DRUPAL_ROOT . '/includes/errors.inc';

  try {
    // Log the message to the watchdog and return an error page to the user.
    _drupal_log_error(_drupal_decode_exception($exception), TRUE);
  }
  catch (Exception $exception2) {
    // Add a 500 status code in case an exception was thrown before the 500
    // status could be set (e.g. while loading a maintenance theme from cache).
    drupal_add_http_header('Status', '500 Internal Server Error');

    // Another uncaught exception was thrown while handling the first one.
    // If we are displaying errors, then do so with no possibility of a further uncaught exception being thrown.
    if (error_displayable()) {
      print '<h1>Additional uncaught exception thrown while handling exception.</h1>';
      print '<h2>Original</h2><p>' . _drupal_render_exception_safe($exception) . '</p>';
      print '<h2>Additional</h2><p>' . _drupal_render_exception_safe($exception2) . '</p><hr />';
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
