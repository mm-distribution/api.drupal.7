# openid_complete()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 328–398 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L328-L398)
- **Module/theme:** openid

## Signature

```php
function openid_complete($response = array())
```

## Documentation

```text
Completes OpenID authentication by validating returned data from the OpenID
Provider.

@param $response Array of returned values from the OpenID Provider.

@return $response Response values for further processing with
  $response['status'] set to one of 'success', 'failed' or 'cancel'.
```

## Code

```php
function openid_complete($response = array()) {
  module_load_include('inc', 'openid');

  if (count($response) == 0) {
    $response = _openid_response();
  }

  // Default to failed response
  $response['status'] = 'failed';
  if (isset($_SESSION['openid']['service']['uri']) && isset($_SESSION['openid']['claimed_id'])) {
    $service = $_SESSION['openid']['service'];
    $claimed_id = $_SESSION['openid']['claimed_id'];
    unset($_SESSION['openid']['service']);
    unset($_SESSION['openid']['claimed_id']);
    if (isset($response['openid.mode'])) {
      if ($response['openid.mode'] == 'cancel') {
        $response['status'] = 'cancel';
      }
      else {
        if (openid_verify_assertion($service, $response)) {
          // OpenID Authentication, section 7.3.2.3 and Appendix A.5:
          // The CanonicalID specified in the XRDS document must be used as the
          // account key. We rely on the XRI proxy resolver to verify that the
          // provider is authorized to respond on behalf of the specified
          // identifer (required per Extensible Resource Identifier (XRI)
          // (XRI) Resolution Version 2.0, section 14.3):
          if (!empty($service['claimed_id'])) {
            $response['openid.claimed_id'] = $service['claimed_id'];
          }
          elseif ($service['version'] == 2) {
            // Returned Claimed Identifier could contain unique fragment
            // identifier to allow identifier recycling so we need to preserve
            // it in the response.
            $response_claimed_id = openid_normalize($response['openid.claimed_id']);

            // OpenID Authentication, section 11.2:
            // If the returned Claimed Identifier is different from the one sent
            // to the OpenID Provider, we need to do discovery on the returned
            // identififer to make sure that the provider is authorized to
            // respond on behalf of this.
            if ($response_claimed_id != $claimed_id || $response_claimed_id != $response['openid.identity']) {
              $discovery = openid_discovery($response['openid.claimed_id']);
              $uris = array();
              if ($discovery && !empty($discovery['services'])) {
                foreach ($discovery['services'] as $discovered_service) {
                  if (!in_array('http://specs.openid.net/auth/2.0/server', $discovered_service['types']) && !in_array('http://specs.openid.net/auth/2.0/signon', $discovered_service['types'])) {
                    continue;
                  }
                  // The OP-Local Identifier (if different than the Claimed
                  // Identifier) must be present in the XRDS document.
                  if ($response_claimed_id != $response['openid.identity'] && (!isset($discovered_service['identity']) || $discovered_service['identity'] != $response['openid.identity'])) {
                    continue;
                  }
                  $uris[] = $discovered_service['uri'];
                }
              }
              if (!in_array($service['uri'], $uris)) {
                return $response;
              }
            }
          }
          else {
            $response['openid.claimed_id'] = $claimed_id;
          }
          $response['status'] = 'success';
        }
      }
    }
  }
  return $response;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
