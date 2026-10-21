# image_style_load()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 651–677 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L651-L677)
- **Module/theme:** image

## Signature

```php
function image_style_load($name = NULL, $isid = NULL, $include = NULL)
```

## Documentation

```text
Loads a style by style name or ID.

May be used as a loader for menu items.

@param $name
  The name of the style.
@param $isid
  Optional. The numeric id of a style if the name is not known.
@param $include
  If set, this loader will restrict to a specific type of image style, may be
  one of the defined Image style storage constants.

@return
  An image style array containing the following keys:
  - "isid": The unique image style ID.
  - "name": The unique image style name.
  - "effects": An array of image effects within this image style.
  If the image style name or ID is not valid, an empty array is returned.
@see image_effect_load()
```

## Code

```php
function image_style_load($name = NULL, $isid = NULL, $include = NULL) {
  $styles = image_styles();

  // If retrieving by name.
  if (isset($name) && isset($styles[$name])) {
    $style = $styles[$name];
  }

  // If retrieving by image style id.
  if (!isset($name) && isset($isid)) {
    foreach ($styles as $name => $database_style) {
      if (isset($database_style['isid']) && $database_style['isid'] == $isid) {
        $style = $database_style;
        break;
      }
    }
  }

  // Restrict to the specific type of flag. This bitwise operation basically
  // states "if the storage is X, then allow".
  if (isset($style) && (!isset($include) || ($style['storage'] & (int) $include))) {
    return $style;
  }

  // Otherwise the style was not found.
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
