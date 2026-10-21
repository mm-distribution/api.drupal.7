# drupal_trigger_fatal_error()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1202–1211 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1202-L1211)

## Signature

```php
function drupal_trigger_fatal_error($error_msg)
```

## Documentation

```text
Invoke trigger_error() using a fatal error that will terminate the request.

Normally, Drupal's error handler does not terminate script execution on
user-level errors, even if the error is of type E_USER_ERROR. This function
triggers an error of type E_USER_ERROR that is explicitly forced to be a
fatal error which terminates script execution.

@param string $error_msg
  The error message to trigger. As with trigger_error() itself, this is
  limited to 1024 bytes; additional characters beyond that will be removed.

@see _drupal_error_handler_real()
```

## Code

```php
function drupal_trigger_fatal_error($error_msg) {
  $fatal_error = &drupal_static(__FUNCTION__, FALSE);
  $fatal_error = TRUE;
  trigger_error($error_msg, E_USER_ERROR);
  $fatal_error = FALSE;
  // The standard Drupal error handler should have treated this as a fatal
  // error and already ended the page request. But in case another error
  // handler is being used, terminate execution explicitly here also.
  exit;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
