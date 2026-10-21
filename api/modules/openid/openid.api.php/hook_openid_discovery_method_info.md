# hook_openid_discovery_method_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/openid/openid.api.php`](_file.md), lines 69–73 · [local source](../../../../source/modules/openid/openid.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php#L69-L73)
- **Module/theme:** openid
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_openid_discovery_method_info()
```

## Documentation

```text
Allow modules to declare OpenID discovery methods.

The discovery function callbacks will be called in turn with an unique
parameter, the claimed identifier. They have to return an associative array
with array of services and claimed identifier in the same form as returned by
openid_discover(). The resulting array must contain following keys:
  - 'services' (required) an array of discovered services (including OpenID
  version, endpoint URI, etc).
  - 'claimed_id' (optional) new claimed identifer, found by following HTTP
  redirects during the services discovery.

The first discovery method that succeed (return at least one services) will
stop the discovery process.

@return
  An associative array which keys are the name of the discovery methods and
  values are function callbacks.

@see hook_openid_discovery_method_info_alter()
```

## Code

```php
function hook_openid_discovery_method_info() {
  return array(
    'new_discovery_idea' => '_my_discovery_method',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_openid_discovery_method_info()".

- [openid_openid_discovery_method_info()](../openid.module/openid_openid_discovery_method_info.md) — `modules/openid/openid.module`

---
_Drupal 7.103 · [modules/openid/openid.api.php](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
