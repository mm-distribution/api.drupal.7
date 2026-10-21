# shortcut_default_set()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 521–540 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L521-L540)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_default_set($account = NULL)
```

## Documentation

```text
Returns the default shortcut set for a given user account.

@param object $account
  (optional) The user account whose default shortcut set will be returned.
  If not provided, the function will return the currently logged-in user's
  default shortcut set.

@return
  An object representing the default shortcut set.
```

## Code

```php
function shortcut_default_set($account = NULL) {
  global $user;
  if (!isset($account)) {
    $account = $user;
  }

  // Allow modules to return a default shortcut set name. Since we can only
  // have one, we allow the last module which returns a valid result to take
  // precedence. If no module returns a valid set, fall back on the site-wide
  // default, which is the lowest-numbered shortcut set.
  $suggestions = array_reverse(module_invoke_all('shortcut_default_set', $account));
  $suggestions[] = SHORTCUT_DEFAULT_SET_NAME;
  foreach ($suggestions as $name) {
    if ($shortcut_set = shortcut_set_load($name)) {
      break;
    }
  }

  return $shortcut_set;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
