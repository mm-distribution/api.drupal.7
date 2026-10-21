# xmlrpc_server_call()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 180–249 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L180-L249)

## Signature

```php
function xmlrpc_server_call($xmlrpc_server, $methodname, $args)
```

## Documentation

```text
Dispatches an XML-RPC request and any parameters to the appropriate handler.

@param object $xmlrpc_server
  Object containing information about this XML-RPC server, the methods it
  provides, their signatures, etc.
@param string $methodname
  The external XML-RPC method name; e.g., 'system.methodHelp'.
@param array $args
  Array containing any parameters that are to be sent along with the request.

@return
  The results of the call.
```

## Code

```php
function xmlrpc_server_call($xmlrpc_server, $methodname, $args) {
  // Make sure parameters are in an array
  if ($args && !is_array($args)) {
    $args = array($args);
  }
  // Has this method been mapped to a Drupal function by us or by modules?
  if (!isset($xmlrpc_server->callbacks[$methodname])) {
    return xmlrpc_error(-32601, t('Server error. Requested method @methodname not specified.', array("@methodname" => $xmlrpc_server->message->methodname)));
  }
  $method = $xmlrpc_server->callbacks[$methodname];
  $signature = $xmlrpc_server->signatures[$methodname];

  // If the method has a signature, validate the request against the signature
  if (is_array($signature)) {
    $ok = TRUE;
    $return_type = array_shift($signature);
    // Check the number of arguments
    if (count($args) != count($signature)) {
      return xmlrpc_error(-32602, t('Server error. Wrong number of method parameters.'));
    }
    // Check the argument types
    foreach ($signature as $key => $type) {
      $arg = $args[$key];
      switch ($type) {
        case 'int':
        case 'i4':
          if (is_array($arg) || !is_int($arg)) {
            $ok = FALSE;
          }
          break;

        case 'base64':
        case 'string':
          if (!is_string($arg)) {
            $ok = FALSE;
          }
          break;

        case 'boolean':
          if ($arg !== FALSE && $arg !== TRUE) {
            $ok = FALSE;
          }
          break;

        case 'float':
        case 'double':
          if (!is_float($arg)) {
            $ok = FALSE;
          }
          break;

        case 'date':
        case 'dateTime.iso8601':
          if (!$arg->is_date) {
            $ok = FALSE;
          }
          break;
      }
      if (!$ok) {
        return xmlrpc_error(-32602, t('Server error. Invalid method parameters.'));
      }
    }
  }

  if (!function_exists($method)) {
    return xmlrpc_error(-32601, t('Server error. Requested function @method does not exist.', array("@method" => $method)));
  }
  // Call the mapped function
  return call_user_func_array($method, $args);
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
