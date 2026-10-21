# openid_openid_discovery_method_info()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 441–450 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L441-L450)
- **Module/theme:** openid
- **Implements:** [hook_openid_discovery_method_info()](../openid.api.php/hook_openid_discovery_method_info.md)

## Signature

```php
function openid_openid_discovery_method_info()
```

## Documentation

```text
Implements hook_openid_discovery_method_info().

Define standard discovery methods.
```

## Code

```php
function openid_openid_discovery_method_info() {
  // The discovery process will stop as soon as one discovery method succeed.
  // We first attempt to discover XRI-based identifiers, then standard XRDS
  // identifiers via Yadis and HTML-based discovery, conforming to the OpenID 2.0
  // specification.
  return array(
    'xri' => '_openid_xri_discovery',
    'xrds' => '_openid_xrds_discovery',
  );
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
