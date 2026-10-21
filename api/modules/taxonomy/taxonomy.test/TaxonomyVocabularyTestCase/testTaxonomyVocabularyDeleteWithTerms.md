# TaxonomyVocabularyTestCase::testTaxonomyVocabularyDeleteWithTerms()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 244–273 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L244-L273)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyDeleteWithTerms()
```

## Documentation

```text
Test deleting a taxonomy that contains terms.
```

## Code

```php
  function testTaxonomyVocabularyDeleteWithTerms() {
    // Delete any existing vocabularies.
    foreach (taxonomy_get_vocabularies() as $vocabulary) {
      taxonomy_vocabulary_delete($vocabulary->vid);
    }

    // Assert that there are no terms left.
    $this->assertEqual(0, db_query('SELECT COUNT(*) FROM {taxonomy_term_data}')->fetchField());

    // Create a new vocabulary and add a few terms to it.
    $vocabulary = $this->createVocabulary();
    $terms = array();
    for ($i = 0; $i < 5; $i++) {
      $terms[$i] = $this->createTerm($vocabulary);
    }

    // Set up hierarchy. term 2 is a child of 1 and 4 a child of 1 and 2.
    $terms[2]->parent = array($terms[1]->tid);
    taxonomy_term_save($terms[2]);
    $terms[4]->parent = array($terms[1]->tid, $terms[2]->tid);
    taxonomy_term_save($terms[4]);

    // Assert that there are now 5 terms.
    $this->assertEqual(5, db_query('SELECT COUNT(*) FROM {taxonomy_term_data}')->fetchField());

    taxonomy_vocabulary_delete($vocabulary->vid);

    // Assert that there are no terms left.
    $this->assertEqual(0, db_query('SELECT COUNT(*) FROM {taxonomy_term_data}')->fetchField());
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
