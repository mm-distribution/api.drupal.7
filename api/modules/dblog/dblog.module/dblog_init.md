# dblog_init()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 89–94 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L89-L94)
- **Module/theme:** dblog
- **Implements:** [hook_init()](../../system/system.api.php/hook_init.md)

## Signature

```php
function dblog_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function dblog_init() {
  if (arg(0) == 'admin' && arg(1) == 'reports') {
    // Add the CSS for this module
    drupal_add_css(drupal_get_path('module', 'dblog') . '/dblog.css');
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
