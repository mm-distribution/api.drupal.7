# xmlrpc_value_calculate_type()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 57–85 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L57-L85)

## Signature

```php
function xmlrpc_value_calculate_type($xmlrpc_value)
```

## Documentation

```text
Maps a PHP type to an XML-RPC type.

@param $xmlrpc_value
  Variable whose type should be mapped.

@return string
  The corresponding XML-RPC type.

@see http://www.xmlrpc.com/spec#scalars
```

## Code

```php
function xmlrpc_value_calculate_type($xmlrpc_value) {
  // http://www.php.net/gettype: Never use gettype() to test for a certain type
  // [...] Instead, use the is_* functions.
  if (is_bool($xmlrpc_value->data)) {
    return 'boolean';
  }
  if (is_double($xmlrpc_value->data)) {
    return 'double';
  }
  if (is_int($xmlrpc_value->data)) {
    return 'int';
  }
  if (is_array($xmlrpc_value->data)) {
    // empty or integer-indexed arrays are 'array', string-indexed arrays 'struct'
    return empty($xmlrpc_value->data) || range(0, count($xmlrpc_value->data) - 1) === array_keys($xmlrpc_value->data) ? 'array' : 'struct';
  }
  if (is_object($xmlrpc_value->data)) {
    if (isset($xmlrpc_value->data->is_date)) {
      return 'date';
    }
    if (isset($xmlrpc_value->data->is_base64)) {
      return 'base64';
    }
    $xmlrpc_value->data = get_object_vars($xmlrpc_value->data);
    return 'struct';
  }
  // default
  return 'string';
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
