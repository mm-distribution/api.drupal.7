# OpenIDFunctionalTestCase::testBlockedUserLogin()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 248–271 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L248-L271)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testBlockedUserLogin()
```

## Documentation

```text
Test that a blocked user cannot log in.
```

## Code

```php
  function testBlockedUserLogin() {
    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));

    // Log in and add an OpenID Identity to the account.
    $this->drupalLogin($this->web_user);
    $this->addIdentity($identity);
    $this->drupalLogout();

    // Log in as an admin user and block the account.
    $admin_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($admin_user);
    $this->drupalGet('admin/people');
    $edit = array(
      'operation' => 'block',
      'accounts[' . $this->web_user->uid . ']' => TRUE,
    );
    $this->drupalPost('admin/people', $edit, t('Update'));
    $this->assertRaw('The update has been performed.', 'Account was blocked.');
    $this->drupalLogout();

    $this->submitLoginForm($identity);
    $this->assertRaw(t('The username %name has not been activated or is blocked.', array('%name' => $this->web_user->name)), 'User login was blocked.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
