# EntityCrudHookTestCase::testFileHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 119–160 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L119-L160)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFileHooks()
```

## Documentation

```text
Tests hook invocations for CRUD operations on files.
```

## Code

```php
  public function testFileHooks() {
    $url = 'public://entity_crud_hook_test.file';
    file_put_contents($url, 'Test test test');
    $file = (object) array(
      'fid' => NULL,
      'uid' => 1,
      'filename' => 'entity_crud_hook_test.file',
      'uri' => $url,
      'filemime' => 'text/plain',
      'filesize' => filesize($url),
      'status' => 1,
      'timestamp' => REQUEST_TIME,
    );
    $_SESSION['entity_crud_hook_test'] = array();
    file_save($file);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_insert called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_insert called');

    $_SESSION['entity_crud_hook_test'] = array();
    $file = file_load($file->fid);

    $this->assertHookMessage('entity_crud_hook_test_entity_load called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_load called');

    $_SESSION['entity_crud_hook_test'] = array();
    $file->filename = 'new.entity_crud_hook_test.file';
    file_save($file);

    $this->assertHookMessage('entity_crud_hook_test_entity_presave called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_presave called');
    $this->assertHookMessage('entity_crud_hook_test_entity_update called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_update called');

    $_SESSION['entity_crud_hook_test'] = array();
    file_delete($file);

    $this->assertHookMessage('entity_crud_hook_test_entity_delete called for type file');
    $this->assertHookMessage('entity_crud_hook_test_file_delete called');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
