# xmlrpc_message_tag_close()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 303–390 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L303-L390)

## Signature

```php
function xmlrpc_message_tag_close($parser, $tag)
```

## Documentation

```text
Handles closing tags for XML parsing in xmlrpc_message_parse().
```

## Code

```php
function xmlrpc_message_tag_close($parser, $tag) {
  $xmlrpc_message = xmlrpc_message_get();
  $value_flag = FALSE;
  switch ($tag) {
    case 'int':
    case 'i4':
      $value = (int)trim($xmlrpc_message->current_tag_contents);
      $value_flag = TRUE;
      break;

    case 'double':
      $value = (double)trim($xmlrpc_message->current_tag_contents);
      $value_flag = TRUE;
      break;

    case 'string':
      $value = $xmlrpc_message->current_tag_contents;
      $value_flag = TRUE;
      break;

    case 'dateTime.iso8601':
      $value = xmlrpc_date(trim($xmlrpc_message->current_tag_contents));
      // $value = $iso->getTimestamp();
      $value_flag = TRUE;
      break;

    case 'value':
      // If no type is indicated, the type is string
      // We take special care for empty values
      if (trim($xmlrpc_message->current_tag_contents) != '' || (isset($xmlrpc_message->last_open) && ($xmlrpc_message->last_open == 'value'))) {
        $value = (string) $xmlrpc_message->current_tag_contents;
        $value_flag = TRUE;
      }
      unset($xmlrpc_message->last_open);
      break;

    case 'boolean':
      $value = (boolean)trim($xmlrpc_message->current_tag_contents);
      $value_flag = TRUE;
      break;

    case 'base64':
      $value = base64_decode(trim($xmlrpc_message->current_tag_contents));
      $value_flag = TRUE;
      break;

    // Deal with stacks of arrays and structs
    case 'data':
    case 'struct':
      $value = array_pop($xmlrpc_message->array_structs);
      array_pop($xmlrpc_message->array_structs_types);
      $value_flag = TRUE;
      break;

    case 'member':
      array_pop($xmlrpc_message->current_struct_name);
      break;

    case 'name':
      $xmlrpc_message->current_struct_name[] = trim($xmlrpc_message->current_tag_contents);
      break;

    case 'methodName':
      $xmlrpc_message->methodname = trim($xmlrpc_message->current_tag_contents);
      break;
  }
  if ($value_flag) {
    if (count($xmlrpc_message->array_structs) > 0) {
      // Add value to struct or array
      if ($xmlrpc_message->array_structs_types[count($xmlrpc_message->array_structs_types) - 1] == 'struct') {
        // Add to struct
        $xmlrpc_message->array_structs[count($xmlrpc_message->array_structs) - 1][$xmlrpc_message->current_struct_name[count($xmlrpc_message->current_struct_name) - 1]] = $value;
      }
      else {
        // Add to array
        $xmlrpc_message->array_structs[count($xmlrpc_message->array_structs) - 1][] = $value;
      }
    }
    else {
      // Just add as a parameter
      $xmlrpc_message->params[] = $value;
    }
  }
  if (!in_array($tag, array("data", "struct", "member"))) {
    $xmlrpc_message->current_tag_contents = '';
  }
  xmlrpc_message_set($xmlrpc_message);
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
