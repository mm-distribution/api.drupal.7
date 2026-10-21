# rdf_field_attach_view_alter()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 741–765 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L741-L765)
- **Module/theme:** rdf
- **Implements:** [hook_field_attach_view_alter()](../../field/field.api.php/hook_field_attach_view_alter.md)

## Signature

```php
function rdf_field_attach_view_alter(&$output, $context)
```

## Documentation

```text
Implements hook_field_attach_view_alter().
```

## Code

```php
function rdf_field_attach_view_alter(&$output, $context) {
  // Append term mappings on displayed taxonomy links.
  foreach (element_children($output) as $field_name) {
    $element = &$output[$field_name];
    if ($element['#field_type'] == 'taxonomy_term_reference' && $element['#formatter'] == 'taxonomy_term_reference_link') {
      foreach ($element['#items'] as $delta => $item) {
        // This function is invoked during entity preview when taxonomy term
        // reference items might contain free-tagging terms that do not exist
        // yet and thus have no $item['taxonomy_term'].
        if (isset($item['taxonomy_term'])) {
          $term = $item['taxonomy_term'];
          if (!empty($term->rdf_mapping['rdftype'])) {
            $element[$delta]['#options']['attributes']['typeof'] = $term->rdf_mapping['rdftype'];
          }
          if (!empty($term->rdf_mapping['name']['predicates'])) {
            // A property attribute is used with an empty datatype attribute so
            // the term name is parsed as a plain literal in RDFa 1.0 and 1.1.
            $element[$delta]['#options']['attributes']['property'] = $term->rdf_mapping['name']['predicates'];
            $element[$delta]['#options']['attributes']['datatype'] = '';
          }
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
