# OpenIDRegistrationTestCase::testRegisterUserWithInvalidSreg()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 481–513 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L481-L513)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testRegisterUserWithInvalidSreg()
```

## Documentation

```text
Test OpenID auto-registration with a provider that supplies invalid SREG
information (a username that is already taken, and no e-mail address).
```

## Code

```php
  function testRegisterUserWithInvalidSreg() {
    // Tell openid_test.module to respond with these SREG fields.
    $web_user = $this->drupalCreateUser(array());
    variable_set('openid_test_response', array('openid.sreg.nickname' => $web_user->name, 'openid.sreg.email' => 'mail@invalid#'));

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->submitLoginForm($identity);

    $this->assertRaw(t('Account registration using the information provided by your OpenID provider failed due to the reasons listed below. Complete the registration by filling out the form below. If you already have an account, you can <a href="@login">log in</a> now and add your OpenID under "My account".', array('@login' => url('user/login'))), 'User was asked to complete the registration process manually.');
    $this->assertRaw(t('The name %name is already taken.', array('%name' => $web_user->name)), 'Form validation error for username was displayed.');
    $this->assertRaw(t('The e-mail address %mail is not valid.', array('%mail' => 'mail@invalid#')), 'Form validation error for e-mail address was displayed.');

    // Enter username and e-mail address manually.
    $edit = array('name' => 'john', 'mail' => 'john@example.com');
    $this->drupalPost(NULL, $edit, t('Create new account'));
    $this->assertRaw(t('Once you have verified your e-mail address, you may log in via OpenID.'), 'User was asked to verify e-mail address.');
    $reset_url = $this->getPasswordResetURLFromMail();

    $user = user_load_by_name('john');
    $this->assertTrue($user, 'User was registered with right username.');
    $this->assertFalse($user->data, 'No additional user info was saved.');

    // Follow the one-time login that was sent in the welcome e-mail.
    $this->drupalGet($reset_url);
    $this->drupalPost(NULL, array(), t('Log in'));

    // The user is taken to user/%uid/edit.
    $this->assertFieldByName('mail', 'john@example.com', 'User was registered with right e-mail address.');

    $this->clickLink(t('OpenID identities'));
    $this->assertRaw($identity, 'OpenID identity was registered.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
