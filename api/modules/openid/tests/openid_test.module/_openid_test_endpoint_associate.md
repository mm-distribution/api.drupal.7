# _openid_test_endpoint_associate()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 265–303 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L265-L303)
- **Module/theme:** openid_test

## Signature

```php
function _openid_test_endpoint_associate()
```

## Documentation

```text
OpenID endpoint; handle "associate" requests (see OpenID Authentication 2.0,
section 8).

The purpose of association is to send the secret MAC key to the Relying Party
using Diffie-Hellman key exchange. The MAC key is used in subsequent
"authenticate" requests. The "associate" request is made by the Relying Party
(in the testing scenario, this is the OpenID module that communicates with
the endpoint using drupal_http_request()).
```

## Code

```php
function _openid_test_endpoint_associate() {
  module_load_include('inc', 'openid');

  // Use default parameters for Diffie-Helmann key exchange.
  $mod = OPENID_DH_DEFAULT_MOD;
  $gen = OPENID_DH_DEFAULT_GEN;

  // Generate private Diffie-Helmann key.
  $r = _openid_dh_rand($mod);
  $private = _openid_math_add($r, 1);

  // Calculate public Diffie-Helmann key.
  $public = _openid_math_powmod($gen, $private, $mod);

  // Calculate shared secret based on Relying Party's public key.
  $cpub = _openid_dh_base64_to_long($_REQUEST['openid_dh_consumer_public']);
  $shared = _openid_math_powmod($cpub, $private, $mod);

  // Encrypt the MAC key using the shared secret.
  $enc_mac_key = base64_encode(_openid_dh_xorsecret($shared, base64_decode(variable_get('mac_key'))));

  // Generate response including our public key and the MAC key. Using our
  // public key and its own private key, the Relying Party can calculate the
  // shared secret, and with this it can decrypt the encrypted MAC key.
  $response = array(
    'ns' => 'http://specs.openid.net/auth/2.0',
    'assoc_handle' => 'openid-test',
    'session_type' => $_REQUEST['openid_session_type'],
    'assoc_type' => $_REQUEST['openid_assoc_type'],
    'expires_in' => '3600',
    'dh_server_public' => _openid_dh_long_to_base64($public),
    'enc_mac_key' => $enc_mac_key,
  );

  // Respond to Relying Party in the special Key-Value Form Encoding (see OpenID
  // Authentication 1.0, section 4.1.1).
  drupal_add_http_header('Content-Type', 'text/plain');
  print _openid_create_message($response);
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
