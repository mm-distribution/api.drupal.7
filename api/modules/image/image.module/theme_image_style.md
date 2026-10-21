# theme_image_style()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1447–1462 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1447-L1462)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_style($variables)
```

## Documentation

```text
Returns HTML for an image using a specific image style.

@param $variables
  An associative array containing:
  - style_name: The name of the style to be used to alter the original image.
  - path: The path of the image file relative to the Drupal files directory.
    This function does not work with images outside the files directory nor
    with remotely hosted images. This should be in a format such as
    'images/image.jpg', or using a stream wrapper such as
    'public://images/image.jpg'.
  - width: The width of the source image (if known).
  - height: The height of the source image (if known).
  - alt: The alternative text for text-based browsers.
  - title: The title text is displayed when the image is hovered in some
    popular browsers.
  - attributes: Associative array of attributes to be placed in the img tag.

@ingroup themeable
```

## Code

```php
function theme_image_style($variables) {
  // Determine the dimensions of the styled image.
  $dimensions = array(
    'width' => $variables['width'],
    'height' => $variables['height'],
  );

  image_style_transform_dimensions($variables['style_name'], $dimensions);

  $variables['width'] = $dimensions['width'];
  $variables['height'] = $dimensions['height'];

  // Determine the URL for the styled image.
  $variables['path'] = image_style_url($variables['style_name'], $variables['path']);
  return theme('image', $variables);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
