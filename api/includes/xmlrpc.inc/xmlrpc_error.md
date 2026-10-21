# xmlrpc_error()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 438–450 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L438-L450)

## Signature

```php
function xmlrpc_error($code = NULL, $message = NULL, $reset = FALSE)
```

## Documentation

```text
Generates, temporarily saves, and returns an XML-RPC error object.

@param $code
  The error code.
@param $message
  The error message.
@param $reset
  TRUE to empty the temporary error storage. Ignored if $code is supplied.

@return object
  An XML-RPC error object representing $code and $message, or the most
  recently stored error object if omitted.
```

## Code

```php
function xmlrpc_error($code = NULL, $message = NULL, $reset = FALSE) {
  static $xmlrpc_error;
  if (isset($code)) {
    $xmlrpc_error = new stdClass();
    $xmlrpc_error->is_error = TRUE;
    $xmlrpc_error->code = $code;
    $xmlrpc_error->message = $message;
  }
  elseif ($reset) {
    $xmlrpc_error = NULL;
  }
  return $xmlrpc_error;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
