# ImageEffectsUnitTest::testRotateEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 485–494 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L485-L494)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testRotateEffect()
```

## Documentation

```text
Test the image_rotate_effect() function.
```

## Code

```php
  function testRotateEffect() {
    // @todo: need to test with 'random' => TRUE
    $this->assertTrue(image_rotate_effect($this->image, array('degrees' => 90, 'bgcolor' => '#fff')), 'Function returned the expected value.');
    $this->assertToolkitOperationsCalled(array('rotate'));

    // Check the parameters.
    $calls = image_test_get_all_calls();
    $this->assertEqual($calls['rotate'][0][1], 90, 'Degrees were passed correctly');
    $this->assertEqual($calls['rotate'][0][2], 0xffffff, 'Background color was passed correctly');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
