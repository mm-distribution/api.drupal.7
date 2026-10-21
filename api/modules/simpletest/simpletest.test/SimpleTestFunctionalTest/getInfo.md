# SimpleTestFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 40–46 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L40-L46)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
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
      'name' => 'SimpleTest functionality',
      'description' => "Test SimpleTest's web interface: check that the intended tests were run and ensure that test reports display the intended results. Also test SimpleTest's internal browser and API's both explicitly and implicitly.",
      'group' => 'SimpleTest'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
