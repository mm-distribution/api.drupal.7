# user_update_7013()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 795–818 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L795-L818)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7013(&$sandbox)
```

## Documentation

```text
Add user module file usage entries.
```

## Code

```php
function user_update_7013(&$sandbox) {
  if (!isset($sandbox['progress'])) {
    // Initialize batch update information.
    $sandbox['progress'] = 0;
    $sandbox['last_uid_processed'] = -1;
    $sandbox['max'] = db_query("SELECT COUNT(*) FROM {users} u WHERE u.picture <> 0")->fetchField();
  }

  // Add usage entries for the user picture files.
  $limit = 500;
  $result = db_query_range('SELECT f.*, u.uid as user_uid FROM {users} u INNER JOIN {file_managed} f ON u.picture = f.fid WHERE u.picture <> 0 AND u.uid > :uid ORDER BY u.uid', 0, $limit, array(':uid' => $sandbox['last_uid_processed']))->fetchAllAssoc('fid', PDO::FETCH_ASSOC);
  foreach ($result as $row) {
    $uid = $row['user_uid'];
    $file = (object) $row;
    file_usage_add($file, 'user', 'user', $uid);

    // Update our progress information for the batch update.
    $sandbox['progress']++;
    $sandbox['last_uid_processed'] = $uid;
  }

  // Indicate our current progress to the batch update system.
  $sandbox['#finished'] = empty($sandbox['max']) || ($sandbox['progress'] / $sandbox['max']);
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
