# TaxonomyVocabularyTestCase::testTaxonomyVocabularyLoadReturnFalse()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 224–239 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L224-L239)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyLoadReturnFalse()
```

## Documentation

```text
Ensure that when an invalid vocabulary vid is loaded, it is possible
to load the same vid successfully if it subsequently becomes valid.
```

## Code

```php
  function testTaxonomyVocabularyLoadReturnFalse() {
    // Load a vocabulary that doesn't exist.
    $vocabularies = taxonomy_get_vocabularies();
    $vid = count($vocabularies) + 1;
    $vocabulary = taxonomy_vocabulary_load($vid);
    // This should not return an object because no such vocabulary exists.
    $this->assertTrue(empty($vocabulary), 'No object loaded.');

    // Create a new vocabulary.
    $this->createVocabulary();
    // Load the vocabulary with the same $vid from earlier.
    // This should return a vocabulary object since it now matches a real vid.
    $vocabulary = taxonomy_vocabulary_load($vid);
    $this->assertTrue(!empty($vocabulary) && is_object($vocabulary), 'Vocabulary is an object.');
    $this->assertEqual($vocabulary->vid, $vid, 'Valid vocabulary vid is the same as our previously invalid one.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
