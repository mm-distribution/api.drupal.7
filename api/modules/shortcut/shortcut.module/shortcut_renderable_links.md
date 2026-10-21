# shortcut_renderable_links()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 635–640 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L635-L640)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_renderable_links($shortcut_set = NULL)
```

## Documentation

```text
Returns an array of shortcut links, suitable for rendering.

@param $shortcut_set
  (optional) An object representing the set whose links will be displayed.
  If not provided, the user's current set will be displayed.
@return
  An array of shortcut links, in the format returned by the menu system.

@see menu_tree()
```

## Code

```php
function shortcut_renderable_links($shortcut_set = NULL) {
  if (!isset($shortcut_set)) {
    $shortcut_set = shortcut_current_displayed_set();
  }
  return menu_tree($shortcut_set->set_name);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
