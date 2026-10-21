# xmlrpc_server_method_help()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 391–394 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L391-L394)

## Signature

```php
function xmlrpc_server_method_help($method)
```

## Documentation

```text
Returns the help for an XML-RPC method.

XML-RPC method system.methodHelp maps to this function.

@param string $method
  Name of method for which we return a help string.

@return string
  Help text for $method.
```

## Code

```php
function xmlrpc_server_method_help($method) {
  $xmlrpc_server = xmlrpc_server_get();
  return $xmlrpc_server->help[$method];
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
