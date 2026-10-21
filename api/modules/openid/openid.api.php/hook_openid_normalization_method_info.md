# hook_openid_normalization_method_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/openid/openid.api.php`](_file.md), lines 100–104 · [local source](../../../../source/modules/openid/openid.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php#L100-L104)
- **Module/theme:** openid
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_openid_normalization_method_info()
```

## Documentation

```text
Allow modules to declare OpenID normalization methods.

The discovery function callbacks will be called in turn with an unique
parameter, the identifier to normalize. They have to return a normalized
identifier, or NULL if the identifier is not in a form they can handle.

The first normalization method that succeed (return a value that is not NULL)
will stop the normalization process.

@return
  An array with a set of function callbacks, that will be called in turn
  when normalizing an OpenID identifier. The normalization functions have
  to return a normalized identifier, or NULL if the identifier is not in
  a form they can handle.
@see hook_openid_normalization_method_info_alter()
```

## Code

```php
function hook_openid_normalization_method_info() {
  return array(
    'new_normalization_idea' => '_my_normalization_method',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_openid_normalization_method_info()".

- [openid_openid_normalization_method_info()](../openid.module/openid_openid_normalization_method_info.md) — `modules/openid/openid.module`

---
_Drupal 7.103 · [modules/openid/openid.api.php](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
