# CascadingStylesheetsUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1095–1101 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1095-L1101)
- **Class:** [CascadingStylesheetsUnitTest](../CascadingStylesheetsUnitTest.md)
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
      'name' => 'CSS Unit Tests',
      'description' => 'Unit tests on CSS functions like aggregation.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
