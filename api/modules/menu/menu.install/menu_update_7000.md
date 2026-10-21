# menu_update_7000()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 80–109 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L80-L109)
- **Module/theme:** menu
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function menu_update_7000()
```

## Documentation

```text
Migrate the "Default menu for content" setting to individual node types.
```

## Code

```php
function menu_update_7000() {
  // Act only on sites originally on Drupal 6 that have a custom "Default menu
  // for content" setting.
  $default_node_menu = variable_get('menu_default_node_menu');
  if (isset($default_node_menu)) {
    // Remove variable no longer used in Drupal 7.
    variable_del('menu_default_node_menu');

    // Make sure the menu chosen as the default still exists.
    $defined_menus = db_query('SELECT * FROM {menu_custom}')->fetchAllAssoc('menu_name', PDO::FETCH_ASSOC);
    // If the menu does not exist, do nothing; nodes will use the default D7
    // node menu settings.
    if (!isset($defined_menus[$default_node_menu])) {
      return;
    }

    // Update the menu settings for each node type.
    foreach (_update_7000_node_get_types() as $type => $type_object) {
      $type_menus = variable_get('menu_options_' . $type);
      // If the site already has a custom menu setting for this node type (set
      // on the initial upgrade to Drupal 7.0), don't override it.
      if (!isset($type_menus)) {
        // Set up this node type so that the Drupal 6 "Default menu for content"
        // is still available in the "Menu settings" section.
        variable_set('menu_options_' . $type, array($default_node_menu));
        variable_set('menu_parent_' . $type, $default_node_menu . ':0');
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
