# SessionTestCase::testDataPersistence()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 75–131 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L75-L131)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDataPersistence()
```

## Documentation

```text
Test data persistence via the session_test module callbacks.
```

## Code

```php
  function testDataPersistence() {
    $user = $this->drupalCreateUser(array('access content'));
    // Enable sessions.
    $this->sessionReset($user->uid);

    $this->drupalLogin($user);

    $value_1 = $this->randomName();
    $this->drupalGet('session-test/set/' . $value_1);
    $this->assertText($value_1, 'The session value was stored.', 'Session');
    $this->drupalGet('session-test/get');
    $this->assertText($value_1, 'Session correctly returned the stored data for an authenticated user.', 'Session');

    // Attempt to write over val_1. If drupal_save_session(FALSE) is working.
    // properly, val_1 will still be set.
    $value_2 = $this->randomName();
    $this->drupalGet('session-test/no-set/' . $value_2);
    $this->assertText($value_2, 'The session value was correctly passed to session-test/no-set.', 'Session');
    $this->drupalGet('session-test/get');
    $this->assertText($value_1, 'Session data is not saved for drupal_save_session(FALSE).', 'Session');

    // Switch browser cookie to anonymous user, then back to user 1.
    $this->sessionReset();
    $this->sessionReset($user->uid);
    $this->assertText($value_1, 'Session data persists through browser close.', 'Session');

    // Logout the user and make sure the stored value no longer persists.
    $this->drupalLogout();
    $this->sessionReset();
    $this->drupalGet('session-test/get');
    $this->assertNoText($value_1, "After logout, previous user's session data is not available.", 'Session');

    // Now try to store some data as an anonymous user.
    $value_3 = $this->randomName();
    $this->drupalGet('session-test/set/' . $value_3);
    $this->assertText($value_3, 'Session data stored for anonymous user.', 'Session');
    $this->drupalGet('session-test/get');
    $this->assertText($value_3, 'Session correctly returned the stored data for an anonymous user.', 'Session');

    // Try to store data when drupal_save_session(FALSE).
    $value_4 = $this->randomName();
    $this->drupalGet('session-test/no-set/' . $value_4);
    $this->assertText($value_4, 'The session value was correctly passed to session-test/no-set.', 'Session');
    $this->drupalGet('session-test/get');
    $this->assertText($value_3, 'Session data is not saved for drupal_save_session(FALSE).', 'Session');

    // Login, the data should persist.
    $this->drupalLogin($user);
    $this->sessionReset($user->uid);
    $this->drupalGet('session-test/get');
    $this->assertNoText($value_1, 'Session has persisted for an authenticated user after logging out and then back in.', 'Session');

    // Change session and create another user.
    $user2 = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user2->uid);
    $this->drupalLogin($user2);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
