# SessionTestCase::testSessionSaveRegenerate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 26–70 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L26-L70)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSessionSaveRegenerate()
```

## Documentation

```text
Tests for drupal_save_session() and drupal_session_regenerate().
```

## Code

```php
  function testSessionSaveRegenerate() {
    $this->assertFalse(drupal_save_session(), 'drupal_save_session() correctly returns FALSE (inside of testing framework) when initially called with no arguments.', 'Session');
    $this->assertFalse(drupal_save_session(FALSE), 'drupal_save_session() correctly returns FALSE when called with FALSE.', 'Session');
    $this->assertFalse(drupal_save_session(), 'drupal_save_session() correctly returns FALSE when saving has been disabled.', 'Session');
    $this->assertTrue(drupal_save_session(TRUE), 'drupal_save_session() correctly returns TRUE when called with TRUE.', 'Session');
    $this->assertTrue(drupal_save_session(), 'drupal_save_session() correctly returns TRUE when saving has been enabled.', 'Session');

    // Test session hardening code from SA-2008-044.
    $user = $this->drupalCreateUser(array('access content'));

    // Enable sessions.
    $this->sessionReset($user->uid);

    // Make sure the session cookie is set as HttpOnly.
    $this->drupalLogin($user);
    $this->assertTrue(preg_match('/HttpOnly/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as HttpOnly.');
    $this->drupalLogout();

    // Verify that the session is regenerated if a module calls exit
    // in hook_user_login().
    user_save($user, array('name' => 'session_test_user'));
    $user->name = 'session_test_user';
    $this->drupalGet('session-test/id');
    $matches = array();
    preg_match('/\s*session_id:(.*)\n/', $this->drupalGetContent(), $matches);
    $this->assertTrue(!empty($matches[1]) , 'Found session ID before logging in.');
    $original_session = $matches[1];

    // We cannot use $this->drupalLogin($user); because we exit in
    // session_test_user_login() which breaks a normal assertion.
    $edit = array(
      'name' => $user->name,
      'pass' => $user->pass_raw
    );
    $this->drupalPost('user', $edit, t('Log in'));
    $this->drupalGet('user');
    $pass = $this->assertText($user->name, format_string('Found name: %name', array('%name' => $user->name)), 'User login');
    $this->_logged_in = $pass;

    $this->drupalGet('session-test/id');
    $matches = array();
    preg_match('/\s*session_id:(.*)\n/', $this->drupalGetContent(), $matches);
    $this->assertTrue(!empty($matches[1]) , 'Found session ID after logging in.');
    $this->assertTrue($matches[1] != $original_session, 'Session ID changed after login.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
