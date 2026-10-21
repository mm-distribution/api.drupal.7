# SessionTestCase::testEmptySessionID()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 228–247 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L228-L247)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptySessionID()
```

## Documentation

```text
Test that empty session IDs are not allowed.
```

## Code

```php
  function testEmptySessionID() {
    $user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($user);
    $this->drupalGet('session-test/is-logged-in');
    $this->assertResponse(200, 'User is logged in.');

    // Reset the sid in {sessions} to a blank string. This may exist in the
    // wild in some cases, although we normally prevent it from happening.
    db_query("UPDATE {sessions} SET sid = '' WHERE uid = :uid", array(':uid' => $user->uid));
    // Send a blank sid in the session cookie, and the session should no longer
    // be valid. Closing the curl handler will stop the previous session ID
    // from persisting.
    $this->curlClose();
    $this->additionalCurlOptions[CURLOPT_COOKIE] = rawurlencode($this->session_name) . '=;';
    $this->drupalGet('session-test/id-from-cookie');
    $this->assertRaw("session_id:\n", 'Session ID is blank as sent from cookie header.');
    // Assert that we have an anonymous session now.
    $this->drupalGet('session-test/is-logged-in');
    $this->assertResponse(403, 'An empty session ID is not allowed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
