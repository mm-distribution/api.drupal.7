# xmlrpc_server()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 16–102 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L16-L102)

## Signature

```php
function xmlrpc_server($callbacks)
```

## Documentation

```text
Invokes XML-RPC methods on this server.

@param array $callbacks
  Either an associative array of external XML-RPC method names as keys with
  the callbacks they map to as values, or a more complex structure
  describing XML-RPC callbacks as returned from hook_xmlrpc().
```

## Code

```php
function xmlrpc_server($callbacks) {
  $xmlrpc_server = new stdClass();
  // Define built-in XML-RPC method names
  $defaults = array(
    'system.multicall' => 'xmlrpc_server_multicall',
    array(
      'system.methodSignature',
      'xmlrpc_server_method_signature',
      array('array', 'string'),
      'Returns an array describing the return type and required parameters of a method.',
    ),
    array(
      'system.getCapabilities',
      'xmlrpc_server_get_capabilities',
      array('struct'),
      'Returns a struct describing the XML-RPC specifications supported by this server.',
    ),
    array(
      'system.listMethods',
      'xmlrpc_server_list_methods',
      array('array'),
      'Returns an array of available methods on this server.',
    ),
    array(
      'system.methodHelp',
      'xmlrpc_server_method_help',
      array('string', 'string'),
      'Returns a documentation string for the specified method.',
    ),
  );
  // We build an array of all method names by combining the built-ins
  // with those defined by modules implementing the _xmlrpc hook.
  // Built-in methods are overridable.
  $callbacks = array_merge($defaults, (array) $callbacks);
  drupal_alter('xmlrpc', $callbacks);
  foreach ($callbacks as $key => $callback) {
    // we could check for is_array($callback)
    if (is_int($key)) {
      $method = $callback[0];
      $xmlrpc_server->callbacks[$method] = $callback[1];
      $xmlrpc_server->signatures[$method] = $callback[2];
      $xmlrpc_server->help[$method] = $callback[3];
    }
    else {
      $xmlrpc_server->callbacks[$key] = $callback;
      $xmlrpc_server->signatures[$key] = '';
      $xmlrpc_server->help[$key] = '';
    }
  }

  $data = file_get_contents('php://input');
  if (!$data) {
    print 'XML-RPC server accepts POST requests only.';
    drupal_exit();
  }
  $xmlrpc_server->message = xmlrpc_message($data);
  if (!xmlrpc_message_parse($xmlrpc_server->message)) {
    xmlrpc_server_error(-32700, t('Parse error. Request not well formed.'));
  }
  if ($xmlrpc_server->message->messagetype != 'methodCall') {
    xmlrpc_server_error(-32600, t('Server error. Invalid XML-RPC. Request must be a methodCall.'));
  }
  if (!isset($xmlrpc_server->message->params)) {
    $xmlrpc_server->message->params = array();
  }
  xmlrpc_server_set($xmlrpc_server);
  $result = xmlrpc_server_call($xmlrpc_server, $xmlrpc_server->message->methodname, $xmlrpc_server->message->params);

  if (is_object($result) && !empty($result->is_error)) {
    xmlrpc_server_error($result);
  }
  // Encode the result
  $r = xmlrpc_value($result);
  // Create the XML
  $xml = '
<methodResponse>
  <params>
  <param>
    <value>' . xmlrpc_value_get_xml($r) . '</value>
  </param>
  </params>
</methodResponse>

';
  // Send it
  xmlrpc_server_output($xml);
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
