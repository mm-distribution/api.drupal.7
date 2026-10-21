# menu_configure()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 690–720 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L690-L720)
- **Module/theme:** menu

## Signature

```php
function menu_configure()
```

## Documentation

```text
Menu callback; Build the form presenting menu configuration options.
```

## Code

```php
function menu_configure() {
  $form['intro'] = array(
    '#type' => 'item',
    '#markup' => t('The menu module allows on-the-fly creation of menu links in the content authoring forms. To configure these settings for a particular content type, visit the <a href="@content-types">Content types</a> page, click the <em>edit</em> link for the content type, and go to the <em>Menu settings</em> section.', array('@content-types' => url('admin/structure/types'))),
  );

  $menu_options = menu_get_menus();

  $main = variable_get('menu_main_links_source', 'main-menu');
  $form['menu_main_links_source'] = array(
    '#type' => 'select',
    '#title' => t('Source for the Main links'),
    '#default_value' => variable_get('menu_main_links_source', 'main-menu'),
    '#empty_option' => t('No Main links'),
    '#options' => $menu_options,
    '#tree' => FALSE,
    '#description' => t('Select what should be displayed as the Main links (typically at the top of the page).'),
  );

  $form['menu_secondary_links_source'] = array(
    '#type' => 'select',
    '#title' => t('Source for the Secondary links'),
    '#default_value' => variable_get('menu_secondary_links_source', 'user-menu'),
    '#empty_option' => t('No Secondary links'),
    '#options' => $menu_options,
    '#tree' => FALSE,
    '#description' => t('Select the source for the Secondary links. An advanced option allows you to use the same source for both Main links (currently %main) and Secondary links: if your source menu has two levels of hierarchy, the top level menu links will appear in the Main links, and the children of the active link will appear in the Secondary links.', array('%main' => $main ? $menu_options[$main] : t('none'))),
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
