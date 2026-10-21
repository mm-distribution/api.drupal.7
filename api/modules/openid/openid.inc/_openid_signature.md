# _openid_signature()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 437–452 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L437-L452)
- **Module/theme:** openid

## Signature

```php
function _openid_signature($association, $message_array, $keys_to_sign)
```

## Documentation

```text
Sign certain keys in a message
@param $association - object loaded from openid_association or openid_server_association table
             - important fields are ->assoc_type and ->mac_key
@param $message_array - array of entire message about to be sent
@param $keys_to_sign - keys in the message to include in signature (without
 'openid.' appended)
```

## Code

```php
function _openid_signature($association, $message_array, $keys_to_sign) {
  $signature = '';
  $sign_data = array();

  foreach ($keys_to_sign as $key) {
    if (isset($message_array['openid.' . $key])) {
      $sign_data[$key] = $message_array['openid.' . $key];
    }
  }

  $message = _openid_create_message($sign_data);
  $secret = base64_decode((string) $association->mac_key);
  $signature = _openid_hmac($secret, $message);

  return base64_encode($signature);
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
