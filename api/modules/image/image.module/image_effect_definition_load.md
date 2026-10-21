# image_effect_definition_load()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1296–1309 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1296-L1309)
- **Module/theme:** image

## Signature

```php
function image_effect_definition_load($effect, $style_name = NULL)
```

## Documentation

```text
Loads the definition for an image effect.

The effect definition is a set of core properties for an image effect, not
containing any user-settings. The definition defines various functions to
call when configuring or executing an image effect. This loader is mostly for
internal use within image.module. Use image_effect_load() or
image_style_load() to get image effects that contain configuration.

@param $effect
  The name of the effect definition to load.
@param $style
  An image style array to which this effect will be added.

@return
  An array containing the image effect definition with the following keys:
  - "effect": The unique name for the effect being performed. Usually prefixed
    with the name of the module providing the effect.
  - "module": The module providing the effect.
  - "help": A description of the effect.
  - "function": The name of the function that will execute the effect.
  - "form": (optional) The name of a function to configure the effect.
  - "summary": (optional) The name of a theme function that will display a
    one-line summary of the effect. Does not include the "theme_" prefix.
```

## Code

```php
function image_effect_definition_load($effect, $style_name = NULL) {
  $definitions = image_effect_definitions();

  // If a style is specified, do not allow loading of default style
  // effects.
  if (isset($style_name)) {
    $style = image_style_load($style_name, NULL);
    if ($style['storage'] == IMAGE_STORAGE_DEFAULT) {
      return FALSE;
    }
  }

  return isset($definitions[$effect]) ? $definitions[$effect] : FALSE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
