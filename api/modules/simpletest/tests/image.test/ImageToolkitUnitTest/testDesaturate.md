# ImageToolkitUnitTest::testDesaturate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 190–197 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L190-L197)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDesaturate()
```

## Documentation

```text
Test the image_desaturate() function.
```

## Code

```php
  function testDesaturate() {
    $this->assertTrue(image_desaturate($this->image), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('desaturate'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual(count($calls['desaturate'][0]), 1, 'Only the image was passed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
