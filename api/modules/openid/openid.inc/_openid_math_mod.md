# _openid_math_mod()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 792–800 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L792-L800)
- **Module/theme:** openid

## Signature

```php
function _openid_math_mod($x, $y)
```

## Documentation

```text
Calls the mod function from the available math library for OpenID.
```

## Code

```php
function _openid_math_mod($x, $y) {
  $library = _openid_get_math_library();
  switch ($library) {
    case 'gmp':
      return gmp_mod($x, $y);
    case 'bcmath':
      return bcmod($x, $y);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
