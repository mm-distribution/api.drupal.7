# xmlrpc_value()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 25–44 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L25-L44)

## Signature

```php
function xmlrpc_value($data, $type = FALSE)
```

## Documentation

```text
Turns a data structure into objects with 'data' and 'type' attributes.

@param $data
  The data structure.
@param $type
  Optional type to assign to $data.

@return object
  An XML-RPC data object containing the input $data.
```

## Code

```php
function xmlrpc_value($data, $type = FALSE) {
  $xmlrpc_value = new stdClass();
  $xmlrpc_value->data = $data;
  if (!$type) {
    $type = xmlrpc_value_calculate_type($xmlrpc_value);
  }
  $xmlrpc_value->type = $type;
  if ($type == 'struct') {
    // Turn all the values in the array into new xmlrpc_values
    foreach ($xmlrpc_value->data as $key => $value) {
      $xmlrpc_value->data[$key] = xmlrpc_value($value);
    }
  }
  if ($type == 'array') {
    for ($i = 0, $j = count($xmlrpc_value->data); $i < $j; $i++) {
      $xmlrpc_value->data[$i] = xmlrpc_value($xmlrpc_value->data[$i]);
    }
  }
  return $xmlrpc_value;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
