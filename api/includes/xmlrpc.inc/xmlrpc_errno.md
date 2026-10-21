# xmlrpc_errno()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 638–641 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L638-L641)

## Signature

```php
function xmlrpc_errno()
```

## Documentation

```text
Returns the last XML-RPC client error number.
```

## Code

```php
function xmlrpc_errno() {
  $error = xmlrpc_error();
  return ($error != NULL ? $error->code : NULL);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
