# OpenIDFunctionalTestCase::testSignatureValidation()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 351–397 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L351-L397)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testSignatureValidation()
```

## Documentation

```text
Tests that openid.signed is verified.
```

## Code

```php
  function testSignatureValidation() {
    // Use a User-supplied Identity that is the URL of an XRDS document.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));

    // Respond with an invalid signature.
    variable_set('openid_test_response', array('openid.sig' => 'this-is-an-invalid-signature'));
    $this->submitLoginForm($identity);
    $this->assertRaw('OpenID login failed.');

    // Do not sign the mandatory field openid.assoc_handle.
    variable_set('openid_test_response', array('openid.signed' => 'op_endpoint,claimed_id,identity,return_to,response_nonce'));
    $this->submitLoginForm($identity);
    $this->assertRaw('OpenID login failed.');

    // Sign all mandatory fields and a custom field.
    $keys_to_sign = array('op_endpoint', 'claimed_id', 'identity', 'return_to', 'response_nonce', 'assoc_handle', 'foo');
    $association = new stdClass();
    $association->mac_key = variable_get('mac_key');
    $response = array(
      'openid.op_endpoint' => url('openid-test/endpoint', array('absolute' => TRUE)),
      'openid.claimed_id' => $identity,
      'openid.identity' => $identity,
      'openid.return_to' => url('openid/authenticate', array('absolute' => TRUE)),
      'openid.response_nonce' => _openid_nonce(),
      'openid.assoc_handle' => 'openid-test',
      'openid.foo' => 123,
      'openid.signed' => implode(',', $keys_to_sign),
    );
    $response['openid.sig'] = _openid_signature($association, $response, $keys_to_sign);
    variable_set('openid_test_response', $response);
    $this->submitLoginForm($identity);
    $this->assertNoRaw('OpenID login failed.');
    $this->assertFieldByName('name', '', 'No username was supplied by provider.');
    $this->assertFieldByName('mail', '', 'No e-mail address was supplied by provider.');

    // Check that unsigned SREG fields are ignored.
    $response = array(
      'openid.signed' => 'op_endpoint,claimed_id,identity,return_to,response_nonce,assoc_handle,sreg.nickname',
      'openid.sreg.nickname' => 'john',
      'openid.sreg.email' => 'john@example.com',
    );
    variable_set('openid_test_response', $response);
    $this->submitLoginForm($identity);
    $this->assertNoRaw('OpenID login failed.');
    $this->assertFieldByName('name', 'john', 'Username was supplied by provider.');
    $this->assertFieldByName('mail', '', 'E-mail address supplied by provider was ignored.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
