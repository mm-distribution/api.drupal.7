# hook_xmlrpc_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2468–2483 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2468-L2483)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_xmlrpc_alter(&$methods)
```

## Documentation

```text
Alters the definition of XML-RPC methods before they are called.

This hook allows modules to modify the callback definition of declared
XML-RPC methods, right before they are invoked by a client. Methods may be
added, or existing methods may be altered.

Note that hook_xmlrpc() supports two distinct and incompatible formats to
define a callback, so care must be taken when altering other methods.

@param $methods
  An asssociative array of method callback definitions, as returned from
  hook_xmlrpc() implementations.

@see hook_xmlrpc()
@see xmlrpc_server()
```

## Code

```php
function hook_xmlrpc_alter(&$methods) {
  // Directly change a simple method.
  $methods['drupal.login'] = 'mymodule_login';

  // Alter complex definitions.
  foreach ($methods as $key => &$method) {
    // Skip simple method definitions.
    if (!is_int($key)) {
      continue;
    }
    // Perform the wanted manipulation.
    if ($method[0] == 'drupal.site.ping') {
      $method[1] = 'mymodule_directory_ping';
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_xmlrpc_alter()".

- [xmlrpc_test_xmlrpc_alter()](../../simpletest/tests/xmlrpc_test.module/xmlrpc_test_xmlrpc_alter.md) — `modules/simpletest/tests/xmlrpc_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
