# system_admin_compact_page()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2983–2986 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2983-L2986)
- **Module/theme:** system

## Signature

```php
function system_admin_compact_page($mode = 'off')
```

## Documentation

```text
Menu callback; Sets whether the admin menu is in compact mode or not.

@param $mode
  Valid values are 'on' and 'off'.
```

## Code

```php
function system_admin_compact_page($mode = 'off') {
  user_cookie_save(array('admin_compact_mode' => ($mode == 'on')));
  drupal_goto();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
