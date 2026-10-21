# SessionTestCase::testEmptyAnonymousSession()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 136–181 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L136-L181)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptyAnonymousSession()
```

## Documentation

```text
Test that empty anonymous sessions are destroyed.
```

## Code

```php
  function testEmptyAnonymousSession() {
    // Verify that no session is automatically created for anonymous user.
    $this->drupalGet('');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(TRUE);

    // The same behavior is expected when caching is enabled.
    variable_set('cache', 1);
    $this->drupalGet('');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(TRUE);
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');

    // Start a new session by setting a message.
    $this->drupalGet('session-test/set-message');
    $this->assertSessionCookie(TRUE);
    $this->assertTrue($this->drupalGetHeader('Set-Cookie'), 'New session was started.');

    // Display the message, during the same request the session is destroyed
    // and the session cookie is unset.
    $this->drupalGet('');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(FALSE);
    $this->assertFalse($this->drupalGetHeader('X-Drupal-Cache'), 'Caching was bypassed.');
    $this->assertText(t('This is a dummy message.'), 'Message was displayed.');
    $this->assertTrue(preg_match('/SESS\w+=deleted/', $this->drupalGetHeader('Set-Cookie')), 'Session cookie was deleted.');

    // Verify that session was destroyed.
    $this->drupalGet('');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(TRUE);
    $this->assertNoText(t('This is a dummy message.'), 'Message was not cached.');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $this->assertFalse($this->drupalGetHeader('Set-Cookie'), 'New session was not started.');

    // Verify that no session is created if drupal_save_session(FALSE) is called.
    $this->drupalGet('session-test/set-message-but-dont-save');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(TRUE);

    // Verify that no message is displayed.
    $this->drupalGet('');
    $this->assertSessionCookie(FALSE);
    $this->assertSessionEmpty(TRUE);
    $this->assertNoText(t('This is a dummy message.'), 'The message was not saved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
