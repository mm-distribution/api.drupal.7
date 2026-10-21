# ImageToolkitUnitTest::testLoad()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 101–106 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L101-L106)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoad()
```

## Documentation

```text
Test the image_load() function.
```

## Code

```php
  function testLoad() {
    $image = image_load($this->file, $this->toolkit);
    $this->assertTrue(is_object($image), 'Returned an object.');
    $this->assertEqual($this->toolkit, $image->toolkit, 'Image had toolkit set.');
    $this->assertToolkitOperationsCalled(array('load', 'get_info'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
