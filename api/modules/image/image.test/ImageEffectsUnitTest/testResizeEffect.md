# ImageEffectsUnitTest::testResizeEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 415–423 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L415-L423)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testResizeEffect()
```

## Documentation

```text
Test the image_resize_effect() function.
```

## Code

```php
  function testResizeEffect() {
    $this->assertTrue(image_resize_effect($this->image, array('width' => 1, 'height' => 2)), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('resize'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['resize'][0][1], 1, 'Width was passed correctly');
    $this->assertEqual($calls['resize'][0][2], 2, 'Height was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
