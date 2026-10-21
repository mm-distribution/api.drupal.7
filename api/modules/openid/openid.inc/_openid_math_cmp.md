# _openid_math_cmp()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 779–787 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L779-L787)
- **Module/theme:** openid

## Signature

```php
function _openid_math_cmp($x, $y)
```

## Documentation

```text
Calls the cmp function from the available math library for OpenID.
```

## Code

```php
function _openid_math_cmp($x, $y) {
  $library = _openid_get_math_library();
  switch ($library) {
    case 'gmp':
      return gmp_cmp($x, $y);
    case 'bcmath':
      return bccomp($x, $y);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
