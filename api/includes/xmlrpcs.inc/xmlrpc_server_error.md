# xmlrpc_server_error()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 113–118 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L113-L118)

## Signature

```php
function xmlrpc_server_error($error, $message = FALSE)
```

## Documentation

```text
Throws an XML-RPC error.

@param $error
  An error object or integer error code.
@param $message
  (optional) The description of the error. Used only if an integer error
  code was passed in.
```

## Code

```php
function xmlrpc_server_error($error, $message = FALSE) {
  if ($message && !is_object($error)) {
    $error = xmlrpc_error($error, $message);
  }
  xmlrpc_server_output(xmlrpc_error_get_xml($error));
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
