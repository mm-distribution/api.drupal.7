# hook_openid()

- **Type:** Hook (documentation function)
- **File:** [`modules/openid/openid.api.php`](_file.md), lines 26–31 · [local source](../../../../source/modules/openid/openid.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php#L26-L31)
- **Module/theme:** openid
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_openid($op, $request)
```

## Documentation

```text
Allow modules to modify the OpenID request parameters.

@param $op
  The operation to be performed.
  Possible values:
  - request: Modify parameters before they are sent to the OpenID provider.
@param $request
  An associative array of parameter defaults to which to modify or append.
@return
  An associative array of parameters to be merged with the default list.
```

## Code

```php
function hook_openid($op, $request) {
  if ($op == 'request') {
    $request['openid.identity'] = 'http://myname.myopenid.com/';
  }
  return $request;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_openid()".

_None found._

---
_Drupal 7.103 · [modules/openid/openid.api.php](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
