# theme_rdf_metadata()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 858–872 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L858-L872)
- **Module/theme:** rdf
- **Topics:** [themeable](../../../topics/themeable.md), [rdf](../../../topics/rdf.md)

## Signature

```php
function theme_rdf_metadata($variables)
```

## Documentation

```text
Returns HTML for a series of empty spans for exporting RDF metadata in RDFa.

Sometimes it is useful to export data which is not semantically present in
the HTML output. For example, a hierarchy of comments is visible for a human
but not for machines because this hiearchy is not present in the DOM tree.
We can express it in RDFa via empty <span> tags. These aren't visible and
give machines extra information about the content and its structure.

@param $variables
  An associative array containing:
  - metadata: An array of attribute arrays. Each item in the array
    corresponds to its own set of attributes, and therefore, needs its own
    element.

@see rdf_process()
@ingroup themeable
@ingroup rdf
```

## Code

```php
function theme_rdf_metadata($variables) {
  $output = '';
  foreach ($variables['metadata'] as $attributes) {
    // Add a class so that developers viewing the HTML source can see why there
    // are empty <span> tags in the document.
    $attributes['class'][] = 'rdf-meta';
    $attributes['class'][] = 'element-hidden';
    // The XHTML+RDFa doctype allows either <span></span> or <span /> syntax to
    // be used, but for maximum browser compatibility, W3C recommends the
    // former when serving pages using the text/html media type, see
    // http://www.w3.org/TR/xhtml1/#C_3.
    $output .= '<span' . drupal_attributes($attributes) . '></span>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
