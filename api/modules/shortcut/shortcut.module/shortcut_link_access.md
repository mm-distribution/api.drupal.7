# shortcut_link_access()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 293–300 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L293-L300)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_access($menu_link)
```

## Documentation

```text
Access callback for editing a link in a shortcut set.
```

## Code

```php
function shortcut_link_access($menu_link) {
  // The link must belong to a shortcut set that the current user has access
  // to edit.
  if ($shortcut_set = shortcut_set_load($menu_link['menu_name'])) {
    return shortcut_set_edit_access($shortcut_set);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
