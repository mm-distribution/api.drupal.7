# rdf_preprocess_taxonomy_term()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 723–736 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L723-L736)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_taxonomy_term(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_taxonomy_term(&$variables) {
  // Adds the RDF type of the term and the term name in a <meta> tag.
  $term = $variables['term'];
  $term_label_meta = array(
      '#tag' => 'meta',
      '#attributes' => array(
        'about' => url('taxonomy/term/' . $term->tid),
        'typeof' => $term->rdf_mapping['rdftype'],
        'property' => $term->rdf_mapping['name']['predicates'],
        'content' => $term->name,
      ),
    );
  drupal_add_html_head($term_label_meta, 'rdf_term_label');
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
