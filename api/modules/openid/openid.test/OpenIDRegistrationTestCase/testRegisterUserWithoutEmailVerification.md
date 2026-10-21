# OpenIDRegistrationTestCase::testRegisterUserWithoutEmailVerification()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 455–475 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L455-L475)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testRegisterUserWithoutEmailVerification()
```

## Documentation

```text
Test OpenID auto-registration with e-mail verification disabled.
```

## Code

```php
  function testRegisterUserWithoutEmailVerification() {
    variable_set('user_email_verification', FALSE);

    // Tell openid_test.module to respond with these SREG fields.
    variable_set('openid_test_response', array('openid.sreg.nickname' => 'john', 'openid.sreg.email' => 'john@example.com'));

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->submitLoginForm($identity);
    $this->assertLink(t('Log out'), 0, 'User was logged in.');

    $user = user_load_by_name('john');
    $this->assertTrue($user, 'User was registered with right username.');
    $this->assertEqual($user->mail, 'john@example.com', 'User was registered with right email address.');
    $this->assertFalse($user->data, 'No additional user info was saved.');

    $this->drupalLogout();

    $this->submitLoginForm($identity);
    $this->assertLink(t('Log out'), 0, 'User was logged in.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
