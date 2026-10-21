# CommonURLUnitTest::hasClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 134–136 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L134-L136)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
private function hasClass($link, $class)
```

## Documentation

_No docblock in source._

## Code

```php
  private function hasClass($link, $class) {
    return preg_match('|class="([^\"\s]+\s+)*' . $class . '|', $link);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
