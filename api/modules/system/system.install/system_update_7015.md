# system_update_7015()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2173–2195 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2173-L2195)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7015()
```

## Documentation

```text
Change the user logout path.
```

## Code

```php
function system_update_7015() {
  db_update('menu_links')
    ->fields(array('link_path' => 'user/logout'))
    ->condition('link_path', 'logout')
    ->execute();
  db_update('menu_links')
    ->fields(array('router_path' => 'user/logout'))
    ->condition('router_path', 'logout')
    ->execute();

  db_update('menu_links')
    ->fields(array(
      'menu_name' => 'user-menu',
      'plid' => 0,
    ))
    ->condition(db_or()
      ->condition('link_path', 'user/logout')
      ->condition('router_path', 'user/logout')
    )
    ->condition('module', 'system')
    ->condition('customized', 0)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
