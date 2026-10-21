# ImageToolkitUnitTest::testScaleAndCrop()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 146–157 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L146-L157)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testScaleAndCrop()
```

## Documentation

```text
Test the image_scale_and_crop() function.
```

## Code

```php
  function testScaleAndCrop() {
    $this->assertTrue(image_scale_and_crop($this->image, 5, 10), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('resize', 'crop'));

    // Check the parameters.
    $calls = image_test_get_all_calls();

    $this->assertEqual($calls['crop'][0][1], 7.5, 'X was computed and passed correctly');
    $this->assertEqual($calls['crop'][0][2], 0, 'Y was computed and passed correctly');
    $this->assertEqual($calls['crop'][0][3], 5, 'Width was computed and passed correctly');
    $this->assertEqual($calls['crop'][0][4], 10, 'Height was computed and passed correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
