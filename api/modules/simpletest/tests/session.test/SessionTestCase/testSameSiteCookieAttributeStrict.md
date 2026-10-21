# SessionTestCase::testSameSiteCookieAttributeStrict()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 382–388 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L382-L388)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSameSiteCookieAttributeStrict()
```

## Documentation

```text
Test SameSite attribute = Strict on session cookies.
```

## Code

```php
  function testSameSiteCookieAttributeStrict() {
    variable_set('samesite_cookie_value', 'Strict');
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    $this->drupalLogin($user);
    $this->assertTrue(preg_match('/SameSite=Strict/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as SameSite=Strict.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
