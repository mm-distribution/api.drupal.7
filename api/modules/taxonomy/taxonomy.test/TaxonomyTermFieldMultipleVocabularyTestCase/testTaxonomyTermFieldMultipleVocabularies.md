# TaxonomyTermFieldMultipleVocabularyTestCase::testTaxonomyTermFieldMultipleVocabularies()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1778–1832 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1778-L1832)
- **Class:** [TaxonomyTermFieldMultipleVocabularyTestCase](../TaxonomyTermFieldMultipleVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermFieldMultipleVocabularies()
```

## Documentation

```text
Tests term reference field and widget with multiple vocabularies.
```

## Code

```php
  function testTaxonomyTermFieldMultipleVocabularies() {
    // Create a term in each vocabulary.
    $term1 = $this->createTerm($this->vocabulary1);
    $term2 = $this->createTerm($this->vocabulary2);

    // Submit an entity with both terms.
    $langcode = LANGUAGE_NONE;
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][]", '', 'Widget is displayed.');
    $edit = array(
      "{$this->field_name}[$langcode][]" => array($term1->tid, $term2->tid),
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created.');

    // Render the entity.
    $entity = field_test_entity_test_load($id);
    $entities = array($id => $entity);
    field_attach_prepare_view('test_entity', $entities, 'full');
    $entity->content = field_attach_view('test_entity', $entity, 'full');
    $this->content = drupal_render($entity->content);
    $this->assertText($term1->name, 'Term 1 name is displayed.');
    $this->assertText($term2->name, 'Term 2 name is displayed.');

    // Delete vocabulary 2.
    taxonomy_vocabulary_delete($this->vocabulary2->vid);

    // Re-render the content.
    $entity = field_test_entity_test_load($id);
    $entities = array($id => $entity);
    field_attach_prepare_view('test_entity', $entities, 'full');
    $entity->content = field_attach_view('test_entity', $entity, 'full');
    $this->plainTextContent = FALSE;
    $this->content = drupal_render($entity->content);

    // Term 1 should still be displayed; term 2 should not be.
    $this->assertText($term1->name, 'Term 1 name is displayed.');
    $this->assertNoText($term2->name, 'Term 2 name is not displayed.');

    // Verify that field and instance settings are correct.
    $field_info = field_info_field($this->field_name);
    $this->assertEqual(sizeof($field_info['settings']['allowed_values']), 1, 'Only one vocabulary is allowed for the field.');

    // The widget should still be displayed.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][]", '', 'Widget is still displayed.');

    // Term 1 should still pass validation.
    $edit = array(
      "{$this->field_name}[$langcode][]" => array($term1->tid),
    );
    $this->drupalPost(NULL, $edit, t('Save'));
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
