# TaxonomyVocabularyFunctionalTest::testTaxonomyAdminDeletingVocabulary()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 164–192 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L164-L192)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyAdminDeletingVocabulary()
```

## Documentation

```text
Deleting a vocabulary.
```

## Code

```php
  function testTaxonomyAdminDeletingVocabulary() {
    // Create a vocabulary.
    $edit = array(
      'name' => $this->randomName(),
      'machine_name' => drupal_strtolower($this->randomName()),
    );
    $this->drupalPost('admin/structure/taxonomy/add', $edit, t('Save'));
    $this->assertText(t('Created new vocabulary'), 'New vocabulary was created.');

    // Check the created vocabulary.
    $vocabularies = taxonomy_get_vocabularies();
    $vocabularies_keys = array_keys($vocabularies);
    $vid = $vocabularies[end($vocabularies_keys)]->vid;
    entity_get_controller('taxonomy_vocabulary')->resetCache();
    $vocabulary = taxonomy_vocabulary_load($vid);
    $this->assertTrue($vocabulary, 'Vocabulary found in database.');

    // Delete the vocabulary.
    $edit = array();
    $this->drupalPost('admin/structure/taxonomy/' . $vocabulary->machine_name . '/edit', $edit, t('Delete'));
    $this->assertRaw(t('Are you sure you want to delete the vocabulary %name?', array('%name' => $vocabulary->name)), '[confirm deletion] Asks for confirmation.');
    $this->assertText(t('Deleting a vocabulary will delete all the terms in it. This action cannot be undone.'), '[confirm deletion] Inform that all terms will be deleted.');

    // Confirm deletion.
    $this->drupalPost(NULL, NULL, t('Delete'));
    $this->assertRaw(t('Deleted vocabulary %name.', array('%name' => $vocabulary->name)), 'Vocabulary deleted.');
    entity_get_controller('taxonomy_vocabulary')->resetCache();
    $this->assertFalse(taxonomy_vocabulary_load($vid), 'Vocabulary is not found in the database.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
