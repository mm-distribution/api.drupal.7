# openid_verify_assertion_return_url()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 1008–1029 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L1008-L1029)
- **Module/theme:** openid

## Signature

```php
function openid_verify_assertion_return_url($service, $response)
```

## Documentation

```text
Verify that openid.return_to matches the current URL.

See OpenID  Authentication 2.0, section 11.1. While OpenID Authentication
1.1, section 4.3 does not mandate return_to verification, the received
return_to should still match these constraints.

@param $service
  Array describing the OpenID provider.
@param $response
  Array of response values from the provider.

@return
  TRUE if return_to is valid, FALSE otherwise.
```

## Code

```php
function openid_verify_assertion_return_url($service, $response) {
  global $base_url;

  $return_to_parts = parse_url($response['openid.return_to']);

  $base_url_parts = parse_url($base_url);
  $current_parts = parse_url($base_url_parts['scheme'] .'://'. $base_url_parts['host'] . request_uri());

  if ($return_to_parts['scheme'] != $current_parts['scheme'] || $return_to_parts['host'] != $current_parts['host'] || $return_to_parts['path'] != $current_parts['path']) {
    return FALSE;
  }
  // Verify that all query parameters in the openid.return_to URL have
  // the same value in the current URL. In addition, the current URL
  // contains a number of other parameters added by the OpenID Provider.
  parse_str(isset($return_to_parts['query']) ? $return_to_parts['query'] : '', $return_to_query_parameters);
  foreach ($return_to_query_parameters as $name => $value) {
    if (!isset($_GET[$name]) || $_GET[$name] != $value) {
      return FALSE;
    }
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
