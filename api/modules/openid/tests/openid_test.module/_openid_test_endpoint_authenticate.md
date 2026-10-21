# _openid_test_endpoint_authenticate()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 314–368 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L314-L368)
- **Module/theme:** openid_test

## Signature

```php
function _openid_test_endpoint_authenticate()
```

## Documentation

```text
OpenID endpoint; handle "authenticate" requests.

All requests result in a successful response. The request is a GET or POST
made by the user's browser based on an HTML form or HTTP redirect generated
by the Relying Party. The user is redirected back to the Relying Party using
a URL containing a signed message in the query string confirming the user's
identity.
```

## Code

```php
function _openid_test_endpoint_authenticate() {
  module_load_include('inc', 'openid');

  $expected_identity = variable_get('openid_test_identity');
  if ($expected_identity && $_REQUEST['openid_identity'] != $expected_identity) {
    $response = variable_get('openid_test_response', array()) + array(
      'openid.ns' => OPENID_NS_2_0,
      'openid.mode' => 'error',
      'openid.error' => 'Unexpted identity',
    );
    drupal_add_http_header('Content-Type', 'text/plain');
    header('Location: ' . url($_REQUEST['openid_return_to'], array('query' => $response, 'external' => TRUE)));
    return;
  }

  // Generate unique identifier for this authentication.
  $nonce = _openid_nonce();

  // Generate response containing the user's identity.
  $response = variable_get('openid_test_response', array()) + array(
    'openid.ns' => OPENID_NS_2_0,
    'openid.mode' => 'id_res',
    'openid.op_endpoint' => url('openid-test/endpoint', array('absolute' => TRUE)),
    'openid.claimed_id' => !empty($_REQUEST['openid_claimed_id']) ? $_REQUEST['openid_claimed_id'] : '',
    'openid.identity' => $_REQUEST['openid_identity'],
    'openid.return_to' => $_REQUEST['openid_return_to'],
    'openid.response_nonce' => $nonce,
    'openid.assoc_handle' => 'openid-test',
  );

  if (isset($response['openid.signed'])) {
    $keys_to_sign = explode(',', $response['openid.signed']);
  }
  else {
    // Unless openid.signed is explicitly defined, all keys are signed.
    $keys_to_sign = array();
    foreach ($response as $key => $value) {
      // Strip off the "openid." prefix.
      $keys_to_sign[] = substr($key, 7);
    }
    $response['openid.signed'] = implode(',', $keys_to_sign);
  }

  // Sign the message using the MAC key that was exchanged during association.
  $association = new stdClass();
  $association->mac_key = variable_get('mac_key');
  if (!isset($response['openid.sig'])) {
    $response['openid.sig'] = _openid_signature($association, $response, $keys_to_sign);
  }

  // Put the signed message into the query string of a URL supplied by the
  // Relying Party, and redirect the user.
  drupal_add_http_header('Content-Type', 'text/plain');
  header('Location: ' . url($_REQUEST['openid_return_to'], array('query' => $response, 'external' => TRUE)));
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
