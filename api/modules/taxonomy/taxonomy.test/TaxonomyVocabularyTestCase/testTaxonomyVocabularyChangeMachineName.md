# TaxonomyVocabularyTestCase::testTaxonomyVocabularyChangeMachineName()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 351–372 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L351-L372)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyChangeMachineName()
```

## Documentation

```text
Tests that machine name changes are properly reflected.
```

## Code

```php
  function testTaxonomyVocabularyChangeMachineName() {
    // Add a field instance to the vocabulary.
    $field = array(
      'field_name' => 'field_test',
      'type' => 'test_field',
    );
    field_create_field($field);
    $instance = array(
      'field_name' => 'field_test',
      'entity_type' => 'taxonomy_term',
      'bundle' => $this->vocabulary->machine_name,
    );
    field_create_instance($instance);

    // Change the machine name.
    $new_name = drupal_strtolower($this->randomName());
    $this->vocabulary->machine_name = $new_name;
    taxonomy_vocabulary_save($this->vocabulary);

    // Check that the field instance is still attached to the vocabulary.
    $this->assertTrue(field_info_instance('taxonomy_term', 'field_test', $new_name), 'The bundle name was updated correctly.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
