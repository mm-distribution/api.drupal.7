# hook_username_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4384–4389 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4384-L4389)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_username_alter(&$name, $account)
```

## Documentation

```text
Alter the username that is displayed for a user.

Called by format_username() to allow modules to alter the username that's
displayed. Can be used to ensure user privacy in situations where
$account->name is too revealing.

@param $name
  The string that format_username() will return.

@param $account
  The account object passed to format_username().

@see format_username()
```

## Code

```php
function hook_username_alter(&$name, $account) {
  // Display the user's uid instead of name.
  if (isset($account->uid)) {
    $name = t('User !uid', array('!uid' => $account->uid));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_username_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
