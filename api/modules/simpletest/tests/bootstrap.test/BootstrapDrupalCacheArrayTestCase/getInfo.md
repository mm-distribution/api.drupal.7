# BootstrapDrupalCacheArrayTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 913–919 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L913-L919)
- **Class:** [BootstrapDrupalCacheArrayTestCase](../BootstrapDrupalCacheArrayTestCase.md)
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
      'name' => 'DrupalCacheArray tests',
      'description' => 'Test DrupalCacheArray functionality.',
      'group' => 'Bootstrap',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
