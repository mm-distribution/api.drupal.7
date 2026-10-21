# hook_shortcut_default_set()

- **Type:** Hook (documentation function)
- **File:** [`modules/shortcut/shortcut.api.php`](_file.md), lines 33–38 · [local source](../../../../source/modules/shortcut/shortcut.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.api.php#L33-L38)
- **Module/theme:** shortcut
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_shortcut_default_set($account)
```

## Documentation

```text
Return the name of a default shortcut set for the provided user account.

This hook allows modules to define default shortcut sets for a particular
user that differ from the site-wide default (for example, a module may want
to define default shortcuts on a per-role basis).

The default shortcut set is used only when the user does not have any other
shortcut set explicitly assigned to them.

Note that only one default shortcut set can exist per user, so when multiple
modules implement this hook, the last (i.e., highest weighted) module which
returns a valid shortcut set name will prevail.

@param $account
  The user account whose default shortcut set is being requested.
@return
  The name of the shortcut set that this module recommends for that user, if
  there is one.
```

## Code

```php
function hook_shortcut_default_set($account) {
  // Use a special set of default shortcuts for administrators only.
  if (in_array(variable_get('user_admin_role', 0), $account->roles)) {
    return variable_get('mymodule_shortcut_admin_default_set');
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_shortcut_default_set()".

_None found._

---
_Drupal 7.103 · [modules/shortcut/shortcut.api.php](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
