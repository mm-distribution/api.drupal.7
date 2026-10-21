# xmlrpc_server_method_signature()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 364–378 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L364-L378)

## Signature

```php
function xmlrpc_server_method_signature($methodname)
```

## Documentation

```text
Returns one method signature for a function.

This is the function mapped to the XML-RPC method system.methodSignature.

A method signature is an array of the input and output types of a method. For
instance, the method signature of this function is array('array', 'string'),
because it takes an array and returns a string.

@param string $methodname
  Name of method to return a method signature for.

@return array
  An array of arrays of types, each of the arrays representing one method
  signature of the function that $methodname maps to.
```

## Code

```php
function xmlrpc_server_method_signature($methodname) {
  $xmlrpc_server = xmlrpc_server_get();
  if (!isset($xmlrpc_server->callbacks[$methodname])) {
    return xmlrpc_error(-32601, t('Server error. Requested method @methodname not specified.', array("@methodname" => $methodname)));
  }
  if (!is_array($xmlrpc_server->signatures[$methodname])) {
    return xmlrpc_error(-32601, t('Server error. Requested method @methodname signature not specified.', array("@methodname" => $methodname)));
  }
  // We array of types
  $return = array();
  foreach ($xmlrpc_server->signatures[$methodname] as $type) {
    $return[] = $type;
  }
  return array($return);
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
