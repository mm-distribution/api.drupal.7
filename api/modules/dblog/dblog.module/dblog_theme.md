# dblog_theme()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 190–197 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L190-L197)
- **Module/theme:** dblog
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function dblog_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function dblog_theme() {
  return array(
    'dblog_message' => array(
      'variables' => array('event' => NULL, 'link' => FALSE),
      'file' => 'dblog.admin.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
