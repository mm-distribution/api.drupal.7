# CommonURLUnitTest::testLCustomClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 127–132 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L127-L132)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLCustomClass()
```

## Documentation

```text
Tests for custom class in l() function.
```

## Code

```php
  function testLCustomClass() {
    $class = $this->randomName();
    $link = l($this->randomName(), $_GET['q'], array('attributes' => array('class' => array($class))));
    $this->assertTrue($this->hasClass($link, $class), format_string('Custom class @class is present on link when requested', array('@class' => $class)));
    $this->assertTrue($this->hasClass($link, 'active'), format_string('Class @class is present on link to the current page', array('@class' => 'active')));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
