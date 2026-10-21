# _drupal_get_last_caller()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 267–293 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L267-L293)

## Signature

```php
function _drupal_get_last_caller($backtrace)
```

## Documentation

```text
Gets the last caller from a backtrace.

@param $backtrace
  A standard PHP backtrace.

@return
  An associative array with keys 'file', 'line' and 'function'.
```

## Code

```php
function _drupal_get_last_caller($backtrace) {
  // Errors that occur inside PHP internal functions do not generate
  // information about file and line. Ignore black listed functions.
  $blacklist = array('debug', '_drupal_error_handler', '_drupal_exception_handler', 'drupal_trigger_fatal_error');
  while (($backtrace && !isset($backtrace[0]['line'])) ||
         (isset($backtrace[1]['function']) && in_array($backtrace[1]['function'], $blacklist))) {
    array_shift($backtrace);
  }

  // The first trace is the call itself.
  // It gives us the line and the file of the last call.
  $call = $backtrace[0];

  // The second call give us the function where the call originated.
  if (isset($backtrace[1])) {
    if (isset($backtrace[1]['class'])) {
      $call['function'] = $backtrace[1]['class'] . $backtrace[1]['type'] . $backtrace[1]['function'] . '()';
    }
    else {
      $call['function'] = $backtrace[1]['function'] . '()';
    }
  }
  else {
    $call['function'] = 'main()';
  }
  return $call;
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
