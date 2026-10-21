# _openid_get_math_library()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 720–735 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L720-L735)
- **Module/theme:** openid

## Signature

```php
function _openid_get_math_library()
```

## Documentation

```text
Determine the available math library GMP vs. BCMath, favouring GMP for performance.
```

## Code

```php
function _openid_get_math_library() {
  // Not drupal_static(), because a function is not going to disappear and
  // change the output of this under any circumstances.
  static $library;

  if (empty($library)) {
    if (function_exists('gmp_add')) {
      $library =  'gmp';
    }
    elseif (function_exists('bcadd')) {
      $library = 'bcmath';
    }
  }

  return $library;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
