# ImageEffectsUnitTest::testDesaturateEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 473–480 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L473-L480)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testDesaturateEffect()
```

## Documentation

```text
Test the image_desaturate_effect() function.
```

## Code

```php
  function testDesaturateEffect() {
    $this->assertTrue(image_desaturate_effect($this->image, array()), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('desaturate'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual(count($calls['desaturate'][0]), 1, 'Only the image was passed.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
