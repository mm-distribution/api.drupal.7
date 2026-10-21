# SessionTestCase::testSessionWrite()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 186–223 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L186-L223)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSessionWrite()
```

## Documentation

```text
Test that sessions are only saved when necessary.
```

## Code

```php
  function testSessionWrite() {
    $user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($user);

    $sql = 'SELECT u.access, s.timestamp FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE u.uid = :uid';
    $times1 = db_query($sql, array(':uid' => $user->uid))->fetchObject();

    // Before every request we sleep one second to make sure that if the session
    // is saved, its timestamp will change.

    // Modify the session.
    sleep(1);
    $this->drupalGet('session-test/set/foo');
    $times2 = db_query($sql, array(':uid' => $user->uid))->fetchObject();
    $this->assertEqual($times2->access, $times1->access, 'Users table was not updated.');
    $this->assertNotEqual($times2->timestamp, $times1->timestamp, 'Sessions table was updated.');

    // Write the same value again, i.e. do not modify the session.
    sleep(1);
    $this->drupalGet('session-test/set/foo');
    $times3 = db_query($sql, array(':uid' => $user->uid))->fetchObject();
    $this->assertEqual($times3->access, $times1->access, 'Users table was not updated.');
    $this->assertEqual($times3->timestamp, $times2->timestamp, 'Sessions table was not updated.');

    // Do not change the session.
    sleep(1);
    $this->drupalGet('');
    $times4 = db_query($sql, array(':uid' => $user->uid))->fetchObject();
    $this->assertEqual($times4->access, $times3->access, 'Users table was not updated.');
    $this->assertEqual($times4->timestamp, $times3->timestamp, 'Sessions table was not updated.');

    // Force updating of users and sessions table once per second.
    variable_set('session_write_interval', 0);
    $this->drupalGet('');
    $times5 = db_query($sql, array(':uid' => $user->uid))->fetchObject();
    $this->assertNotEqual($times5->access, $times4->access, 'Users table was updated.');
    $this->assertNotEqual($times5->timestamp, $times4->timestamp, 'Sessions table was updated.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
