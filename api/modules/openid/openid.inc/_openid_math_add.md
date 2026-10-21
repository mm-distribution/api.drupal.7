# _openid_math_add()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 740–748 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L740-L748)
- **Module/theme:** openid

## Signature

```php
function _openid_math_add($x, $y)
```

## Documentation

```text
Calls the add function from the available math library for OpenID.
```

## Code

```php
function _openid_math_add($x, $y) {
  $library = _openid_get_math_library();
  switch ($library) {
    case 'gmp':
      return gmp_strval(gmp_add($x, $y));
    case 'bcmath':
      return bcadd($x, $y);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
