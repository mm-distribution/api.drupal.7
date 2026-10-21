# menu_help()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 23–43 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L23-L43)
- **Module/theme:** menu
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function menu_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function menu_help($path, $arg) {
  switch ($path) {
    case 'admin/help#menu':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Menu module provides an interface for managing menus. A menu is a hierarchical collection of links, which can be within or external to the site, generally used for navigation. Each menu is rendered in a block that can be enabled and positioned through the <a href="@blocks">Blocks administration page</a>. You can view and manage menus on the <a href="@menus">Menus administration page</a>. For more information, see the online handbook entry for the <a href="@menu">Menu module</a>.', array('@blocks' => url('admin/structure/block'), '@menus' => url('admin/structure/menu'), '@menu' => 'http://drupal.org/documentation/modules/menu/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Managing menus') . '</dt>';
      $output .= '<dd>' . t('Users with the <em>Administer menus and menu items</em> permission can add, edit and delete custom menus on the <a href="@menu">Menus administration page</a>. Custom menus can be special site menus, menus of external links, or any combination of internal and external links. You may create an unlimited number of additional menus, each of which will automatically have an associated block. By selecting <em>list links</em>, you can add, edit, or delete links for a given menu. The links listing page provides a drag-and-drop interface for controlling the order of links, and creating a hierarchy within the menu.', array('@menu' => url('admin/structure/menu'), '@add-menu' => url('admin/structure/menu/add'))) . '</dd>';
      $output .= '<dt>' . t('Displaying menus') . '</dt>';
      $output .= '<dd>' . t('After you have created a menu, you must enable and position the associated block on the <a href="@blocks">Blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/structure/menu/add':
      return '<p>' . t('You can enable the newly-created block for this menu on the <a href="@blocks">Blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</p>';
  }
  if ($path == 'admin/structure/menu' && module_exists('block')) {
    return '<p>' . t('Each menu has a corresponding block that is managed on the <a href="@blocks">Blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
