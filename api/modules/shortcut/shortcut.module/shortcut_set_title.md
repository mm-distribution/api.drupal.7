# shortcut_set_title()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 752–754 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L752-L754)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_title($shortcut_set)
```

## Documentation

```text
Returns the sanitized title of a shortcut set.

Deprecated. This function was previously used as a menu item title callback
but has been replaced by shortcut_set_title_callback() (which does not
sanitize the title, since the menu system does that automatically). In
Drupal 7, use that function for title callbacks, and call check_plain()
directly if you need a sanitized title. In Drupal 8, this function will be
restored as a title callback and therefore will no longer sanitize its
output.

@param $shortcut_set
  An object representing the shortcut set, as returned by
  shortcut_set_load().
```

## Code

```php
function shortcut_set_title($shortcut_set) {
  return check_plain($shortcut_set->title);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
