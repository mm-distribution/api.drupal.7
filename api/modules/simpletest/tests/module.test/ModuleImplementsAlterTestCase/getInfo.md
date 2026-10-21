# ModuleImplementsAlterTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 348–354 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L348-L354)
- **Class:** [ModuleImplementsAlterTestCase](../ModuleImplementsAlterTestCase.md)
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
      'name' => 'Module implements alter',
      'description' => 'Tests hook_module_implements_alter().',
      'group' => 'Module',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
