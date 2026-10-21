# user_update_7008()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 638–643 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L638-L643)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7008()
```

## Documentation

```text
If 'user_register' variable was unset in Drupal 6, set it to be the same as
the Drupal 6 default setting.
```

## Code

```php
function user_update_7008() {
  if (!isset($GLOBALS['conf']['user_register'])) {
    // Set to the Drupal 6 default, "visitors can create accounts".
    variable_set('user_register', USER_REGISTER_VISITORS);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
