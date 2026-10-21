# openid_association()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 596–651 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L596-L651)
- **Module/theme:** openid

## Signature

```php
function openid_association($op_endpoint)
```

## Documentation

```text
Attempt to create a shared secret with the OpenID Provider.

@param $op_endpoint URL of the OpenID Provider endpoint.

@return $assoc_handle The association handle.
```

## Code

```php
function openid_association($op_endpoint) {
  module_load_include('inc', 'openid');

  // Remove Old Associations:
  db_delete('openid_association')
    ->where('created + expires_in < :request_time', array(':request_time' => REQUEST_TIME))
    ->execute();

  // Check to see if we have an association for this IdP already
  $assoc_handle = db_query("SELECT assoc_handle FROM {openid_association} WHERE idp_endpoint_uri = :endpoint", array(':endpoint' => $op_endpoint))->fetchField();
  if (empty($assoc_handle)) {
    $mod = OPENID_DH_DEFAULT_MOD;
    $gen = OPENID_DH_DEFAULT_GEN;
    $r = _openid_dh_rand($mod);
    $private = _openid_math_add($r, 1);
    $public = _openid_math_powmod($gen, $private, $mod);

    // If there is no existing association, then request one
    $assoc_request = openid_association_request($public);
    $assoc_message = _openid_encode_message(_openid_create_message($assoc_request));
    $assoc_options = array(
      'headers' => array('Content-Type' => 'application/x-www-form-urlencoded; charset=utf-8'),
      'method' => 'POST',
      'data' => $assoc_message,
    );
    $assoc_result = drupal_http_request($op_endpoint, $assoc_options);
    if (isset($assoc_result->error)) {
      return FALSE;
    }

    $assoc_response = _openid_parse_message($assoc_result->data);
    if (isset($assoc_response['mode']) && $assoc_response['mode'] == 'error') {
      return FALSE;
    }

    if ($assoc_response['session_type'] == 'DH-SHA1') {
      $spub = _openid_dh_base64_to_long($assoc_response['dh_server_public']);
      $enc_mac_key = base64_decode($assoc_response['enc_mac_key']);
      $shared = _openid_math_powmod($spub, $private, $mod);
      $assoc_response['mac_key'] = base64_encode(_openid_dh_xorsecret($shared, $enc_mac_key));
    }
    db_insert('openid_association')
      ->fields(array(
        'idp_endpoint_uri' => $op_endpoint,
        'session_type' => $assoc_response['session_type'],
        'assoc_handle' => $assoc_response['assoc_handle'],
        'assoc_type' => $assoc_response['assoc_type'],
        'expires_in' => $assoc_response['expires_in'],
        'mac_key' => $assoc_response['mac_key'],
        'created' => REQUEST_TIME,
      ))
      ->execute();
    $assoc_handle = $assoc_response['assoc_handle'];
  }
  return $assoc_handle;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
