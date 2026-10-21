# _openid_dh_xorsecret()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 519–528 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L519-L528)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_xorsecret($shared, $secret)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_xorsecret($shared, $secret) {
  $dh_shared_str = _openid_dh_long_to_binary($shared);
  $sha1_dh_shared = sha1($dh_shared_str, TRUE);
  $xsecret = "";
  for ($i = 0; $i < strlen($secret); $i++) {
    $xsecret .= chr(ord($secret[$i]) ^ ord($sha1_dh_shared[$i]));
  }

  return $xsecret;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
