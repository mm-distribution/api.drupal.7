# shortcut_set_delete_access()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 242–254 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L242-L254)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_delete_access($shortcut_set)
```

## Documentation

```text
Access callback for deleting a shortcut set.

@param $shortcut_set
  The shortcut set to be deleted.

@return
  TRUE if the current user has access to delete shortcut sets and this is
  not the site-wide default set; FALSE otherwise.
```

## Code

```php
function shortcut_set_delete_access($shortcut_set) {
  // Only admins can delete sets.
  if (!user_access('administer shortcuts')) {
    return FALSE;
  }

  // Never let the default shortcut set be deleted.
  if ($shortcut_set->set_name == SHORTCUT_DEFAULT_SET_NAME) {
    return FALSE;
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
