# shortcut_set_title_exists()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 599–601 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L599-L601)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_title_exists($title)
```

## Documentation

```text
Check to see if a shortcut set with the given title already exists.

@param $title
  Human-readable name of the shortcut set to check.

@return
  TRUE if a shortcut set with that title exists; FALSE otherwise.
```

## Code

```php
function shortcut_set_title_exists($title) {
  return (bool) db_query_range('SELECT 1 FROM {shortcut_set} WHERE title = :title', 0, 1, array(':title' => $title))->fetchField();
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
