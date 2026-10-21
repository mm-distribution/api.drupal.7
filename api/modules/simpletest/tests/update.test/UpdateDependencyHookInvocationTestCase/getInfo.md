# UpdateDependencyHookInvocationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 92–98 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L92-L98)
- **Class:** [UpdateDependencyHookInvocationTestCase](../UpdateDependencyHookInvocationTestCase.md)
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
      'name' => 'Update dependency hook invocation',
      'description' => 'Test that the hook invocation for determining update dependencies works correctly.',
      'group' => 'Update API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
