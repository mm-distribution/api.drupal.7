# ImageToolkitUnitTest::testRotate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 162–170 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L162-L170)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testRotate()
```

## Documentation

```text
Test the image_rotate() function.
```

## Code

```php
  function testRotate() {
    $this->assertTrue(image_rotate($this->image, 90, 1), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('rotate'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['rotate'][0][1], 90, 'Degrees were passed correctly');
    $this->assertEqual($calls['rotate'][0][2], 1, 'Background color was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
