# OpenIDFunctionalTestCase::addIdentity()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 286–311 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L286-L311)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function addIdentity($identity, $version = 2, $local_id = 'http://example.com/xrds', $claimed_id = NULL)
```

## Documentation

```text
Add OpenID identity to user's profile.

@param $identity
  The User-supplied Identifier.
@param $version
  The protocol version used by the service.
@param $local_id
  The expected OP-Local Identifier found during discovery.
@param $claimed_id
  The expected Claimed Identifier returned by the OpenID Provider, or FALSE
  if the discovery is expected to fail.
```

## Code

```php
  function addIdentity($identity, $version = 2, $local_id = 'http://example.com/xrds', $claimed_id = NULL) {
    // Tell openid_test.module to only accept this OP-Local Identifier.
    variable_set('openid_test_identity', $local_id);

    $edit = array('openid_identifier' => $identity);
    $this->drupalPost('user/' . $this->web_user->uid . '/openid', $edit, t('Add an OpenID'));

    if ($claimed_id === FALSE) {
      $this->assertRaw(t('Sorry, that is not a valid OpenID. Ensure you have spelled your ID correctly.'), 'Invalid identity was rejected.');
      return;
    }

    // OpenID 1 used a HTTP redirect, OpenID 2 uses a HTML form that is submitted automatically using JavaScript.
    if ($version == 2) {
      // Check we are on the OpenID redirect form.
      $this->assertTitle(t('OpenID redirect'), 'OpenID redirect page was displayed.');

      // Submit form to the OpenID Provider Endpoint.
      $this->drupalPost(NULL, array(), t('Send'));
    }

    if (!isset($claimed_id)) {
      $claimed_id = $identity;
    }
    $this->assertRaw(t('Successfully added %identity', array('%identity' => $claimed_id)), format_string('Identity %identity was added.', array('%identity' => $identity)));
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
