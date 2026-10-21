# TaxonomyVocabularyFunctionalTest::testTaxonomyAdminNoVocabularies()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 148–159 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L148-L159)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyAdminNoVocabularies()
```

## Documentation

```text
Test the vocabulary overview with no vocabularies.
```

## Code

```php
  function testTaxonomyAdminNoVocabularies() {
    // Delete all vocabularies.
    $vocabularies = taxonomy_get_vocabularies();
    foreach ($vocabularies as $key => $vocabulary) {
      taxonomy_vocabulary_delete($key);
    }
    // Confirm that no vocabularies are found in the database.
    $this->assertFalse(taxonomy_get_vocabularies(), 'No vocabularies found in the database.');
    $this->drupalGet('admin/structure/taxonomy');
    // Check the default message for no vocabularies.
    $this->assertText(t('No vocabularies available.'), 'No vocabularies were found.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
