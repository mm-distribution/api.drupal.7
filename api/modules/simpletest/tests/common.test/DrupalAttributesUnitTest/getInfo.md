# DrupalAttributesUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3050–3056 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3050-L3056)
- **Class:** [DrupalAttributesUnitTest](../DrupalAttributesUnitTest.md)
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
      'name' => 'HTML Attributes',
      'description' => 'Perform unit tests on the drupal_attributes() function.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
