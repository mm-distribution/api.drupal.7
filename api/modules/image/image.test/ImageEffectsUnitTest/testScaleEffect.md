# ImageEffectsUnitTest::testScaleEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 428–437 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L428-L437)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testScaleEffect()
```

## Documentation

```text
Test the image_scale_effect() function.
```

## Code

```php
  function testScaleEffect() {
    // @todo: need to test upscaling.
    $this->assertTrue(image_scale_effect($this->image, array('width' => 10, 'height' => 10)), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('resize'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['resize'][0][1], 10, 'Width was passed correctly');
    $this->assertEqual($calls['resize'][0][2], 5, 'Height was based off aspect ratio and passed correctly');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
