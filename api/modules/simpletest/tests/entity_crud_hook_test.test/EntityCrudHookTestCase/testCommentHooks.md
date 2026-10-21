# EntityCrudHookTestCase::testCommentHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 59–114 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L59-L114)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testCommentHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on comments.
```

## Code

```php
  public function testCommentHooks() {
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
    node_save($node);
    $nid = $node->nid;

    $comment = (object) array(
      'cid' => NULL,
      'pid' => 0,
      'nid' => $nid,
      'uid' => 1,
      'subject' => 'Test comment',
      'created' => REQUEST_TIME,
      'changed' => REQUEST_TIME,
      'status' => 1,
      'language' => LANGUAGE_NONE,
    );
    $_SESSION['entity_crud_hook_test'] = array();
    comment_save($comment);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $comment = comment_load($comment->cid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $comment->subject = 'New subject';
    comment_save($comment);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    comment_delete($comment->cid);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type comment');
    $this->assertHookMessage('entity_crud_hook_test_comment_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
