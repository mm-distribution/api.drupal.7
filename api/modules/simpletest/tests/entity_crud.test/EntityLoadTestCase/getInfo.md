# EntityLoadTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud.test`](../_file.md), lines 14–20 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test#L14-L20)
- **Class:** [EntityLoadTestCase](../EntityLoadTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Entity loading',
      'description' => 'Tests the entity_load() function.',
      'group' => 'Entity API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test) · Licensed GPL-2.0-or-later (see LICENSE)._
