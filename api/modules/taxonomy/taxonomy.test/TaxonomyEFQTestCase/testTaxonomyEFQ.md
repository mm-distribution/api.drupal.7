# TaxonomyEFQTestCase::testTaxonomyEFQ()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2079–2107 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2079-L2107)
- **Class:** [TaxonomyEFQTestCase](../TaxonomyEFQTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyEFQ()
```

## Documentation

```text
Tests that a basic taxonomy EntityFieldQuery works.
```

## Code

```php
  function testTaxonomyEFQ() {
    $terms = array();
    for ($i = 0; $i < 5; $i++) {
      $term = $this->createTerm($this->vocabulary);
      $terms[$term->tid] = $term;
    }
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'taxonomy_term');
    $result = $query->execute();
    $result = $result['taxonomy_term'];
    asort($result);
    $this->assertEqual(array_keys($terms), array_keys($result), 'Taxonomy terms were retrieved by EntityFieldQuery.');

    // Create a second vocabulary and five more terms.
    $vocabulary2 = $this->createVocabulary();
    $terms2 = array();
    for ($i = 0; $i < 5; $i++) {
      $term = $this->createTerm($vocabulary2);
      $terms2[$term->tid] = $term;
    }

    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'taxonomy_term');
    $query->entityCondition('bundle', $vocabulary2->machine_name);
    $result = $query->execute();
    $result = $result['taxonomy_term'];
    asort($result);
    $this->assertEqual(array_keys($terms2), array_keys($result), format_string('Taxonomy terms from the %name vocabulary were retrieved by EntityFieldQuery.', array('%name' => $vocabulary2->name)));
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
