# SimpleTestInstallationProfileModuleTestsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 663–669 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L663-L669)
- **Class:** [SimpleTestInstallationProfileModuleTestsTestCase](../SimpleTestInstallationProfileModuleTestsTestCase.md)
- **Module/theme:** simpletest

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
      'name' => 'Installation profile module tests',
      'description' => 'Verifies that tests bundled with installation profile modules are found.',
      'group' => 'SimpleTest',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
