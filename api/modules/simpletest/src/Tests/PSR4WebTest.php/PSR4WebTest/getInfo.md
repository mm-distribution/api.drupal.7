# PSR4WebTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/src/Tests/PSR4WebTest.php`](../_file.md), lines 7–13 · [local source](../../../../../../../source/modules/simpletest/src/Tests/PSR4WebTest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/src/Tests/PSR4WebTest.php#L7-L13)
- **Class:** [PSR4WebTest](../PSR4WebTest.md)
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
      'name' => 'PSR4 web test',
      'description' => 'We want to assert that this PSR-4 test case is being discovered.',
      'group' => 'SimpleTest',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/src/Tests/PSR4WebTest.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/src/Tests/PSR4WebTest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
