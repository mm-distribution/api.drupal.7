# xmlrpc()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8550–8553 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8550-L8553)

## Signature

```php
function xmlrpc($url, $args, $options = array())
```

## Documentation

```text
Performs one or more XML-RPC request(s).

Usage example:
@code
$result = xmlrpc('http://example.com/xmlrpc.php', array(
  'service.methodName' => array($parameter, $second, $third),
));
@endcode

@param $url
  An absolute URL of the XML-RPC endpoint.
@param $args
  An associative array whose keys are the methods to call and whose values
  are the arguments to pass to the respective method. If multiple methods
  are specified, a system.multicall is performed.
@param $options
  (optional) An array of options to pass along to drupal_http_request().

@return
  For one request:
    Either the return value of the method on success, or FALSE.
    If FALSE is returned, see xmlrpc_errno() and xmlrpc_error_msg().
  For multiple requests:
    An array of results. Each result will either be the result
    returned by the method called, or an xmlrpc_error object if the call
    failed. See xmlrpc_error().
```

## Code

```php
function xmlrpc($url, $args, $options = array()) {
  require_once DRUPAL_ROOT . '/includes/xmlrpc.inc';
  return _xmlrpc($url, $args, $options);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
