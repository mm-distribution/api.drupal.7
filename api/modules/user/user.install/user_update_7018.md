# user_update_7018()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 918–922 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L918-L922)
- **Module/theme:** user
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function user_update_7018()
```

## Documentation

```text
Ensure there is an index on {users}.picture.
```

## Code

```php
function user_update_7018() {
  if (!db_index_exists('users', 'picture')) {
    db_add_index('users', 'picture', array('picture'));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
