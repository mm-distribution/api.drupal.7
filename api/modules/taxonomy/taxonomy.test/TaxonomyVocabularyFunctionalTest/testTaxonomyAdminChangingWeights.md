# TaxonomyVocabularyFunctionalTest::testTaxonomyAdminChangingWeights()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 120–143 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L120-L143)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyAdminChangingWeights()
```

## Documentation

```text
Changing weights on the vocabulary overview with two or more vocabularies.
```

## Code

```php
  function testTaxonomyAdminChangingWeights() {
    // Create some vocabularies.
    for ($i = 0; $i < 10; $i++) {
      $this->createVocabulary();
    }
    // Get all vocabularies and change their weights.
    $vocabularies = taxonomy_get_vocabularies();
    $edit = array();
    foreach ($vocabularies as $key => $vocabulary) {
      $vocabulary->weight = -$vocabulary->weight;
      $vocabularies[$key]->weight = $vocabulary->weight;
      $edit[$key . '[weight]'] = $vocabulary->weight;
    }
    // Saving the new weights via the interface.
    $this->drupalPost('admin/structure/taxonomy', $edit, t('Save'));

    // Load the vocabularies from the database.
    $new_vocabularies = taxonomy_get_vocabularies();

    // Check that the weights are saved in the database correctly.
    foreach ($vocabularies as $key => $vocabulary) {
      $this->assertEqual($new_vocabularies[$key]->weight, $vocabularies[$key]->weight, 'The vocabulary weight was changed.');
    }
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
