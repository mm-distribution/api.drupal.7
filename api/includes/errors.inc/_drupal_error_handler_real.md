# _drupal_error_handler_real()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 52–75 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L52-L75)

## Signature

```php
function _drupal_error_handler_real($error_level, $message, $filename, $line)
```

## Documentation

```text
Provides custom PHP error handling.

@param $error_level
  The level of the error raised.
@param $message
  The error message.
@param $filename
  The filename that the error was raised in.
@param $line
  The line number the error was raised at.
```

## Code

```php
function _drupal_error_handler_real($error_level, $message, $filename, $line) {
  if ($error_level & error_reporting()) {
    $types = drupal_error_levels();
    list($severity_msg, $severity_level) = $types[$error_level];
    $caller = _drupal_get_last_caller(debug_backtrace());

    if (!function_exists('filter_xss_admin')) {
      require_once DRUPAL_ROOT . '/includes/common.inc';
    }

    // We treat recoverable errors as fatal, and also allow fatal errors to be
    // explicitly triggered by drupal_trigger_fatal_error().
    _drupal_log_error(array(
      '%type' => isset($types[$error_level]) ? $severity_msg : 'Unknown error',
      // The standard PHP error handler considers that the error messages
      // are HTML. We mimic this behavior here.
      '!message' => filter_xss_admin($message),
      '%function' => $caller['function'],
      '%file' => $caller['file'],
      '%line' => $caller['line'],
      'severity_level' => $severity_level,
    ), $error_level == E_RECOVERABLE_ERROR || drupal_static('drupal_trigger_fatal_error'));
  }
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
