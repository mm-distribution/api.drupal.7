# user_update_7000()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 428–471 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L428-L471)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7000(&$sandbox)
```

## Documentation

```text
Increase the length of the password field to accommodate better hashes.

Also re-hashes all current passwords to improve security. This may be a
lengthy process, and is performed batch-wise.
```

## Code

```php
function user_update_7000(&$sandbox) {
  $sandbox['#finished'] = 0;
  // Lower than DRUPAL_HASH_COUNT to make the update run at a reasonable speed.
  $hash_count_log2 = 11;
  // Multi-part update.
  if (!isset($sandbox['user_from'])) {
    db_change_field('users', 'pass', 'pass', array('type' => 'varchar', 'length' => 128, 'not null' => TRUE, 'default' => ''));
    $sandbox['user_from'] = 0;
    $sandbox['user_count'] = db_query("SELECT COUNT(uid) FROM {users}")->fetchField();
  }
  else {
    require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
    //  Hash again all current hashed passwords.
    $has_rows = FALSE;
    // Update this many per page load.
    $count = 1000;
    $result = db_query_range("SELECT uid, pass FROM {users} WHERE uid > 0 ORDER BY uid", $sandbox['user_from'], $count);
    foreach ($result as $account) {
      $has_rows = TRUE;

      // If the $account->pass value is not a MD5 hash (a 32 character
      // hexadecimal string) then skip it.
      if (!preg_match('/^[0-9a-f]{32}$/', $account->pass)) {
        continue;
      }

      $new_hash = user_hash_password($account->pass, $hash_count_log2);
      if ($new_hash) {
        // Indicate an updated password.
        $new_hash  = 'U' . $new_hash;
        db_update('users')
          ->fields(array('pass' => $new_hash))
          ->condition('uid', $account->uid)
          ->execute();
      }
    }
    $sandbox['#finished'] = $sandbox['user_from']/$sandbox['user_count'];
    $sandbox['user_from'] += $count;
    if (!$has_rows) {
      $sandbox['#finished'] = 1;
      return t('User passwords rehashed to improve security');
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
