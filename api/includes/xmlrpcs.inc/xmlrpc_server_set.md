# xmlrpc_server_set()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 146–152 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L146-L152)

## Signature

```php
function xmlrpc_server_set($xmlrpc_server = NULL)
```

## Documentation

```text
Stores a copy of an XML-RPC request temporarily.

@param object $xmlrpc_server
  (optional) Request object created by xmlrpc_server(). Omit to leave the
  previous server object saved.

@return
  The latest stored request.

@see xmlrpc_server_get()
```

## Code

```php
function xmlrpc_server_set($xmlrpc_server = NULL) {
  static $server;
  if (!isset($server)) {
    $server = $xmlrpc_server;
  }
  return $server;
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
