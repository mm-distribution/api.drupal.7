# OpenIDRegistrationTestCase::testRegisterUserWithEmailVerification()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 420–450 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L420-L450)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testRegisterUserWithEmailVerification()
```

## Documentation

```text
Test OpenID auto-registration with e-mail verification enabled.
```

## Code

```php
  function testRegisterUserWithEmailVerification() {
    variable_set('user_email_verification', TRUE);

    // Tell openid_test.module to respond with these SREG fields.
    variable_set('openid_test_response', array('openid.sreg.nickname' => 'john', 'openid.sreg.email' => 'john@example.com'));

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->submitLoginForm($identity);
    $this->assertRaw(t('Once you have verified your e-mail address, you may log in via OpenID.'), 'User was asked to verify e-mail address.');
    $this->assertRaw(t('A welcome message with further instructions has been sent to your e-mail address.'), 'A welcome message was sent to the user.');
    $reset_url = $this->getPasswordResetURLFromMail();

    $user = user_load_by_name('john');
    $this->assertTrue($user, 'User was registered with right username.');
    $this->assertEqual($user->mail, 'john@example.com', 'User was registered with right email address.');
    $this->assertFalse($user->data, 'No additional user info was saved.');

    $this->submitLoginForm($identity);
    $this->assertRaw(t('You must validate your email address for this account before logging in via OpenID.'));

    // Follow the one-time login that was sent in the welcome e-mail.
    $this->drupalGet($reset_url);
    $this->drupalPost(NULL, array(), t('Log in'));

    $this->drupalLogout();

    // Verify that the account was activated.
    $this->submitLoginForm($identity);
    $this->assertLink(t('Log out'), 0, 'User was logged in.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
