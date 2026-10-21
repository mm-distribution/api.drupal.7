# openid_verify_assertion_signature()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 908–932 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L908-L932)
- **Module/theme:** openid

## Signature

```php
function openid_verify_assertion_signature($service, $association, $response)
```

## Documentation

```text
Verify the signature of the response received from the OpenID provider.

@param $service
  Array describing the OpenID provider.
@param $association
  Information on the association with the OpenID provider.
@param $response
  Array of response values from the provider.

@return
  TRUE if the signature is valid and covers all fields required to be signed.
@see http://openid.net/specs/openid-authentication-2_0.html#rfc.section.11.4
```

## Code

```php
function openid_verify_assertion_signature($service, $association, $response) {
  if ($service['version'] == 2) {
    // OpenID Authentication 2.0, section 10.1:
    // These keys must always be signed.
    $mandatory_keys = array('op_endpoint', 'return_to', 'response_nonce', 'assoc_handle');
    if (isset($response['openid.claimed_id'])) {
      // If present, these two keys must also be signed. According to the spec,
      // they are either both present or both absent.
      $mandatory_keys[] = 'claimed_id';
      $mandatory_keys[] = 'identity';
    }
  }
  else {
    // OpenID Authentication 1.1. section 4.3.3.
    $mandatory_keys = array('identity', 'return_to');
  }

  $keys_to_sign = explode(',', $response['openid.signed']);

  if (count(array_diff($mandatory_keys, $keys_to_sign)) > 0) {
    return FALSE;
  }

  return _openid_signature($association, $response, $keys_to_sign) === $response['openid.sig'];
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
