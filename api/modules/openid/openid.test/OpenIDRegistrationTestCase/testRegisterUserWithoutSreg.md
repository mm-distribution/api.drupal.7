# OpenIDRegistrationTestCase::testRegisterUserWithoutSreg()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 519–549 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L519-L549)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testRegisterUserWithoutSreg()
```

## Documentation

```text
Test OpenID auto-registration with a provider that does not supply SREG
information (i.e. no username or e-mail address).
```

## Code

```php
  function testRegisterUserWithoutSreg() {
    // Load the front page to get the user login block.
    $this->drupalGet('');

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->submitLoginForm($identity);
    $this->assertRaw(t('Complete the registration by filling out the form below. If you already have an account, you can <a href="@login">log in</a> now and add your OpenID under "My account".', array('@login' => url('user/login'))), 'User was asked to complete the registration process manually.');
    $this->assertNoRaw(t('You must enter a username.'), 'Form validation error for username was not displayed.');
    $this->assertNoRaw(t('You must enter an e-mail address.'), 'Form validation error for e-mail address was not displayed.');

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
