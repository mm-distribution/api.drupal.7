# OpenIDRegistrationTestCase::testRegisterUserWithAXButNoSREG()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 555–576 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L555-L576)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testRegisterUserWithAXButNoSREG()
```

## Documentation

```text
Test OpenID auto-registration with a provider that supplies AX information,
but no SREG.
```

## Code

```php
  function testRegisterUserWithAXButNoSREG() {
    variable_set('user_email_verification', FALSE);

    // Tell openid_test.module to respond with these AX fields.
    variable_set('openid_test_response', array(
      'openid.ns.ext123' => 'http://openid.net/srv/ax/1.0',
      'openid.ext123.type.mail456' => 'http://axschema.org/contact/email',
      'openid.ext123.value.mail456' => 'john@example.com',
      'openid.ext123.type.name789' => 'http://schema.openid.net/namePerson/friendly',
      'openid.ext123.count.name789' => '1',
      'openid.ext123.value.name789.1' => 'john',
    ));

    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->submitLoginForm($identity);
    $this->assertLink(t('Log out'), 0, 'User was logged in.');

    $user = user_load_by_name('john');
    $this->assertTrue($user, 'User was registered with right username.');
    $this->assertEqual($user->mail, 'john@example.com', 'User was registered with right email address.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
