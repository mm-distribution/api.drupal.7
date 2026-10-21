# watchdog_severity_levels()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7785–7796 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7785-L7796)
- **Topics:** [logging_severity_levels](../../topics/logging_severity_levels.md)

## Signature

```php
function watchdog_severity_levels()
```

## Documentation

```text
Returns a list of severity levels, as defined in RFC 3164.

@return
  Array of the possible severity levels for log messages.

@see http://www.ietf.org/rfc/rfc3164.txt
@see watchdog()
@ingroup logging_severity_levels
```

## Code

```php
function watchdog_severity_levels() {
  return array(
    WATCHDOG_EMERGENCY => t('emergency'),
    WATCHDOG_ALERT     => t('alert'),
    WATCHDOG_CRITICAL  => t('critical'),
    WATCHDOG_ERROR     => t('error'),
    WATCHDOG_WARNING   => t('warning'),
    WATCHDOG_NOTICE    => t('notice'),
    WATCHDOG_INFO      => t('info'),
    WATCHDOG_DEBUG     => t('debug'),
  );
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
