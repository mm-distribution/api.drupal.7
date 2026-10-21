# shortcut_set_edit_access()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 220–230 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L220-L230)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_edit_access($shortcut_set = NULL)
```

## Documentation

```text
Access callback for editing a shortcut set.

@param object $shortcut_set
  (optional) The shortcut set to be edited. If not set, the current user's
  shortcut set will be used.

@return
  TRUE if the current user has access to edit the shortcut set, FALSE
  otherwise.
```

## Code

```php
function shortcut_set_edit_access($shortcut_set = NULL) {
  // Sufficiently-privileged users can edit their currently displayed shortcut
  // set, but not other sets. Shortcut administrators can edit any set.
  if (user_access('administer shortcuts')) {
    return TRUE;
  }
  if (user_access('customize shortcut links')) {
    return !isset($shortcut_set) || $shortcut_set == shortcut_current_displayed_set();
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
