# xmlrpc_server_multicall()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 265–302 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L265-L302)

## Signature

```php
function xmlrpc_server_multicall($methodcalls)
```

## Documentation

```text
Dispatches multiple XML-RPC requests.

@param array $methodcalls
  An array of XML-RPC requests to make. Each request is an array with the
  following elements:
  - methodName: Name of the method to invoke.
  - params: Parameters to pass to the method.

@return
  An array of the results of each request.

@see xmlrpc_server_call()
```

## Code

```php
function xmlrpc_server_multicall($methodcalls) {
  // See http://www.xmlrpc.com/discuss/msgReader$1208
  // To avoid multicall expansion attacks, limit the number of duplicate method
  // calls allowed with a default of 1. Set to -1 for unlimited.
  $duplicate_method_limit = variable_get('xmlrpc_multicall_duplicate_method_limit', 1);
  $method_count = array();
  $return = array();
  $xmlrpc_server = xmlrpc_server_get();
  foreach ($methodcalls as $call) {
    $ok = TRUE;
    if (!isset($call['methodName']) || !isset($call['params'])) {
      $result = xmlrpc_error(3, t('Invalid syntax for system.multicall.'));
      $ok = FALSE;
    }
    $method = $call['methodName'];
    $method_count[$method] = isset($method_count[$method]) ? $method_count[$method] + 1 : 1;
    $params = $call['params'];
    if ($method == 'system.multicall') {
      $result = xmlrpc_error(-32600, t('Recursive calls to system.multicall are forbidden.'));
    }
    elseif ($duplicate_method_limit > 0 && $method_count[$method] > $duplicate_method_limit) {
      $result = xmlrpc_error(-156579, t('Too many duplicate method calls in system.multicall.'));
    }
    elseif ($ok) {
      $result = xmlrpc_server_call($xmlrpc_server, $method, $params);
    }
    if (is_object($result) && !empty($result->is_error)) {
      $return[] = array(
        'faultCode' => $result->code,
        'faultString' => $result->message,
      );
    }
    else {
      $return[] = array($result);
    }
  }
  return $return;
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
