# menu_update_7001()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 114–163 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L114-L163)
- **Module/theme:** menu
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function menu_update_7001()
```

## Documentation

```text
Rename "Primary Links" and "Secondary Links" to their Drupal 7 equivalents.
```

## Code

```php
function menu_update_7001() {
  // Migrate D6 menu_primary_links_source to D7 menu_main_links_source (without
  // renaming).
  if (variable_get('menu_primary_links_source') !== NULL) {
    variable_set('menu_main_links_source', variable_get('menu_primary_links_source'));
    variable_del('menu_primary_links_source');
  }

  // Rename each menu, and any settings that refer to the old menu name.
  // - "Primary Links" has become system menu "Main menu".
  // - "Secondary Links" has become a new custom menu "Secondary menu".
  $rename = array(
    'primary-links' => array('main-menu', 'Main menu'),
    'secondary-links' => array('secondary-menu', 'Secondary menu'),
  );
  foreach ($rename as $from_menu => $to) {
    list($to_menu, $to_title) = $to;
    // Rename the menu, and links in the menu.
    db_update('menu_custom')
      ->fields(array('menu_name' => $to_menu, 'title' => $to_title))
      ->condition('menu_name', $from_menu)
      ->execute();
    db_update('menu_links')
      ->fields(array('menu_name' => $to_menu))
      ->condition('menu_name', $from_menu)
      ->execute();

    // Update any content type that used this menu as a default menu.
    // Note: these variables may be unset/default, in which case we leave them
    // alone. See menu_update_7000()
    foreach (_update_7000_node_get_types() as $type => $type_object) {
      $menu_options = variable_get('menu_options_' . $type);
      if ($menu_options !== NULL) {
        variable_set('menu_options_' . $type, str_replace($from_menu, $to_menu, $menu_options));
        if (variable_get('menu_parent_' . $type) == $from_menu . ':0') {
          variable_set('menu_parent_' . $type, $to_menu . ':0');
        }
      }
    }

    // Update the "source for primary links" and "source for secondary links" to
    // follow.
    if (variable_get('menu_main_links_source') == $from_menu) {
      variable_set('menu_main_links_source', $to_menu);
    }
    if (variable_get('menu_secondary_links_source') == $from_menu) {
      variable_set('menu_secondary_links_source', $to_menu);
    }
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
