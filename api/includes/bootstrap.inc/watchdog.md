# watchdog()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2051–2087 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2051-L2087)

## Signature

```php
function watchdog($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = NULL)
```

## Documentation

```text
Logs a system message.

@param $type
  The category to which this message belongs. Can be any string, but the
  general practice is to use the name of the module calling watchdog().
@param $message
  The message to store in the log. Keep $message translatable
  by not concatenating dynamic values into it! Variables in the
  message should be added by using placeholder strings alongside
  the variables argument to declare the value of the placeholders.
  See t() for documentation on how $message and $variables interact.
@param $variables
  Array of variables to replace in the message on display or
  NULL if message is already translated or not possible to
  translate.
@param $severity
  The severity of the message; one of the following values as defined in
  @link http://www.faqs.org/rfcs/rfc3164.html RFC 3164: @endlink
  - WATCHDOG_EMERGENCY: Emergency, system is unusable.
  - WATCHDOG_ALERT: Alert, action must be taken immediately.
  - WATCHDOG_CRITICAL: Critical conditions.
  - WATCHDOG_ERROR: Error conditions.
  - WATCHDOG_WARNING: Warning conditions.
  - WATCHDOG_NOTICE: (default) Normal but significant conditions.
  - WATCHDOG_INFO: Informational messages.
  - WATCHDOG_DEBUG: Debug-level messages.
@param $link
  A link to associate with the message.
  SECURITY NOTE: Make sure your link is properly sanitized.
  Use the l() function to generate secure links.

@see watchdog_severity_levels()
@see hook_watchdog()
```

## Code

```php
function watchdog($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = NULL) {
  global $user, $base_root;

  static $in_error_state = FALSE;

  // It is possible that the error handling will itself trigger an error. In that case, we could
  // end up in an infinite loop. To avoid that, we implement a simple static semaphore.
  if (!$in_error_state && function_exists('module_invoke_all')) {
    $in_error_state = TRUE;

    // The user object may not exist in all conditions, so 0 is substituted if needed.
    $user_uid = isset($user->uid) ? $user->uid : 0;

    // Prepare the fields to be logged
    $log_entry = array(
      'type'        => $type,
      'message'     => $message,
      'variables'   => $variables,
      'severity'    => $severity,
      'link'        => $link,
      'user'        => $user,
      'uid'         => $user_uid,
      'request_uri' => $base_root . request_uri(),
      'referer'     => isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '',
      'ip'          => ip_address(),
      // Request time isn't accurate for long processes, use time() instead.
      'timestamp'   => time(),
    );

    // Call the logging hooks to log/process the message
    module_invoke_all('watchdog', $log_entry);

    // It is critical that the semaphore is only cleared here, in the parent
    // watchdog() call (not outside the loop), to prevent recursive execution.
    $in_error_state = FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
