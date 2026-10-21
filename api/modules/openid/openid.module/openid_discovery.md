# openid_discovery()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 419–434 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L419-L434)
- **Module/theme:** openid

## Signature

```php
function openid_discovery($claimed_id)
```

## Documentation

```text
Perform discovery on a claimed ID to determine the OpenID provider endpoint.

Discovery methods are provided by the hook_openid_discovery_method_info and
could be further altered using the hook_openid_discovery_method_info_alter.

@param $claimed_id
  The OpenID URL to perform discovery on.

@return
  The resulting discovery array from the first successful discovery method,
  which must contain following keys:
  - 'services' (required) an array of discovered services (including OpenID
  version, endpoint URI, etc).
  - 'claimed_id' (optional) new claimed identifer, found by following HTTP
  redirects during the services discovery.
  If all the discovery method fails or if no appropriate discovery method is
  found, FALSE is returned.
```

## Code

```php
function openid_discovery($claimed_id) {
  module_load_include('inc', 'openid');

  $methods = module_invoke_all('openid_discovery_method_info');
  drupal_alter('openid_discovery_method_info', $methods);

  // Execute each method in turn and return first successful discovery.
  foreach ($methods as $method) {
    $discovery = $method($claimed_id);
    if (!empty($discovery)) {
      return $discovery;
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
