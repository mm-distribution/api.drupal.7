# drupal_get_rdf_namespaces()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 269–279 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L269-L279)

## Signature

```php
function drupal_get_rdf_namespaces()
```

## Documentation

```text
Returns a string containing RDF namespace declarations for use in XML and
XHTML output.
```

## Code

```php
function drupal_get_rdf_namespaces() {
  $xml_rdf_namespaces = array();

  // Serializes the RDF namespaces in XML namespace syntax.
  if (function_exists('rdf_get_namespaces')) {
    foreach (rdf_get_namespaces() as $prefix => $uri) {
      $xml_rdf_namespaces[] = 'xmlns:' . $prefix . '="' . $uri . '"';
    }
  }
  return count($xml_rdf_namespaces) ? "\n  " . implode("\n  ", $xml_rdf_namespaces) : '';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
