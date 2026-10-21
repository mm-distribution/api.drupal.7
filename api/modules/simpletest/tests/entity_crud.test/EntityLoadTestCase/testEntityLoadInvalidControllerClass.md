# EntityLoadTestCase::testEntityLoadInvalidControllerClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud.test`](../_file.md), lines 66–89 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test#L66-L89)
- **Class:** [EntityLoadTestCase](../EntityLoadTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testEntityLoadInvalidControllerClass()
```

## Documentation

```text
Tests the controller class loading functionality on non-existing entity
types and on entities without valid controller class.
```

## Code

```php
  public function testEntityLoadInvalidControllerClass() {
    // Ensure that loading a non-existing entity type will throw an
    // EntityMalformedException.
    try {
      entity_load('test', array('1'));
      $this->fail(t('Cannot load a controller class on non-existing entity type.'));
    }
    catch (EntityMalformedException $e) {
      $this->pass(t('Cannot load a controller class on non-existing entity type.'));
    }

    // Ensure that loading an entity without valid controller class will throw
    // an EntityMalformedException.
    module_enable(array('entity_crud_hook_test'));
    variable_set('entity_crud_hook_test_alter_controller_class', TRUE);
    try {
      entity_load('node', array('1'));
      $this->fail(t('Cannot load a missing or non-existent controller class.'));
    }
    catch (EntityMalformedException $e) {
      $this->pass(t('Cannot load a missing or non-existent controller class.'));
    }
    variable_set('entity_crud_hook_test_alter_controller_class', FALSE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test) · Licensed GPL-2.0-or-later (see LICENSE)._
