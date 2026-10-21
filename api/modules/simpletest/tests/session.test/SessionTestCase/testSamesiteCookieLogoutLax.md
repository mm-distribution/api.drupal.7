# SessionTestCase::testSamesiteCookieLogoutLax()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 483–490 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L483-L490)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSamesiteCookieLogoutLax()
```

## Documentation

```text
Test SameSite attribute = Lax on set-cookie header on logout.
```

## Code

```php
  function testSamesiteCookieLogoutLax() {
    variable_set('samesite_cookie_value', 'Lax');
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    $this->drupalLogin($user);
    $this->drupalGet('user/logout');
    $this->assertTrue(preg_match('/SameSite=Lax/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie deletion includes SameSite=Lax.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
