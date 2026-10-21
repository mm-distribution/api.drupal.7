# ModuleInstallTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 283–289 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L283-L289)
- **Class:** [ModuleInstallTestCase](../ModuleInstallTestCase.md)
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
      'name' => 'Module installation',
      'description' => 'Tests the installation of modules.',
      'group' => 'Module',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
