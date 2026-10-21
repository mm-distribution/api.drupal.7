# hook_openid_normalization_method_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/openid/openid.api.php`](_file.md), lines 109–112 · [local source](../../../../source/modules/openid/openid.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php#L109-L112)
- **Module/theme:** openid
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_openid_normalization_method_info_alter(&$methods)
```

## Documentation

```text
Allow modules to alter normalization methods.
```

## Code

```php
function hook_openid_normalization_method_info_alter(&$methods) {
  // Remove Google IDP normalization.
  unset($methods['google_idp']);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_openid_normalization_method_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/openid/openid.api.php](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
