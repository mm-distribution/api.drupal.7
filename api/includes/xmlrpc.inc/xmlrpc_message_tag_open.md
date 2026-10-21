# xmlrpc_message_tag_open()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 266–289 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L266-L289)

## Signature

```php
function xmlrpc_message_tag_open($parser, $tag, $attr)
```

## Documentation

```text
Handles opening tags for XML parsing in xmlrpc_message_parse().
```

## Code

```php
function xmlrpc_message_tag_open($parser, $tag, $attr) {
  $xmlrpc_message = xmlrpc_message_get();
  $xmlrpc_message->current_tag_contents = '';
  $xmlrpc_message->last_open = $tag;
  switch ($tag) {
    case 'methodCall':
    case 'methodResponse':
    case 'fault':
      $xmlrpc_message->messagetype = $tag;
      break;

    // Deal with stacks of arrays and structs
    case 'data':
      $xmlrpc_message->array_structs_types[] = 'array';
      $xmlrpc_message->array_structs[] = array();
      break;

    case 'struct':
      $xmlrpc_message->array_structs_types[] = 'struct';
      $xmlrpc_message->array_structs[] = array();
      break;
  }
  xmlrpc_message_set($xmlrpc_message);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
