# user_install()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 303–351 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L303-L351)
- **Module/theme:** user
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function user_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function user_install() {
  // Insert a row for the anonymous user.
  db_insert('users')
    ->fields(array(
      'uid' => 0,
      'name' => '',
      'mail' => '',
    ))
    ->execute();

  // We need some placeholders here as name and mail are uniques and data is
  // presumed to be a serialized array. This will be changed by the settings
  // form in the installer.
  db_insert('users')
    ->fields(array(
      'uid' => 1,
      'name' => 'placeholder-for-uid-1',
      'mail' => 'placeholder-for-uid-1',
      'created' => REQUEST_TIME,
      'changed' => REQUEST_TIME,
      'status' => 1,
      'data' => NULL,
    ))
    ->execute();

  // Built-in roles.
  $rid_anonymous = db_insert('role')
    ->fields(array('name' => 'anonymous user', 'weight' => 0))
    ->execute();
  $rid_authenticated = db_insert('role')
    ->fields(array('name' => 'authenticated user', 'weight' => 1))
    ->execute();

  // Sanity check to ensure the anonymous and authenticated role IDs are the
  // same as the drupal defined constants. In certain situations, this will
  // not be true.
  if ($rid_anonymous != DRUPAL_ANONYMOUS_RID) {
    db_update('role')
      ->fields(array('rid' => DRUPAL_ANONYMOUS_RID))
      ->condition('rid', $rid_anonymous)
      ->execute();
  }
  if ($rid_authenticated != DRUPAL_AUTHENTICATED_RID) {
    db_update('role')
      ->fields(array('rid' => DRUPAL_AUTHENTICATED_RID))
      ->condition('rid', $rid_authenticated)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
