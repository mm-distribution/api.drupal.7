# ImageToolkitUnitTest::testGetAvailableToolkits()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 91–96 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L91-L96)
- **Class:** [ImageToolkitUnitTest](../ImageToolkitUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetAvailableToolkits()
```

## Documentation

```text
Check that hook_image_toolkits() is called and only available toolkits are
returned.
```

## Code

```php
  function testGetAvailableToolkits() {
    $toolkits = image_get_available_toolkits();
    $this->assertTrue(isset($toolkits['test']), 'The working toolkit was returned.');
    $this->assertFalse(isset($toolkits['broken']), 'The toolkit marked unavailable was not returned');
    $this->assertToolkitOperationsCalled(array());
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
