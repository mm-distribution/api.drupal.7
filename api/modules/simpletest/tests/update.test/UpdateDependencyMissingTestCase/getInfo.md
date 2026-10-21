# UpdateDependencyMissingTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 62–68 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L62-L68)
- **Class:** [UpdateDependencyMissingTestCase](../UpdateDependencyMissingTestCase.md)
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
      'name' => 'Missing update dependencies',
      'description' => 'Test that missing update dependencies are correctly flagged.',
      'group' => 'Update API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
