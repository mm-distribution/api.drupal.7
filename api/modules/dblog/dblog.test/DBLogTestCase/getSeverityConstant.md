# DBLogTestCase::getSeverityConstant()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 658–679 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L658-L679)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog
- **Topics:** [logging_severity_levels](../../../../topics/logging_severity_levels.md)

## Signature

```php
protected function getSeverityConstant($class)
```

## Documentation

```text
Gets the watchdog severity constant corresponding to the CSS class.

@param string $class
  CSS class attribute.

@return int|null
  The watchdog severity constant or NULL if not found.

@ingroup logging_severity_levels
```

## Code

```php
  protected function getSeverityConstant($class) {
    // Reversed array from dblog_overview().
    $map = array(
      'dblog-debug' => WATCHDOG_DEBUG,
      'dblog-info' => WATCHDOG_INFO,
      'dblog-notice' => WATCHDOG_NOTICE,
      'dblog-warning' => WATCHDOG_WARNING,
      'dblog-error' => WATCHDOG_ERROR,
      'dblog-critical' => WATCHDOG_CRITICAL,
      'dblog-alert' => WATCHDOG_ALERT,
      'dblog-emerg' => WATCHDOG_EMERGENCY,
    );

    // Find the class that contains the severity.
    $classes = explode(' ', $class);
    foreach ($classes as $class) {
      if (isset($map[$class])) {
        return $map[$class];
      }
    }
    return NULL;
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
