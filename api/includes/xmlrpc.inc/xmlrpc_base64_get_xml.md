# xmlrpc_base64_get_xml()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 556–558 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L556-L558)

## Signature

```php
function xmlrpc_base64_get_xml($xmlrpc_base64)
```

## Documentation

```text
Converts an XML-RPC base 64 object into XML.

@param $xmlrpc_base64
  The XML-RPC base 64 object.

@return string
  An XML representation of the base 64 data as XML.
```

## Code

```php
function xmlrpc_base64_get_xml($xmlrpc_base64) {
  return '<base64>' . base64_encode($xmlrpc_base64->data) . '</base64>';
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
