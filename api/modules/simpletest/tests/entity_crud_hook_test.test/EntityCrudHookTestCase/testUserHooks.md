# EntityCrudHookTestCase::testUserHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 299–336 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L299-L336)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testUserHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on users.
```

## Code

```php
  public function testUserHooks() {
    $edit = array(
      'name' => 'Test user',
      'mail' => 'test@example.com',
      'created' => REQUEST_TIME,
      'status' => 1,
      'language' => 'en',
    );
    $account = (object) $edit;
    $_SESSION['entity_crud_hook_test'] = array();
    $account = user_save($account, $edit);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $account = user_load($account->uid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $edit['name'] = 'New name';
    $account = user_save($account, $edit);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    user_delete($account->uid);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type user');
    $this->assertHookMessage('entity_crud_hook_test_user_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
