# _drupal_decode_exception()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 86–122 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L86-L122)

## Signature

```php
function _drupal_decode_exception($exception)
```

## Documentation

```text
Decodes an exception and retrieves the correct caller.

@param $exception
  The exception object that was thrown.

@return
  An error in the format expected by _drupal_log_error().
```

## Code

```php
function _drupal_decode_exception($exception) {
  $message = $exception->getMessage();

  $backtrace = $exception->getTrace();
  // Add the line throwing the exception to the backtrace.
  array_unshift($backtrace, array('line' => $exception->getLine(), 'file' => $exception->getFile()));

  // For PDOException errors, we try to return the initial caller,
  // skipping internal functions of the database layer.
  if ($exception instanceof PDOException) {
    // The first element in the stack is the call, the second element gives us the caller.
    // We skip calls that occurred in one of the classes of the database layer
    // or in one of its global functions.
    $db_functions = array('db_query',  'db_query_range');
    while (!empty($backtrace[1]) && ($caller = $backtrace[1]) &&
        ((isset($caller['class']) && (strpos($caller['class'], 'Query') !== FALSE || strpos($caller['class'], 'Database') !== FALSE || strpos($caller['class'], 'PDO') !== FALSE)) ||
        in_array($caller['function'], $db_functions))) {
      // We remove that call.
      array_shift($backtrace);
    }
    if (isset($exception->errorInfo['query_string'], $exception->errorInfo['args'])) {
      $message .= ": " . $exception->errorInfo['query_string'] . "; " . print_r($exception->errorInfo['args'], TRUE);
    }
  }
  $caller = _drupal_get_last_caller($backtrace);

  return array(
    '%type' => get_class($exception),
    // The standard PHP exception handler considers that the exception message
    // is plain-text. We mimic this behavior here.
    '!message' => check_plain($message),
    '%function' => $caller['function'],
    '%file' => $caller['file'],
    '%line' => $caller['line'],
    'severity_level' => WATCHDOG_ERROR,
  );
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
