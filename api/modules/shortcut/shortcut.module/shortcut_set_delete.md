# shortcut_set_delete()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 391–412 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L391-L412)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_delete($shortcut_set)
```

## Documentation

```text
Deletes a shortcut set.

Note that the default set cannot be deleted.

@param $shortcut_set
  An object representing the shortcut set to delete.

@return
  TRUE if the set was deleted, FALSE otherwise.
```

## Code

```php
function shortcut_set_delete($shortcut_set) {
  // Don't allow deletion of the system default shortcut set.
  if ($shortcut_set->set_name == SHORTCUT_DEFAULT_SET_NAME) {
    return FALSE;
  }

  // First, delete any user assignments for this set, so that each of these
  // users will go back to using whatever default set applies.
  db_delete('shortcut_set_users')
    ->condition('set_name', $shortcut_set->set_name)
    ->execute();

  // Next, delete the menu links for this set.
  menu_delete_links($shortcut_set->set_name);

  // Finally, delete the set itself.
  $deleted = db_delete('shortcut_set')
    ->condition('set_name', $shortcut_set->set_name)
    ->execute();

  return (bool) $deleted;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
