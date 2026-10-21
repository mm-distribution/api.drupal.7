# ImageToolkitUnitTest::testScale()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 132–141 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L132-L141)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testScale()
```

## Documentation

```text
Test the image_scale() function.
```

## Code

```php
  function testScale() {
// TODO: need to test upscaling
    $this->assertTrue(image_scale($this->image, 10, 10), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('resize'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['resize'][0][1], 10, 'Width was passed correctly');
    $this->assertEqual($calls['resize'][0][2], 5, 'Height was based off aspect ratio and passed correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
