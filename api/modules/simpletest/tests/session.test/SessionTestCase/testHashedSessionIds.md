# SessionTestCase::testHashedSessionIds()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 252–277 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L252-L277)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHashedSessionIds()
```

## Documentation

```text
Test hashing of session ids in the database.
```

## Code

```php
  function testHashedSessionIds() {
    $user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($user);
    $this->drupalGet('session-test/is-logged-in');
    $this->assertResponse(200, 'User is logged in.');

    $this->drupalGet('session-test/id');
    $matches = array();
    preg_match('/\s*session_id:(.*)\n/', $this->drupalGetContent(), $matches);
    $this->assertTrue(!empty($matches[1]) , 'Found session ID after logging in.');
    $session_id = $matches[1];

    $this->drupalGet('session-test/id-from-cookie');
    $matches = array();
    preg_match('/\s*session_id:(.*)\n/', $this->drupalGetContent(), $matches);
    $this->assertTrue(!empty($matches[1]) , 'Found session ID from cookie.');
    $cookie_session_id = $matches[1];

    $this->assertEqual($session_id, $cookie_session_id, 'Session id and cookie session id are the same.');

    $sql = 'SELECT s.sid FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE u.uid = :uid';
    $db_session = db_query($sql, array(':uid' => $user->uid))->fetchObject();

    $this->assertNotEqual($db_session->sid, $cookie_session_id, 'Session id in the database is not the same as in the session cookie.');
    $this->assertEqual($db_session->sid, drupal_hash_base64($cookie_session_id), 'Session id in the database is the cookie session id hashed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
