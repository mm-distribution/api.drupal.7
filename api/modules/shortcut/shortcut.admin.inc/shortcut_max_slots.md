# shortcut_max_slots()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 16–18 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L16-L18)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_max_slots()
```

## Documentation

```text
Returns the maximum number of shortcut "slots" available per shortcut set.

This is used as a limitation in the user interface only.

@return
  The maximum number of shortcuts allowed to be added to a shortcut set.
```

## Code

```php
function shortcut_max_slots() {
  return variable_get('shortcut_max_slots', 7);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
