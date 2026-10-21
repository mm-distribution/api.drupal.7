# xmlrpc_server_list_methods()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 312–315 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L312-L315)

## Signature

```php
function xmlrpc_server_list_methods()
```

## Documentation

```text
Lists the methods available on this XML-RPC server.

XML-RPC method system.listMethods maps to this function.

@return array
  Array of the names of methods available on this server.
```

## Code

```php
function xmlrpc_server_list_methods() {
  $xmlrpc_server = xmlrpc_server_get();
  return array_keys($xmlrpc_server->callbacks);
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
