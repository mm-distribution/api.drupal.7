# TaxonomyVocabularyTestCase::testTaxonomyVocabularyLoadMultiple()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 303–346 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L303-L346)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyLoadMultiple()
```

## Documentation

```text
Tests for loading multiple vocabularies.
```

## Code

```php
  function testTaxonomyVocabularyLoadMultiple() {

    // Delete any existing vocabularies.
    foreach (taxonomy_get_vocabularies() as $vocabulary) {
      taxonomy_vocabulary_delete($vocabulary->vid);
    }

    // Create some vocabularies and assign weights.
    $vocabulary1 = $this->createVocabulary();
    $vocabulary1->weight = 0;
    taxonomy_vocabulary_save($vocabulary1);
    $vocabulary2 = $this->createVocabulary();
    $vocabulary2->weight = 1;
    taxonomy_vocabulary_save($vocabulary2);
    $vocabulary3 = $this->createVocabulary();
    $vocabulary3->weight = 2;
    taxonomy_vocabulary_save($vocabulary3);

    // Fetch the names for all vocabularies, confirm that they are keyed by
    // machine name.
    $names = taxonomy_vocabulary_get_names();
    $this->assertEqual($names[$vocabulary1->machine_name]->name, $vocabulary1->name, 'Vocabulary 1 name found.');

    // Fetch all of the vocabularies using taxonomy_get_vocabularies().
    // Confirm that the vocabularies are ordered by weight.
    $vocabularies = taxonomy_get_vocabularies();
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary1->vid, 'Vocabulary was found in the vocabularies array.');
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary2->vid, 'Vocabulary was found in the vocabularies array.');
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary3->vid, 'Vocabulary was found in the vocabularies array.');

    // Fetch the vocabularies with taxonomy_vocabulary_load_multiple(), specifying IDs.
    // Ensure they are returned in the same order as the original array.
    $vocabularies = taxonomy_vocabulary_load_multiple(array($vocabulary3->vid, $vocabulary2->vid, $vocabulary1->vid));
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary3->vid, 'Vocabulary loaded successfully by ID.');
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary2->vid, 'Vocabulary loaded successfully by ID.');
    $this->assertEqual(array_shift($vocabularies)->vid, $vocabulary1->vid, 'Vocabulary loaded successfully by ID.');

    // Fetch vocabulary 1 by name.
    $vocabulary = current(taxonomy_vocabulary_load_multiple(array(), array('name' => $vocabulary1->name)));
    $this->assertEqual($vocabulary->vid, $vocabulary1->vid, 'Vocabulary loaded successfully by name.');

    // Fetch vocabulary 1 by name and ID.
    $this->assertEqual(current(taxonomy_vocabulary_load_multiple(array($vocabulary1->vid), array('name' => $vocabulary1->name)))->vid, $vocabulary1->vid, 'Vocabulary loaded successfully by name and ID.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
