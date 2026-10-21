# shortcut_set_load()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 315–326 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L315-L326)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_load($set_name)
```

## Documentation

```text
Loads the data for a shortcut set.

@param $set_name
  The name of the shortcut set to load.

@return object
  If the shortcut set exists, an object containing the following properties:
  - 'set_name': The internal name of the shortcut set.
  - 'title': The title of the shortcut set.
  - 'links': An array of links associated with this shortcut set.
  If the shortcut set does not exist, the function returns FALSE.
```

## Code

```php
function shortcut_set_load($set_name) {
  $set = db_select('shortcut_set', 'ss')
  ->fields('ss')
  ->condition('set_name', $set_name)
  ->execute()
  ->fetchObject();
  if (!$set) {
    return FALSE;
  }
  $set->links = menu_load_links($set_name);
  return $set;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
