# TaxonomyTermFunctionTestCase::testTermDelete()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 422–432 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L422-L432)
- **Class:** [TaxonomyTermFunctionTestCase](../TaxonomyTermFunctionTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTermDelete()
```

## Documentation

_No docblock in source._

## Code

```php
  function testTermDelete() {
    $vocabulary = $this->createVocabulary();
    $valid_term = $this->createTerm($vocabulary);
    // Delete a valid term.
    taxonomy_term_delete($valid_term->tid);
    $terms = taxonomy_term_load_multiple(array(), array('vid' => $vocabulary->vid));
    $this->assertTrue(empty($terms), 'Vocabulary is empty after deletion.');

    // Delete an invalid term. Should not throw any notices.
    taxonomy_term_delete(42);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
