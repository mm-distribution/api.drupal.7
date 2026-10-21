# shortcut_valid_link()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 614–622 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L614-L622)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_valid_link($path)
```

## Documentation

```text
Determines if a path corresponds to a valid shortcut link.

@param $path
  The path to the link.
@return
  TRUE if the shortcut link is valid, FALSE otherwise. Valid links are ones
  that correspond to actual paths on the site.

@see menu_edit_item_validate()
```

## Code

```php
function shortcut_valid_link($path) {
  // Do not use URL aliases.
  $normal_path = drupal_get_normal_path($path);
  if ($path != $normal_path) {
    $path = $normal_path;
  }
  // An empty path is valid too and will be converted to <front>.
  return (!url_is_external($path) && menu_get_item($path)) || empty($path) || $path == '<front>';
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
