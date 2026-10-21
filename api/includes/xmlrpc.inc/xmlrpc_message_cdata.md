# xmlrpc_message_cdata()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 294–298 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L294-L298)

## Signature

```php
function xmlrpc_message_cdata($parser, $cdata)
```

## Documentation

```text
Handles character data for XML parsing in xmlrpc_message_parse().
```

## Code

```php
function xmlrpc_message_cdata($parser, $cdata) {
  $xmlrpc_message = xmlrpc_message_get();
  $xmlrpc_message->current_tag_contents .= $cdata;
  xmlrpc_message_set($xmlrpc_message);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
