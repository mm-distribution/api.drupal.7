# SimpleTestBrokenSetUp::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 587–593 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L587-L593)
- **Class:** [SimpleTestBrokenSetUp](../SimpleTestBrokenSetUp.md)
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
      'name' => 'Broken SimpleTest method',
      'description' => 'Tests a test case that does not call parent::setUp().',
      'group' => 'SimpleTest'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
