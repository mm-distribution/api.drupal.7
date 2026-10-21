# OpenIDInvalidIdentifierTransitionTestCase::testStrippedFragmentAccountAutoUpdateSreg()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 633–659 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L633-L659)
- **Class:** [OpenIDInvalidIdentifierTransitionTestCase](../OpenIDInvalidIdentifierTransitionTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testStrippedFragmentAccountAutoUpdateSreg()
```

## Documentation

```text
Test OpenID auto transition with e-mail.
```

## Code

```php
  function testStrippedFragmentAccountAutoUpdateSreg() {
    $this->drupalLogin($this->web_user);

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE, 'fragment' => $this->randomName()));
    $identity_stripped = preg_replace('/#.*/', '', $identity);

    // Add invalid identifier to the authmap (identifier has stripped fragment).
    $this->addIdentity($identity_stripped);
    $this->drupalLogout();

    // Test logging in via the login form, provider will respond with full
    // identifier (including fragment) but with different email, so we can't
    // provide auto-update.
    variable_set('openid_test_response', array(
      'openid.claimed_id' => $identity,
      'openid.sreg.nickname' => $this->web_user->name,
      'openid.sreg.email' => $this->web_user->mail));

    $this->submitLoginForm($identity_stripped);

    // Verify user was redirected away from user login to an accessible page.
    $this->assertResponse(200);

    // Verify the message.
    $this->assertRaw(t('New OpenID identifier %identity was added as a replacement for invalid identifier %invalid_identity.', array('%invalid_identity' => $identity_stripped, '%identity' => $identity)), 'Message that OpenID identifier was added automatically was displayed.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
