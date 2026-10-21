# menu_install()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 46–63 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L46-L63)
- **Module/theme:** menu
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function menu_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function menu_install() {
  $system_menus = menu_list_system_menus();
  $t = get_t();
  $descriptions = array(
    'navigation' => $t('The <em>Navigation</em> menu contains links intended for site visitors. Links are added to the <em>Navigation</em> menu automatically by some modules.'),
    'user-menu' => $t("The <em>User</em> menu contains links related to the user's account, as well as the 'Log out' link."),
    'management' => $t('The <em>Management</em> menu contains links for administrative tasks.'),
    'main-menu' => $t('The <em>Main</em> menu is used on many sites to show the major sections of the site, often in a top navigation bar.'),
  );
  foreach ($system_menus as $menu_name => $title) {
    $menu = array(
      'menu_name' => $menu_name,
      'title' => $t($title),
      'description' => $descriptions[$menu_name],
    );
    menu_save($menu);
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
