# EntityCrudHookTestCase::testNodeHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 165–206 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L165-L206)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNodeHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on nodes.
```

## Code

```php
  public function testNodeHooks() {
    $node = (object) array(
      'uid' => 1,
      'type' => 'article',
      'title' => 'Test node',
      'status' => 1,
      'comment' => 2,
      'promote' => 0,
      'sticky' => 0,
      'language' => LANGUAGE_NONE,
      'created' => REQUEST_TIME,
      'changed' => REQUEST_TIME,
    );
    $_SESSION['entity_crud_hook_test'] = array();
    node_save($node);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $node = node_load($node->nid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $node->title = 'New title';
    node_save($node);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    node_delete($node->nid);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type node');
    $this->assertHookMessage('entity_crud_hook_test_node_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
