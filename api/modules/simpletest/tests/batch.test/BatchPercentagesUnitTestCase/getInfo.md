# BatchPercentagesUnitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 322–328 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L322-L328)
- **Class:** [BatchPercentagesUnitTestCase](../BatchPercentagesUnitTestCase.md)
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
      'name' => 'Batch percentages',
      'description' => 'Unit tests of progress percentage rounding.',
      'group' => 'Batch API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
