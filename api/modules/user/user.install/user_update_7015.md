# user_update_7015()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 837–844 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L837-L844)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7015()
```

## Documentation

```text
Change {users}.signature_format into varchar.
```

## Code

```php
function user_update_7015() {
  db_change_field('users', 'signature_format', 'signature_format', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the signature.',
  ));
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
