# ImageEffectsUnitTest::testScaleAndCropEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 458–468 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L458-L468)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testScaleAndCropEffect()
```

## Documentation

```text
Test the image_scale_and_crop_effect() function.
```

## Code

```php
  function testScaleAndCropEffect() {
    $this->assertTrue(image_scale_and_crop_effect($this->image, array('width' => 5, 'height' => 10)), 'Function returned the expected value.');
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
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
