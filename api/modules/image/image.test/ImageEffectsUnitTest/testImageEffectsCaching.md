# ImageEffectsUnitTest::testImageEffectsCaching()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 499–513 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L499-L513)
- **Class:** [ImageEffectsUnitTest](../ImageEffectsUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testImageEffectsCaching()
```

## Documentation

```text
Test image effect caching.
```

## Code

```php
  function testImageEffectsCaching() {
    $image_effect_definitions_called = &drupal_static('image_module_test_image_effect_info_alter');

    // First call should grab a fresh copy of the data.
    $effects = image_effect_definitions();
    $this->assertTrue($image_effect_definitions_called === 1, 'image_effect_definitions() generated data.');

    // Second call should come from cache.
    drupal_static_reset('image_effect_definitions');
    drupal_static_reset('image_module_test_image_effect_info_alter');
    $cached_effects = image_effect_definitions();
    $this->assertTrue(is_null($image_effect_definitions_called), 'image_effect_definitions() returned data from cache.');

    $this->assertTrue($effects == $cached_effects, 'Cached effects are the same as generated effects.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
