# EntityLoadTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/entity_crud.test`](_file.md), lines 11–90 · [local source](../../../../../source/modules/simpletest/tests/entity_crud.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test#L11-L90)
- **Module/theme:** batch_test

## Signature

```php
class EntityLoadTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the entity_load() function.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](EntityLoadTestCase/getInfo.md)
- [testEntityLoadConditions()](EntityLoadTestCase/testEntityLoadConditions.md) — Tests the functionality for loading entities matching certain conditions.
- [testEntityLoadIds()](EntityLoadTestCase/testEntityLoadIds.md)
- [testEntityLoadInvalidControllerClass()](EntityLoadTestCase/testEntityLoadInvalidControllerClass.md) — Tests the controller class loading functionality on non-existing entity types and on entities without valid controller class.

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test) · Licensed GPL-2.0-or-later (see LICENSE)._
