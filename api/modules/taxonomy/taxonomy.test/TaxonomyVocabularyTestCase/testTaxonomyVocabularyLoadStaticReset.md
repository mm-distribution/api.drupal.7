# TaxonomyVocabularyTestCase::testTaxonomyVocabularyLoadStaticReset()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 278–298 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L278-L298)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyLoadStaticReset()
```

## Documentation

```text
Ensure that the vocabulary static reset works correctly.
```

## Code

```php
  function testTaxonomyVocabularyLoadStaticReset() {
    $original_vocabulary = taxonomy_vocabulary_load($this->vocabulary->vid);
    $this->assertTrue(is_object($original_vocabulary), 'Vocabulary loaded successfully.');
    $this->assertEqual($this->vocabulary->name, $original_vocabulary->name, 'Vocabulary loaded successfully.');

    // Change the name and description.
    $vocabulary = $original_vocabulary;
    $vocabulary->name = $this->randomName();
    $vocabulary->description = $this->randomName();
    taxonomy_vocabulary_save($vocabulary);

    // Load the vocabulary.
    $new_vocabulary = taxonomy_vocabulary_load($original_vocabulary->vid);
    $this->assertEqual($new_vocabulary->name, $vocabulary->name);
    $this->assertEqual($new_vocabulary->name, $vocabulary->name);

    // Delete the vocabulary.
    taxonomy_vocabulary_delete($this->vocabulary->vid);
    $vocabularies = taxonomy_get_vocabularies();
    $this->assertTrue(!isset($vocabularies[$this->vocabulary->vid]), 'The vocabulary was deleted.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
