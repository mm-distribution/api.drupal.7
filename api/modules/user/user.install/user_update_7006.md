# user_update_7006()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 610–624 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L610-L624)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7006(&$sandbox)
```

## Documentation

```text
Add module data to {role_permission}.
```

## Code

```php
function user_update_7006(&$sandbox) {
  $module_field = array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'description' => "The module declaring the permission.",
  );
  // Check that the field hasn't been updated in an aborted run of this
  // update.
  if (!db_field_exists('role_permission', 'module')) {
    // Add a new field for the fid.
    db_add_field('role_permission', 'module', $module_field);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
