# image_effect_load()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1367–1372 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1367-L1372)
- **Module/theme:** image

## Signature

```php
function image_effect_load($ieid, $style_name, $include = NULL)
```

## Documentation

```text
Loads a single image effect.

@param $ieid
  The image effect ID.
@param $style_name
  The image style name.
@param $include
  If set, this loader will restrict to a specific type of image style, may be
  one of the defined Image style storage constants.

@return
  An image effect array, consisting of the following keys:
  - "ieid": The unique image effect ID.
  - "isid": The unique image style ID that contains this image effect.
  - "weight": The weight of this image effect within the image style.
  - "name": The name of the effect definition that powers this image effect.
  - "data": An array of configuration options for this image effect.
  Besides these keys, the entirety of the image definition is merged into
  the image effect array. Returns FALSE if the specified effect cannot be
  found.
@see image_style_load()
@see image_effect_definition_load()
```

## Code

```php
function image_effect_load($ieid, $style_name, $include = NULL) {
  if (($style = image_style_load($style_name, NULL, $include)) && isset($style['effects'][$ieid])) {
    return $style['effects'][$ieid];
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
