# hook_openid_response()

- **Type:** Hook (documentation function)
- **File:** [`modules/openid/openid.api.php`](_file.md), lines 42–46 · [local source](../../../../source/modules/openid/openid.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php#L42-L46)
- **Module/theme:** openid
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_openid_response($response, $account)
```

## Documentation

```text
Allow modules to act upon a successful OpenID login.

@param $response
  Response values from the OpenID Provider.
@param $account
  The Drupal user account that logged in
```

## Code

```php
function hook_openid_response($response, $account) {
  if (isset($response['openid.ns.ax'])) {
    _mymodule_store_ax_fields($response, $account);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_openid_response()".

_None found._

---
_Drupal 7.103 · [modules/openid/openid.api.php](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
