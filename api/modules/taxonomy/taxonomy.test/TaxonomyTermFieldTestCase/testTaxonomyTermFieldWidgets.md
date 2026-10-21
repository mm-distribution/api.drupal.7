# TaxonomyTermFieldTestCase::testTaxonomyTermFieldWidgets()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1616–1646 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1616-L1646)
- **Class:** [TaxonomyTermFieldTestCase](../TaxonomyTermFieldTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermFieldWidgets()
```

## Documentation

```text
Test widgets.
```

## Code

```php
  function testTaxonomyTermFieldWidgets() {
    // Create a term in the vocabulary.
    $term = $this->createTerm($this->vocabulary);

    // Display creation form.
    $langcode = LANGUAGE_NONE;
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode]", '', 'Widget is displayed.');

    // Submit with some value.
    $edit = array(
      "{$this->field_name}[$langcode]" => array($term->tid),
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created.');

    // Display the object.
    $entity = field_test_entity_test_load($id);
    $entities = array($id => $entity);
    field_attach_prepare_view('test_entity', $entities, 'full');
    $entity->content = field_attach_view('test_entity', $entity, 'full');
    $this->content = drupal_render($entity->content);
    $this->assertText($term->name, 'Term name is displayed.');

    // Delete the vocabulary and verify that the widget is gone.
    taxonomy_vocabulary_delete($this->vocabulary->vid);
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertNoFieldByName("{$this->field_name}[$langcode]", '', 'Widget is not displayed.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
