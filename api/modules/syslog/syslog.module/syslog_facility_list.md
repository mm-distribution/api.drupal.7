# syslog_facility_list()

- **Type:** Function
- **File:** [`modules/syslog/syslog.module`](_file.md), lines 79–90 · [local source](../../../../source/modules/syslog/syslog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module#L79-L90)
- **Module/theme:** syslog

## Signature

```php
function syslog_facility_list()
```

## Documentation

```text
Lists all possible syslog facilities for UNIX/Linux.

@return array
  An array of syslog facilities for UNIX/Linux.
```

## Code

```php
function syslog_facility_list() {
  return array(
    LOG_LOCAL0 => 'LOG_LOCAL0',
    LOG_LOCAL1 => 'LOG_LOCAL1',
    LOG_LOCAL2 => 'LOG_LOCAL2',
    LOG_LOCAL3 => 'LOG_LOCAL3',
    LOG_LOCAL4 => 'LOG_LOCAL4',
    LOG_LOCAL5 => 'LOG_LOCAL5',
    LOG_LOCAL6 => 'LOG_LOCAL6',
    LOG_LOCAL7 => 'LOG_LOCAL7',
  );
}
```

---
_Drupal 7.103 · [modules/syslog/syslog.module](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
