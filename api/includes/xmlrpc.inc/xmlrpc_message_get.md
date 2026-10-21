# xmlrpc_message_get()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 259–261 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L259-L261)

## Signature

```php
function xmlrpc_message_get()
```

## Documentation

```text
Returns the most recently stored XML-RPC message object.

@return object
  The most recently stored message.

@see xmlrpc_message_set()
```

## Code

```php
function xmlrpc_message_get() {
  return xmlrpc_message_set();
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
