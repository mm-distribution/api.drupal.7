# shortcut_set_name()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 571–573 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L571-L573)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_name($number)
```

## Documentation

```text
Returns the name of a shortcut set, based on a provided number.

All shortcut sets have names like "shortcut-set-N" so that they can be
matched with a properly-namespaced entry in the {menu_links} table.

@param $number
  A number representing the shortcut set whose name should be retrieved.

@return
  A string representing the expected shortcut name.
```

## Code

```php
function shortcut_set_name($number) {
  return "shortcut-set-$number";
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
