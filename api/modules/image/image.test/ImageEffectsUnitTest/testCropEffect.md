# ImageEffectsUnitTest::testCropEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 442–453 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L442-L453)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testCropEffect()
```

## Documentation

```text
Test the image_crop_effect() function.
```

## Code

```php
  function testCropEffect() {
    // @todo should test the keyword offsets.
    $this->assertTrue(image_crop_effect($this->image, array('anchor' => 'top-1', 'width' => 3, 'height' => 4)), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('crop'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['crop'][0][1], 0, 'X was passed correctly');
    $this->assertEqual($calls['crop'][0][2], 1, 'Y was passed correctly');
    $this->assertEqual($calls['crop'][0][3], 3, 'Width was passed correctly');
    $this->assertEqual($calls['crop'][0][4], 4, 'Height was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
