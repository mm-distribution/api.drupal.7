# user_update_7019()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 927–932 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L927-L932)
- **Module/theme:** user
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function user_update_7019()
```

## Documentation

```text
Ensure there is a combined index on {authmap}.uid and {authmap}.module.
```

## Code

```php
function user_update_7019() {
  // Check first in case it was already added manually.
  if (!db_index_exists('authmap', 'uid_module')) {
    db_add_index('authmap', 'uid_module', array('uid', 'module'));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
