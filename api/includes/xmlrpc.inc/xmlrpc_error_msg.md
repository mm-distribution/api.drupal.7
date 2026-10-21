# xmlrpc_error_msg()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 646–649 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L646-L649)

## Signature

```php
function xmlrpc_error_msg()
```

## Documentation

```text
Returns the last XML-RPC client error message.
```

## Code

```php
function xmlrpc_error_msg() {
  $error = xmlrpc_error();
  return ($error != NULL ? $error->message : NULL);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
