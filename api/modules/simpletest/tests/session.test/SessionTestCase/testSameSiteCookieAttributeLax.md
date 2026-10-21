# SessionTestCase::testSameSiteCookieAttributeLax()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 371–377 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L371-L377)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSameSiteCookieAttributeLax()
```

## Documentation

```text
Test SameSite attribute = Lax on session cookies.
```

## Code

```php
  function testSameSiteCookieAttributeLax() {
    variable_set('samesite_cookie_value', 'Lax');
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    $this->drupalLogin($user);
    $this->assertTrue(preg_match('/SameSite=Lax/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as SameSite=Lax.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
