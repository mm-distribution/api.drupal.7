# openid_verify_assertion()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 824–891 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L824-L891)
- **Module/theme:** openid

## Signature

```php
function openid_verify_assertion($service, $response)
```

## Documentation

```text
Attempt to verify the response received from the OpenID Provider.

@param $service
  Array describing the OpenID provider.
@param $response
  Array of response values from the provider.

@return boolean
@see http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4
```

## Code

```php
function openid_verify_assertion($service, $response) {
  module_load_include('inc', 'openid');

  // http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.3
  // Check the Nonce to protect against replay attacks.
  if (!openid_verify_assertion_nonce($service, $response)) {
    return FALSE;
  }

  // http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.1
  // Verifying the return URL.
  if (!openid_verify_assertion_return_url($service, $response)) {
    return FALSE;
  }

  // http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4
  // Verify the signatures.
  $valid = FALSE;
  $association = FALSE;

  // If the OP returned a openid.invalidate_handle, we have to proceed with
  // direct verification: ignore the openid.assoc_handle, even if present.
  // See http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4.1
  if (!empty($response['openid.assoc_handle']) && empty($response['openid.invalidate_handle'])) {
    $association = db_query("SELECT * FROM {openid_association} WHERE idp_endpoint_uri = :endpoint AND assoc_handle = :assoc_handle", array(':endpoint' => $service['uri'], ':assoc_handle' => $response['openid.assoc_handle']))->fetchObject();
  }

  if ($association && isset($association->session_type)) {
    // http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4.2
    // Verification using an association.
    $valid = openid_verify_assertion_signature($service, $association, $response);
  }
  else {
    // http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4.2
    // Direct verification.
    // The verification requests contain all the fields from the response,
    // except openid.mode.
    $request = $response;
    $request['openid.mode'] = 'check_authentication';
    $message = _openid_create_message($request);
    $options = array(
      'headers' => array('Content-Type' => 'application/x-www-form-urlencoded; charset=utf-8'),
      'method' => 'POST',
      'data' => _openid_encode_message($message),
    );
    $result = drupal_http_request($service['uri'], $options);
    if (!isset($result->error)) {
      $response = _openid_parse_message($result->data);

      if (strtolower(trim($response['is_valid'])) == 'true') {
        $valid = TRUE;
        if (!empty($response['invalidate_handle'])) {
          // This association handle has expired on the OP side, remove it from the
          // database to avoid reusing it again on a subsequent authentication request.
          // See http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4.2.2
          db_delete('openid_association')
            ->condition('idp_endpoint_uri', $service['uri'])
            ->condition('assoc_handle', $response['invalidate_handle'])
            ->execute();
        }
      }
      else {
        $valid = FALSE;
      }
    }
  }
  return $valid;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
