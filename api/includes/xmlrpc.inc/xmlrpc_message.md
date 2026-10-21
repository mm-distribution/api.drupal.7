# xmlrpc_message()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 149–159 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L149-L159)

## Signature

```php
function xmlrpc_message($message)
```

## Documentation

```text
Constructs an object representing an XML-RPC message.

@param $message
  A string containing an XML message.

@return object
  An XML-RPC object containing the message.

@see http://www.xmlrpc.com/spec
```

## Code

```php
function xmlrpc_message($message) {
  $xmlrpc_message = new stdClass();
  // The stack used to keep track of the current array/struct
  $xmlrpc_message->array_structs = array();
  // The stack used to keep track of if things are structs or array
  $xmlrpc_message->array_structs_types = array();
  // A stack as well
  $xmlrpc_message->current_struct_name = array();
  $xmlrpc_message->message = $message;
  return $xmlrpc_message;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
