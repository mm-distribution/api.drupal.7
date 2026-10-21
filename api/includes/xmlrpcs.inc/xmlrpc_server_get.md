# xmlrpc_server_get()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 162–164 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L162-L164)

## Signature

```php
function xmlrpc_server_get()
```

## Documentation

```text
Retrieves the latest stored XML-RPC request.

@return object
  The stored request.

@see xmlrpc_server_set()
```

## Code

```php
function xmlrpc_server_get() {
  return xmlrpc_server_set();
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
