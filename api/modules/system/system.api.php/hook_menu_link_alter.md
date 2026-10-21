# hook_menu_link_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1305–1320 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1305-L1320)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_link_alter(&$item)
```

## Documentation

```text
Alter the data being saved to the {menu_links} table by menu_link_save().

@param $item
  Associative array defining a menu link as passed into menu_link_save().

@see hook_translated_menu_link_alter()
```

## Code

```php
function hook_menu_link_alter(&$item) {
  // Make all new admin links hidden (a.k.a disabled).
  if (strpos($item['link_path'], 'admin') === 0 && empty($item['mlid'])) {
    $item['hidden'] = 1;
  }
  // Flag a link to be altered by hook_translated_menu_link_alter().
  if ($item['link_path'] == 'devel/cache/clear') {
    $item['options']['alter'] = TRUE;
  }
  // Flag a link to be altered by hook_translated_menu_link_alter(), but only
  // if it is derived from a menu router item; i.e., do not alter a custom
  // menu link pointing to the same path that has been created by a user.
  if ($item['link_path'] == 'user' && $item['module'] == 'system') {
    $item['options']['alter'] = TRUE;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_link_alter()".

- [user_menu_link_alter()](../../user/user.module/user_menu_link_alter.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
