# UserBlocksUnitTests::insertSession()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2135–2145 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2135-L2145)
- **Class:** [UserBlocksUnitTests](../UserBlocksUnitTests.md)
- **Module/theme:** user

## Signature

```php
private function insertSession(array $fields = array())
```

## Documentation

```text
Insert a user session into the {sessions} table. This function is used
since we cannot log in more than one user at the same time in tests.
```

## Code

```php
  private function insertSession(array $fields = array()) {
    $fields += array(
      'uid' => 0,
      'sid' => drupal_hash_base64(uniqid(mt_rand(), TRUE)),
      'timestamp' => REQUEST_TIME,
    );
    db_insert('sessions')
      ->fields($fields)
      ->execute();
    $this->assertEqual(db_query("SELECT COUNT(*) FROM {sessions} WHERE uid = :uid AND sid = :sid AND timestamp = :timestamp", array(':uid' => $fields['uid'], ':sid' => $fields['sid'], ':timestamp' => $fields['timestamp']))->fetchField(), 1, 'Session record inserted.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
