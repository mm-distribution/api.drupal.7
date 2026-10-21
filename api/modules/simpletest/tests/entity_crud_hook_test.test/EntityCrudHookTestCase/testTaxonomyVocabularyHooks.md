# EntityCrudHookTestCase::testTaxonomyVocabularyHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 259–294 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L259-L294)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTaxonomyVocabularyHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on taxonomy vocabularies.
```

## Code

```php
  public function testTaxonomyVocabularyHooks() {
    $vocabulary = (object) array(
      'name' => 'Test vocabulary',
      'machine_name' => 'test',
      'description' => NULL,
      'module' => 'entity_crud_hook_test',
    );
    $_SESSION['entity_crud_hook_test'] = array();
    taxonomy_vocabulary_save($vocabulary);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $vocabulary = taxonomy_vocabulary_load($vocabulary->vid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $vocabulary->name = 'New name';
    taxonomy_vocabulary_save($vocabulary);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    taxonomy_vocabulary_delete($vocabulary->vid);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type taxonomy_vocabulary');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_vocabulary_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
