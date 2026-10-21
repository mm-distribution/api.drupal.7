# drupal_error_levels()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 16–38 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L16-L38)
- **Topics:** [logging_severity_levels](../../topics/logging_severity_levels.md)

## Signature

```php
function drupal_error_levels()
```

## Documentation

```text
Maps PHP error constants to watchdog severity levels.

The error constants are documented at
http://php.net/manual/errorfunc.constants.php

@ingroup logging_severity_levels
```

## Code

```php
function drupal_error_levels() {
  $types = array(
    E_ERROR => array('Error', WATCHDOG_ERROR),
    E_WARNING => array('Warning', WATCHDOG_WARNING),
    E_PARSE => array('Parse error', WATCHDOG_ERROR),
    E_NOTICE => array('Notice', WATCHDOG_NOTICE),
    E_CORE_ERROR => array('Core error', WATCHDOG_ERROR),
    E_CORE_WARNING => array('Core warning', WATCHDOG_WARNING),
    E_COMPILE_ERROR => array('Compile error', WATCHDOG_ERROR),
    E_COMPILE_WARNING => array('Compile warning', WATCHDOG_WARNING),
    E_USER_ERROR => array('User error', WATCHDOG_ERROR),
    E_USER_WARNING => array('User warning', WATCHDOG_WARNING),
    E_USER_NOTICE => array('User notice', WATCHDOG_NOTICE),
    E_STRICT => array('Strict warning', WATCHDOG_DEBUG),
    E_RECOVERABLE_ERROR => array('Recoverable fatal error', WATCHDOG_ERROR),
  );
  // E_DEPRECATED and E_USER_DEPRECATED were added in PHP 5.3.0.
  if (defined('E_DEPRECATED')) {
    $types[E_DEPRECATED] = array('Deprecated function', WATCHDOG_DEBUG);
    $types[E_USER_DEPRECATED] = array('User deprecated function', WATCHDOG_DEBUG);
  }
  return $types;
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
