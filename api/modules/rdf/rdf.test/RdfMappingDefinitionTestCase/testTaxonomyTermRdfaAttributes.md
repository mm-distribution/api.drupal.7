# RdfMappingDefinitionTestCase::testTaxonomyTermRdfaAttributes()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 401–414 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L401-L414)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testTaxonomyTermRdfaAttributes()
```

## Documentation

```text
Creates a random term and ensures the right RDFa markup is used.
```

## Code

```php
  function testTaxonomyTermRdfaAttributes() {
    $vocabulary = $this->createVocabulary();
    $term = $this->createTerm($vocabulary);

    // Views the term and checks that the RDFa markup is correct.
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $term_url = url('taxonomy/term/' . $term->tid);
    $term_name = $term->name;
    $term_rdfa_meta = $this->xpath('//meta[@typeof="skos:Concept" and @about=:term-url and contains(@property, "rdfs:label") and contains(@property, "skos:prefLabel") and @content=:term-name]', array(
      ':term-url' => $term_url,
      ':term-name' => $term_name,
    ));
    $this->assertTrue(!empty($term_rdfa_meta), 'RDFa markup found on term page.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
