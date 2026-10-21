# rdf_help()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 11–19 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L11-L19)
- **Module/theme:** rdf
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function rdf_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function rdf_help($path, $arg) {
  switch ($path) {
    case 'admin/help#rdf':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The RDF module enriches your content with metadata to let other applications (e.g., search engines, aggregators, and so on) better understand its relationships and attributes. This semantically enriched, machine-readable output for Drupal sites uses the <a href="@rdfa">RDFa specification</a> which allows RDF data to be embedded in HTML markup. Other modules can define mappings of their data to RDF terms, and the RDF module makes this RDF data available to the theme. The core Drupal modules define RDF mappings for their data model, and the core Drupal themes output this RDF metadata information along with the human-readable visual information. For more information, see the online handbook entry for <a href="@rdf">RDF module</a>.', array('@rdfa' => 'http://www.w3.org/TR/xhtml-rdfa-primer/', '@rdf' => 'http://drupal.org/documentation/modules/rdf')) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
