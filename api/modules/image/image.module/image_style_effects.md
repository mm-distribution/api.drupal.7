# image_style_effects()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 762–772 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L762-L772)
- **Module/theme:** image

## Signature

```php
function image_style_effects($style)
```

## Documentation

```text
Loads all the effects for an image style.

@param array $style
  An image style array containing:
  - isid: The unique image style ID that contains this image effect.

@return array
  An array of image effects associated with specified image style in the
  format array('isid' => array()), or an empty array if the specified style
  has no effects.
@see image_effects()
```

## Code

```php
function image_style_effects($style) {
  $effects = image_effects();
  $style_effects = array();
  foreach ($effects as $effect) {
    if ($style['isid'] == $effect['isid']) {
      $style_effects[$effect['ieid']] = $effect;
    }
  }

  return $style_effects;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
