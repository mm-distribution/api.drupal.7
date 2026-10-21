# shortcut_set_get_unique_name()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 545–557 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L545-L557)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_get_unique_name()
```

## Documentation

```text
Returns a unique, machine-readable shortcut set name.
```

## Code

```php
function shortcut_set_get_unique_name() {
  // Shortcut sets are numbered sequentially, so we keep trying until we find
  // one that is available. For better performance, we start with a number
  // equal to one more than the current number of shortcut sets, so that if
  // no shortcut sets have been deleted from the database, this will
  // automatically give us the correct one.
  $number = db_query("SELECT COUNT(*) FROM {shortcut_set}")->fetchField() + 1;
  do {
    $name = shortcut_set_name($number);
    $number++;
  } while ($shortcut_set = shortcut_set_load($name));
  return $name;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
