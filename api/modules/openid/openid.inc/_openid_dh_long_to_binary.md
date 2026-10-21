# _openid_dh_long_to_binary()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 490–517 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L490-L517)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_long_to_binary($long)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_long_to_binary($long) {
  $cmp = _openid_math_cmp($long, 0);
  if ($cmp < 0) {
    return FALSE;
  }

  if ($cmp == 0) {
    return "\x00";
  }

  $bytes = array();

  while (_openid_math_cmp($long, 0) > 0) {
    array_unshift($bytes, _openid_math_mod($long, 256));
    $long = _openid_math_div($long, pow(2, 8));
  }

  if ($bytes && ($bytes[0] > 127)) {
    array_unshift($bytes, 0);
  }

  $string = '';
  foreach ($bytes as $byte) {
    $string .= pack('C', $byte);
  }

  return $string;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
