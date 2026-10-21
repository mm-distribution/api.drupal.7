# EntityCrudHookTestCase::testTaxonomyTermHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 211–254 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L211-L254)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTaxonomyTermHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on taxonomy terms.
```

## Code

```php
  public function testTaxonomyTermHooks() {
    $vocabulary = (object) array(
      'name' => 'Test vocabulary',
      'machine_name' => 'test',
      'description' => NULL,
      'module' => 'entity_crud_hook_test',
    );
    taxonomy_vocabulary_save($vocabulary);

    $term = (object) array(
      'vid' => $vocabulary->vid,
      'name' => 'Test term',
      'description' => NULL,
      'format' => 1,
    );
    $_SESSION['entity_crud_hook_test'] = array();
    taxonomy_term_save($term);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $term = taxonomy_term_load($term->tid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $term->name = 'New name';
    taxonomy_term_save($term);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    taxonomy_term_delete($term->tid);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type taxonomy_term');
    $this->assertHookMessage('entity_crud_hook_test_taxonomy_term_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
