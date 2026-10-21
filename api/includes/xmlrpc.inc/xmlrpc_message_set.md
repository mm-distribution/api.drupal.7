# xmlrpc_message_set()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 243–249 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L243-L249)

## Signature

```php
function xmlrpc_message_set($value = NULL)
```

## Documentation

```text
Stores a copy of the most recent XML-RPC message object temporarily.

@param $value
  An XML-RPC message to store, or NULL to keep the last message.

@return object
  The most recently stored message.

@see xmlrpc_message_get()
```

## Code

```php
function xmlrpc_message_set($value = NULL) {
  static $xmlrpc_message;
  if ($value) {
    $xmlrpc_message = $value;
  }
  return $xmlrpc_message;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
