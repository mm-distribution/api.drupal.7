# user_update_7005()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 587–605 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L587-L605)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7005(&$sandbox)
```

## Documentation

```text
Changes the users table to allow longer e-mail addresses.
```

## Code

```php
function user_update_7005(&$sandbox) {
  $mail_field = array(
    'type' => 'varchar',
    'length' => 254,
    'not null' => FALSE,
    'default' => '',
    'description' => "User's e-mail address.",
  );
  $init_field = array(
    'type' => 'varchar',
    'length' => 254,
    'not null' => FALSE,
    'default' => '',
    'description' => 'E-mail address used for initial account creation.',
  );
  db_drop_index('users', 'mail');
  db_change_field('users', 'mail', 'mail', $mail_field, array('indexes' => array('mail' => array('mail'))));
  db_change_field('users', 'init', 'init', $init_field);
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
