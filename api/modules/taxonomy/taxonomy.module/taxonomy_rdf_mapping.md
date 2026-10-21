# taxonomy_rdf_mapping()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1840–1877 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1840-L1877)
- **Module/theme:** taxonomy
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function taxonomy_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().

@return array
  The rdf mapping for vocabularies and terms.
```

## Code

```php
function taxonomy_rdf_mapping() {
  return array(
    array(
      'type' => 'taxonomy_term',
      'bundle' => RDF_DEFAULT_BUNDLE,
      'mapping' => array(
        'rdftype' => array('skos:Concept'),
        'name'   => array(
          'predicates' => array('rdfs:label', 'skos:prefLabel'),
        ),
        'description'   => array(
          'predicates' => array('skos:definition'),
        ),
        'vid'   => array(
          'predicates' => array('skos:inScheme'),
          'type' => 'rel',
        ),
        'parent'   => array(
          'predicates' => array('skos:broader'),
          'type' => 'rel',
        ),
      ),
    ),
    array(
      'type' => 'taxonomy_vocabulary',
      'bundle' => RDF_DEFAULT_BUNDLE,
      'mapping' => array(
        'rdftype' => array('skos:ConceptScheme'),
        'name'   => array(
          'predicates' => array('dc:title'),
        ),
        'description'   => array(
          'predicates' => array('rdfs:comment'),
        ),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
