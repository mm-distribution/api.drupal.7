# EntityCrudHookTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 31–33 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L31-L33)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('entity_crud_hook_test', 'taxonomy', 'comment');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
