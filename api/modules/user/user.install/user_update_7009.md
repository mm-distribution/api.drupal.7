# user_update_7009()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 648–657 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L648-L657)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7009()
```

## Documentation

```text
Converts fields that store serialized variables from text to blob.
```

## Code

```php
function user_update_7009() {
  $spec = array(
    'type' => 'blob',
    'not null' => FALSE,
    'size' => 'big',
    'serialize' => TRUE,
    'description' => 'A serialized array of name value pairs that are related to the user. Any form values posted during user edit are stored and are loaded into the $user object during user_load(). Use of this field is discouraged and it will likely disappear in a future version of Drupal.',
  );
  db_change_field('users', 'data', 'data', $spec);
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
