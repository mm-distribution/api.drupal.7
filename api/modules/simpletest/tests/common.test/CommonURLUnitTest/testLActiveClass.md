# CommonURLUnitTest::testLActiveClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 119–122 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L119-L122)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLActiveClass()
```

## Documentation

_No docblock in source._

## Code

```php
  function testLActiveClass() {
    $link = l($this->randomName(), $_GET['q']);
    $this->assertTrue($this->hasClass($link, 'active'), format_string('Class @class is present on link to the current page', array('@class' => 'active')));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
