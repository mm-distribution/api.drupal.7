# SyslogTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/syslog/syslog.test`](../_file.md), lines 12–18 · [local source](../../../../../source/modules/syslog/syslog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.test#L12-L18)
- **Class:** [SyslogTestCase](../SyslogTestCase.md)
- **Module/theme:** syslog

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Syslog functionality',
      'description' => 'Test syslog settings.',
      'group' => 'Syslog'
    );
  }
```

---
_Drupal 7.103 · [modules/syslog/syslog.test](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
