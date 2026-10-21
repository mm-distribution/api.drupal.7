# dblog_uninstall()

- **Type:** Function
- **File:** [`modules/dblog/dblog.install`](_file.md), lines 98–100 · [local source](../../../../source/modules/dblog/dblog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install#L98-L100)
- **Module/theme:** dblog
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function dblog_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function dblog_uninstall() {
  variable_del('dblog_row_limit');
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.install](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
