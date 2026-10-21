# xmlrpc_request()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 403–422 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L403-L422)

## Signature

```php
function xmlrpc_request($method, $args)
```

## Documentation

```text
Constructs an object representing an XML-RPC request.

@param $method
  The name of the method to be called.
@param $args
  An array of parameters to send with the method.

@return object
  An XML-RPC object representing the request.
```

## Code

```php
function xmlrpc_request($method, $args) {
  $xmlrpc_request = new stdClass();
  $xmlrpc_request->method = $method;
  $xmlrpc_request->args = $args;
  $xmlrpc_request->xml = <<<EOD
<?xml version="1.0"?>
<methodCall>
<methodName>{$xmlrpc_request->method}</methodName>
<params>

EOD;
  foreach ($xmlrpc_request->args as $arg) {
    $xmlrpc_request->xml .= '<param><value>';
    $v = xmlrpc_value($arg);
    $xmlrpc_request->xml .= xmlrpc_value_get_xml($v);
    $xmlrpc_request->xml .= "</value></param>\n";
  }
  $xmlrpc_request->xml .= '</params></methodCall>';
  return $xmlrpc_request;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
