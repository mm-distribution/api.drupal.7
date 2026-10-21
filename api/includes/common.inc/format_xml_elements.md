# format_xml_elements()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1854–1877 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1854-L1877)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_xml_elements($array)
```

## Documentation

```text
Formats XML elements.

@param $array
  An array where each item represents an element and is either a:
  - (key => value) pair (<key>value</key>)
  - Associative array with fields:
    - 'key': element name
    - 'value': element contents
    - 'attributes': associative array of element attributes
    - 'encoded': TRUE if 'value' is already encoded

In both cases, 'value' can be a simple string, or it can be another array
with the same format as $array itself for nesting.

If 'encoded' is TRUE it is up to the caller to ensure that 'value' is either
entity-encoded or CDATA-escaped. Using this option is not recommended when
working with untrusted user input, since failing to escape the data
correctly has security implications.
```

## Code

```php
function format_xml_elements($array) {
  $output = '';
  foreach ($array as $key => $value) {
    if (is_numeric($key)) {
      if ($value['key']) {
        $output .= ' <' . $value['key'];
        if (isset($value['attributes']) && is_array($value['attributes'])) {
          $output .= drupal_attributes($value['attributes']);
        }

        if (isset($value['value']) && $value['value'] != '') {
          $output .= '>' . (is_array($value['value']) ? format_xml_elements($value['value']) : (!empty($value['encoded']) ? $value['value'] : check_plain($value['value']))) . '</' . $value['key'] . ">\n";
        }
        else {
          $output .= " />\n";
        }
      }
    }
    else {
      $output .= ' <' . $key . '>' . (is_array($value) ? format_xml_elements($value) : check_plain($value)) . "</$key>\n";
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
