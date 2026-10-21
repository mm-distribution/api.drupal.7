# xmlrpc_base64()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 540–545 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L540-L545)

## Signature

```php
function xmlrpc_base64($data)
```

## Documentation

```text
Returns an XML-RPC base 64 object.

@param $data
  Base 64 data to store in returned object.

@return object
  An XML-RPC base 64 object.
```

## Code

```php
function xmlrpc_base64($data) {
  $xmlrpc_base64 = new stdClass();
  $xmlrpc_base64->is_base64 = TRUE;
  $xmlrpc_base64->data = $data;
  return $xmlrpc_base64;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
