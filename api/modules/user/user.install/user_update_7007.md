# user_update_7007()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 629–632 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L629-L632)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7007()
```

## Documentation

```text
Add a weight column to user roles.
```

## Code

```php
function user_update_7007() {
  db_add_field('role', 'weight', array('type' => 'int', 'not null' => TRUE, 'default' => 0));
  db_add_index('role', 'name_weight', array('name', 'weight'));
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
