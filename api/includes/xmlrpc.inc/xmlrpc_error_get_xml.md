# xmlrpc_error_get_xml()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 461–481 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L461-L481)

## Signature

```php
function xmlrpc_error_get_xml($xmlrpc_error)
```

## Documentation

```text
Converts an XML-RPC error object into XML.

@param $xmlrpc_error
  The XML-RPC error object.

@return string
  An XML representation of the error as an XML methodResponse.
```

## Code

```php
function xmlrpc_error_get_xml($xmlrpc_error) {
  return <<<EOD
<methodResponse>
  <fault>
  <value>
    <struct>
    <member>
      <name>faultCode</name>
      <value><int>{$xmlrpc_error->code}</int></value>
    </member>
    <member>
      <name>faultString</name>
      <value><string>{$xmlrpc_error->message}</string></value>
    </member>
    </struct>
  </value>
  </fault>
</methodResponse>

EOD;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
