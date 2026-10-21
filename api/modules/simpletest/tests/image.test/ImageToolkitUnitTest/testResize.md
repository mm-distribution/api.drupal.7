# ImageToolkitUnitTest::testResize()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 119–127 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L119-L127)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testResize()
```

## Documentation

```text
Test the image_resize() function.
```

## Code

```php
  function testResize() {
    $this->assertTrue(image_resize($this->image, 1, 2), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('resize'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['resize'][0][1], 1, 'Width was passed correctly');
    $this->assertEqual($calls['resize'][0][2], 2, 'Height was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
