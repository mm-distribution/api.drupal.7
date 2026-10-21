# shortcut_set_save()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 351–378 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L351-L378)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_save(&$shortcut_set)
```

## Documentation

```text
Saves a shortcut set.

@param $shortcut_set
  An object containing the following properties:
  - 'title': The title of the shortcut set.
  - 'set_name': (optional) The internal name of the shortcut set. If
    omitted, a new shortcut set will be created, and the 'set_name' property
    will be added to the passed-in object.
  - 'links': (optional) An array of menu links to save for the shortcut set.
    Each link is an array containing at least the following keys (which will
    be expanded to fill in other default values after the shortcut set is
    saved):
    - 'link_path': The Drupal path or external path that the link points to.
    - 'link_title': The title of the link.
    Any other keys accepted by menu_link_save() may also be provided.

@return
  A constant which is either SAVED_NEW or SAVED_UPDATED depending on whether
  a new set was created or an existing one was updated.

@see menu_link_save()
```

## Code

```php
function shortcut_set_save(&$shortcut_set) {
  // First save the shortcut set itself.
  if (isset($shortcut_set->set_name)) {
    $return = drupal_write_record('shortcut_set', $shortcut_set, 'set_name');
  }
  else {
    $shortcut_set->set_name = shortcut_set_get_unique_name();
    $return = drupal_write_record('shortcut_set', $shortcut_set);
  }
  // If links were provided for the set, save them.
  if (isset($shortcut_set->links)) {
    foreach ($shortcut_set->links as &$link) {
      // Do not specifically associate these links with the shortcut module,
      // since other modules may make them editable via the menu system.
      // However, we do need to specify the correct menu name.
      $link['menu_name'] = $shortcut_set->set_name;
      $link['plid'] = 0;
      menu_link_save($link);
    }
    // Make sure that we have a return value, since if the links were updated
    // but the shortcut set was not, the call to drupal_write_record() above
    // would not return an indication that anything had changed.
    if (empty($return)) {
      $return = SAVED_UPDATED;
    }
  }
  return $return;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
