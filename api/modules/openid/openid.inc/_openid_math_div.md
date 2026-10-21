# _openid_math_div()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 766–774 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L766-L774)
- **Module/theme:** openid

## Signature

```php
function _openid_math_div($x, $y)
```

## Documentation

```text
Calls the div function from the available math library for OpenID.
```

## Code

```php
function _openid_math_div($x, $y) {
  $library = _openid_get_math_library();
  switch ($library) {
    case 'gmp':
      return gmp_div($x, $y);
    case 'bcmath':
      return bcdiv($x, $y);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
