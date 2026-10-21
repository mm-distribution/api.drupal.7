# user_update_7016()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 858–866 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L858-L866)
- **Module/theme:** user
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function user_update_7016()
```

## Documentation

```text
Update the database to match the schema.
```

## Code

```php
function user_update_7016() {
  // Add field default.
  db_change_field('users', 'uid', 'uid', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => TRUE,
    'default' => 0,
  ));
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
