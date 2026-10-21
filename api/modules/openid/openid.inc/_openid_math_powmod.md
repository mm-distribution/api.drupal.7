# _openid_math_powmod()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 818–826 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L818-L826)
- **Module/theme:** openid

## Signature

```php
function _openid_math_powmod($x, $y, $z)
```

## Documentation

```text
Calls the mul function from the available math library for OpenID.
```

## Code

```php
function _openid_math_powmod($x, $y, $z) {
  $library = _openid_get_math_library();
  switch ($library) {
    case 'gmp':
      return gmp_powm($x, $y, $z);
    case 'bcmath':
      return bcpowmod($x, $y, $z);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
