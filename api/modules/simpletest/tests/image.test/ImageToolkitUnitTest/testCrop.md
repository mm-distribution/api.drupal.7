# ImageToolkitUnitTest::testCrop()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 175–185 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L175-L185)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testCrop()
```

## Documentation

```text
Test the image_crop() function.
```

## Code

```php
  function testCrop() {
    $this->assertTrue(image_crop($this->image, 1, 2, 3, 4), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('crop'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['crop'][0][1], 1, 'X was passed correctly');
    $this->assertEqual($calls['crop'][0][2], 2, 'Y was passed correctly');
    $this->assertEqual($calls['crop'][0][3], 3, 'Width was passed correctly');
    $this->assertEqual($calls['crop'][0][4], 4, 'Height was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
