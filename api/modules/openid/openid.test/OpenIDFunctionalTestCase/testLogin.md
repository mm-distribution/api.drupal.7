# OpenIDFunctionalTestCase::testLogin()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 154–192 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L154-L192)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testLogin()
```

## Documentation

```text
Test login using OpenID.
```

## Code

```php
  function testLogin() {
    $this->drupalLogin($this->web_user);

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->addIdentity($identity);

    $this->drupalLogout();

    // Test logging in via the login block on the front page.
    $this->submitLoginForm($identity);
    $this->assertLink(t('Log out'), 0, 'User was logged in.');

    $this->drupalLogout();

    // Test logging in via the user/login page.
    $edit = array('openid_identifier' => $identity);
    $this->drupalPost('user/login', $edit, t('Log in'));

    // Check we are on the OpenID redirect form.
    $this->assertTitle(t('OpenID redirect'), 'OpenID redirect page was displayed.');

    // Submit form to the OpenID Provider Endpoint.
    $this->drupalPost(NULL, array(), t('Send'));

    $this->assertLink(t('Log out'), 0, 'User was logged in.');

    // Verify user was redirected away from user/login to an accessible page.
    $this->assertResponse(200);

    $this->drupalLogout();
    // Use a User-supplied Identity that is the URL of an XRDS document.
    // Tell the test module to add a doctype. This should fail.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE, 'query' => array('doctype' => 1)));
    // Test logging in via the login block on the front page.
    $edit = array('openid_identifier' => $identity);
    $this->drupalPost('', $edit, t('Log in'));
    $this->assertRaw(t('Sorry, that is not a valid OpenID. Ensure you have spelled your ID correctly.'), 'XML with DOCTYPE was rejected.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
