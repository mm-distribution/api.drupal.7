# rdf_rdfa_attributes()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 307–334 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L307-L334)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)

## Signature

```php
function rdf_rdfa_attributes($mapping, $data = NULL)
```

## Documentation

```text
Builds an array of RDFa attributes for a given mapping. This array will
typically be passed through drupal_attributes() to create the attributes
variables that are available to template files. These include $attributes,
$title_attributes, $content_attributes and the field-specific
$item_attributes variables. For more information, see
theme_rdf_template_variable_wrapper().

@param $mapping
  An array containing a mandatory 'predicates' key and optional 'datatype',
  'callback' and 'type' keys. For example:
  @code
    array(
      'predicates' => array('dc:created'),
      'datatype' => 'xsd:dateTime',
      'callback' => 'date_iso8601',
      ),
    );
  @endcode
@param $data
  A value that needs to be converted by the provided callback function.

@return
  An array containing RDFa attributes suitable for drupal_attributes().
```

## Code

```php
function rdf_rdfa_attributes($mapping, $data = NULL) {
  // The type of mapping defaults to 'property'.
  $type = isset($mapping['type']) ? $mapping['type'] : 'property';

  switch ($type) {
    // The mapping expresses the relationship between two resources.
    case 'rel':
    case 'rev':
      $attributes[$type] = $mapping['predicates'];
      break;

    // The mapping expresses the relationship between a resource and some
    // literal text.
    case 'property':
      $attributes['property'] = $mapping['predicates'];
      // Convert $data to a specific format as per the callback function.
      if (isset($data) && isset($mapping['callback']) && function_exists($mapping['callback'])) {
        $callback = $mapping['callback'];
        $attributes['content'] = $callback($data);
      }
      if (isset($mapping['datatype'])) {
        $attributes['datatype'] = $mapping['datatype'];
      }
      break;
  }

  return $attributes;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
