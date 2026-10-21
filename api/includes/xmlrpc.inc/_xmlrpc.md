# _xmlrpc()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 580–633 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L580-L633)

## Signature

```php
function _xmlrpc($url, $args, $options = array())
```

## Documentation

```text
Performs one or more XML-RPC requests.

@param $url
  An absolute URL of the XML-RPC endpoint, e.g.,
  http://example.com/xmlrpc.php
@param $args
  An associative array whose keys are the methods to call and whose values
  are the arguments to pass to the respective method. If multiple methods
  are specified, a system.multicall is performed.
@param $options
  (optional) An array of options to pass along to drupal_http_request().

@return
  A single response (single request) or an array of responses (multicall
  request). Each response is the return value of the method, just as if it
  has been a local function call, on success, or FALSE on failure. If FALSE
  is returned, see xmlrpc_errno() and xmlrpc_error_msg() to get more
  information.
```

## Code

```php
function _xmlrpc($url, $args, $options = array()) {
  xmlrpc_clear_error();
  if (count($args) > 1) {
    $multicall_args = array();
    foreach ($args as $method => $call) {
      $multicall_args[] = array('methodName' => $method, 'params' => $call);
    }
    $method = 'system.multicall';
    $args = array($multicall_args);
  }
  else {
    $method = key($args);
    $args = $args[$method];
  }
  $xmlrpc_request = xmlrpc_request($method, $args);
  // Required options which will replace any that are passed in.
  $options['method'] = 'POST';
  $options['headers']['Content-Type'] = 'text/xml';
  $options['data'] = $xmlrpc_request->xml;
  $result = drupal_http_request($url, $options);
  if ($result->code != 200) {
    xmlrpc_error($result->code, $result->error);
    return FALSE;
  }
  $message = xmlrpc_message($result->data);
  // Now parse what we've got back
  if (!xmlrpc_message_parse($message)) {
    // XML error
    xmlrpc_error(-32700, t('Parse error. Not well formed'));
    return FALSE;
  }
  // Is the message a fault?
  if ($message->messagetype == 'fault') {
    xmlrpc_error($message->fault_code, $message->fault_string);
    return FALSE;
  }
  // We now know that the message is well-formed and a non-fault result.
  if ($method == 'system.multicall') {
    // Return per-method results or error objects.
    $return = array();
    foreach ($message->params[0] as $result) {
      if (array_keys($result) == array(0)) {
        $return[] = $result[0];
      }
      else {
        $return[] = xmlrpc_error($result['faultCode'], $result['faultString']);
      }
    }
  }
  else {
    $return = $message->params[0];
  }
  return $return;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
