# xmlrpc_value_get_xml()

- **Type:** Function
- **File:** [`includes/xmlrpc.inc`](_file.md), lines 96–136 · [local source](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc#L96-L136)

## Signature

```php
function xmlrpc_value_get_xml($xmlrpc_value)
```

## Documentation

```text
Generates XML representing the given value.

@param $xmlrpc_value
  A value to be represented in XML.

@return
  XML representation of $xmlrpc_value.
```

## Code

```php
function xmlrpc_value_get_xml($xmlrpc_value) {
  switch ($xmlrpc_value->type) {
    case 'boolean':
      return '<boolean>' . (($xmlrpc_value->data) ? '1' : '0') . '</boolean>';

    case 'int':
      return '<int>' . $xmlrpc_value->data . '</int>';

    case 'double':
      return '<double>' . $xmlrpc_value->data . '</double>';

    case 'string':
      // Note: we don't escape apostrophes because of the many blogging clients
      // that don't support numerical entities (and XML in general) properly.
      return '<string>' . htmlspecialchars($xmlrpc_value->data) . '</string>';

    case 'array':
      $return = '<array><data>' . "\n";
      foreach ($xmlrpc_value->data as $item) {
        $return .= '  <value>' . xmlrpc_value_get_xml($item) . "</value>\n";
      }
      $return .= '</data></array>';
      return $return;

    case 'struct':
      $return = '<struct>' . "\n";
      foreach ($xmlrpc_value->data as $name => $value) {
        $return .= "  <member><name>" . check_plain($name) . "</name><value>";
        $return .= xmlrpc_value_get_xml($value) . "</value></member>\n";
      }
      $return .= '</struct>';
      return $return;

    case 'date':
      return xmlrpc_date_get_xml($xmlrpc_value->data);

    case 'base64':
      return xmlrpc_base64_get_xml($xmlrpc_value->data);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/xmlrpc.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
