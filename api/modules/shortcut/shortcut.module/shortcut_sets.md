# shortcut_sets()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 583–588 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L583-L588)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_sets()
```

## Documentation

```text
Returns an array of all shortcut sets, keyed by the set name.

@return
  An array of shortcut sets. Note that only the basic shortcut set
  properties (name and title) are returned by this function, not the list
  of menu links that belong to the set.
```

## Code

```php
function shortcut_sets() {
  return db_select('shortcut_set', 'ss')
  ->fields('ss')
  ->execute()
  ->fetchAllAssoc('set_name');
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
