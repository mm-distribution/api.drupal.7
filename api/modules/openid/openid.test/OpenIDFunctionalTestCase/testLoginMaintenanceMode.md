# OpenIDFunctionalTestCase::testLoginMaintenanceMode()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 197–224 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L197-L224)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testLoginMaintenanceMode()
```

## Documentation

```text
Test login using OpenID during maintenance mode.
```

## Code

```php
  function testLoginMaintenanceMode() {
    $this->web_user = $this->drupalCreateUser(array('access site in maintenance mode'));
    $this->drupalLogin($this->web_user);

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->addIdentity($identity);
    $this->drupalLogout();

    // Enable maintenance mode.
    variable_set('maintenance_mode', 1);

    // Test logging in via the user/login page while the site is offline.
    $edit = array('openid_identifier' => $identity);
    $this->drupalPost('user/login', $edit, t('Log in'));

    // Check we are on the OpenID redirect form.
    $this->assertTitle(t('OpenID redirect'), 'OpenID redirect page was displayed.');

    // Submit form to the OpenID Provider Endpoint.
    $this->drupalPost(NULL, array(), t('Send'));

    $this->assertLink(t('Log out'), 0, 'User was logged in.');

    // Verify user was redirected away from user/login to an accessible page.
    $this->assertText(t('Operating in maintenance mode.'));
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
