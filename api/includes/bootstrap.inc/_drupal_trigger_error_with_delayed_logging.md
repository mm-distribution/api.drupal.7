# _drupal_trigger_error_with_delayed_logging()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1181–1186 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1181-L1186)

## Signature

```php
function _drupal_trigger_error_with_delayed_logging($error_msg, $error_type = E_USER_NOTICE)
```

## Documentation

```text
Invokes trigger_error() with logging delayed until the end of the request.

This is an alternative to PHP's trigger_error() function which can be used
during low-level Drupal core operations that need to avoid being interrupted
by a watchdog() call.

Normally, Drupal's error handler calls watchdog() in response to a
trigger_error() call. However, this invokes hook_watchdog() which can run
arbitrary code. If the trigger_error() happens in the middle of an
operation such as a rebuild operation which should not be interrupted by
arbitrary code, that could potentially break or trigger the rebuild again.
This function protects against that by delaying the watchdog() call until
the end of the current page request.

This is an internal function which should only be called by low-level Drupal
core functions. It may be removed in a future Drupal 7 release.

@param string $error_msg
  The error message to trigger. As with trigger_error() itself, this is
  limited to 1024 bytes; additional characters beyond that will be removed.
@param int $error_type
  (optional) The type of error. This should be one of the E_USER family of
  constants. As with trigger_error() itself, this defaults to E_USER_NOTICE
  if not provided.

@see _drupal_log_error()
```

## Code

```php
function _drupal_trigger_error_with_delayed_logging($error_msg, $error_type = E_USER_NOTICE) {
  $delay_logging = &drupal_static(__FUNCTION__, FALSE);
  $delay_logging = TRUE;
  trigger_error($error_msg, $error_type);
  $delay_logging = FALSE;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
