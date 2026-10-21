# syslog_uninstall()

- **Type:** Function
- **File:** [`modules/syslog/syslog.install`](_file.md), lines 11–15 · [local source](../../../../source/modules/syslog/syslog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.install#L11-L15)
- **Module/theme:** syslog
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function syslog_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function syslog_uninstall() {
  variable_del('syslog_identity');
  variable_del('syslog_facility');
  variable_del('syslog_format');
}
```

---
_Drupal 7.103 · [modules/syslog/syslog.install](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
