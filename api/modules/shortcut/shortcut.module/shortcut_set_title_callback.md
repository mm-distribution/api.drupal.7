# shortcut_set_title_callback()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 765–767 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L765-L767)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_title_callback($shortcut_set)
```

## Documentation

```text
Returns the title of a shortcut set.

Title callback for the editing pages for shortcut sets.

@param $shortcut_set
  An object representing the shortcut set, as returned by
  shortcut_set_load().
```

## Code

```php
function shortcut_set_title_callback($shortcut_set) {
  return $shortcut_set->title;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
