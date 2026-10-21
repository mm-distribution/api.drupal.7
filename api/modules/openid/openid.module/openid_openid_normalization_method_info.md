# openid_openid_normalization_method_info()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 579–587 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L579-L587)
- **Module/theme:** openid
- **Implements:** [hook_openid_normalization_method_info()](../openid.api.php/hook_openid_normalization_method_info.md)

## Signature

```php
function openid_openid_normalization_method_info()
```

## Documentation

```text
Implements hook_openid_normalization_method_info().

Define standard normalization methods.
```

## Code

```php
function openid_openid_normalization_method_info() {
  // OpenID Authentication 2.0, section 7.2:
  // If the User-supplied Identifier looks like an XRI, treat it as such;
  // otherwise treat it as an HTTP URL.
  return array(
    'xri' => '_openid_xri_normalize',
    'url' => '_openid_url_normalize',
  );
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
