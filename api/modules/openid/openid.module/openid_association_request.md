# openid_association_request()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 728–744 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L728-L744)
- **Module/theme:** openid

## Signature

```php
function openid_association_request($public)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_association_request($public) {
  module_load_include('inc', 'openid');

  $request = array(
    'openid.ns' => OPENID_NS_2_0,
    'openid.mode' => 'associate',
    'openid.session_type' => 'DH-SHA1',
    'openid.assoc_type' => 'HMAC-SHA1'
  );

  if ($request['openid.session_type'] == 'DH-SHA1' || $request['openid.session_type'] == 'DH-SHA256') {
    $cpub = _openid_dh_long_to_base64($public);
    $request['openid.dh_consumer_public'] = $cpub;
  }

  return $request;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
