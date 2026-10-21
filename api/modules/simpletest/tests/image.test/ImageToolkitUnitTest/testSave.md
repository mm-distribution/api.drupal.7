# ImageToolkitUnitTest::testSave()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 111–114 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L111-L114)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSave()
```

## Documentation

```text
Test the image_save() function.
```

## Code

```php
  function testSave() {
    $this->assertFalse(image_save($this->image), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('save'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
