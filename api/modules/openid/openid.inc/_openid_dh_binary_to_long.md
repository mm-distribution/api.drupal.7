# _openid_dh_binary_to_long()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 478–488 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L478-L488)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_binary_to_long($str)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_binary_to_long($str) {
  $bytes = array_merge(unpack('C*', $str));

  $n = 0;
  foreach ($bytes as $byte) {
    $n = _openid_math_mul($n, pow(2, 8));
    $n = _openid_math_add($n, $byte);
  }

  return $n;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
