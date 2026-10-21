# TaxonomyLoadMultipleTestCase::testTaxonomyTermMultipleLoad()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1421–1462 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1421-L1462)
- **Class:** [TaxonomyLoadMultipleTestCase](../TaxonomyLoadMultipleTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermMultipleLoad()
```

## Documentation

```text
Create a vocabulary and some taxonomy terms, ensuring they're loaded
correctly using taxonomy_term_load_multiple().
```

## Code

```php
  function testTaxonomyTermMultipleLoad() {
    // Create a vocabulary.
    $vocabulary = $this->createVocabulary();

    // Create five terms in the vocabulary.
    $i = 0;
    while ($i < 5) {
      $i++;
      $this->createTerm($vocabulary);
    }
    // Load the terms from the vocabulary.
    $terms = taxonomy_term_load_multiple(NULL, array('vid' => $vocabulary->vid));
    $count = count($terms);
    $this->assertEqual($count, 5, format_string('Correct number of terms were loaded. !count terms.', array('!count' => $count)));

    // Load the same terms again by tid.
    $terms2 = taxonomy_term_load_multiple(array_keys($terms));
    $this->assertEqual($count, count($terms2), 'Five terms were loaded by tid.');
    $this->assertEqual($terms, $terms2, 'Both arrays contain the same terms.');

    // Load the terms by tid, with a condition on vid.
    $terms3 = taxonomy_term_load_multiple(array_keys($terms2), array('vid' => $vocabulary->vid));
    $this->assertEqual($terms2, $terms3);

    // Remove one term from the array, then delete it.
    $deleted = array_shift($terms3);
    taxonomy_term_delete($deleted->tid);
    $deleted_term = taxonomy_term_load($deleted->tid);
    $this->assertFalse($deleted_term);

    // Load terms from the vocabulary by vid.
    $terms4 = taxonomy_term_load_multiple(NULL, array('vid' => $vocabulary->vid));
    $this->assertEqual(count($terms4), 4, 'Correct number of terms were loaded.');
    $this->assertFalse(isset($terms4[$deleted->tid]));

    // Create a single term and load it by name.
    $term = $this->createTerm($vocabulary);
    $loaded_terms = taxonomy_term_load_multiple(array(), array('name' => $term->name));
    $this->assertEqual(count($loaded_terms), 1, 'One term was loaded.');
    $loaded_term = reset($loaded_terms);
    $this->assertEqual($term->tid, $loaded_term->tid, 'Term loaded by name successfully.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
