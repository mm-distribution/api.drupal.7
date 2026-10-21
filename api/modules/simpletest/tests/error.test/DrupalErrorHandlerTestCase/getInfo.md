# DrupalErrorHandlerTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 7–13 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L7-L13)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
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
      'name' => 'Drupal error handlers',
      'description' => 'Performs tests on the Drupal error and exception handler.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
