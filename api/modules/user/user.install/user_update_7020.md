# user_update_7020()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 937–971 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L937-L971)
- **Module/theme:** user
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function user_update_7020()
```

## Documentation

```text
Add changed field to users table.
```

## Code

```php
function user_update_7020() {
  // The "changed" column was renamed to "access" in system_update_136(), and
  // the "changed" index on "access" column may persist on old MySQL databases.
  if (db_index_exists('users', 'changed')) {
    if (!db_index_exists('users', 'access')) {
      db_add_index('users', 'access', array('access'));
    }
    db_drop_index('users', 'changed');
  }

  $spec = array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Timestamp for when user was changed.',
  );
  $keys = array(
    'indexes' => array(
      'changed' => array('changed'),
    ),
  );
  // In some cases sites have added the changed field themselves e.g. via a
  // contrib or custom module. Ensure the field uses core's new schema.
  if (db_field_exists('users', 'changed')) {
    db_change_field('users', 'changed', 'changed', $spec, $keys);
  }
  else {
    db_add_field('users', 'changed', $spec, $keys);
    // Set the initial value for existing users.
    db_update('users')
      ->expression('changed', 'created')
      ->execute();
  }

}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
