# image_rotate_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 253–285 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L253-L285)
- **Module/theme:** image

## Signature

```php
function image_rotate_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Rotate an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the rotate effect containing
  the following items:
  - "degrees": The number of (clockwise) degrees to rotate the image.
  - "random": A boolean indicating that a random rotation angle should be
    used for this image. The angle specified in "degrees" is used as a
    positive and negative maximum.
  - "bgcolor": The background color to use for exposed areas of the image.
    Use web-style hex colors (#FFFFFF for white, #000000 for black). Leave
    blank for transparency on image types that support it.
@return
  TRUE on success. FALSE on failure to rotate image.
@see image_rotate().
```

## Code

```php
function image_rotate_effect(&$image, $data) {
  // Set sane default values.
  $data += array(
    'degrees' => 0,
    'bgcolor' => NULL,
    'random' => FALSE,
  );

  // Convert short #FFF syntax to full #FFFFFF syntax.
  if (strlen((string) $data['bgcolor']) == 4) {
    $c = $data['bgcolor'];
    $data['bgcolor'] = $c[0] . $c[1] . $c[1] . $c[2] . $c[2] . $c[3] . $c[3];
  }

  // Convert #FFFFFF syntax to hexadecimal colors.
  if ($data['bgcolor'] != '') {
    $data['bgcolor'] = hexdec(str_replace('#', '0x', $data['bgcolor']));
  }
  else {
    $data['bgcolor'] = NULL;
  }

  if (!empty($data['random'])) {
    $degrees = abs((float) $data['degrees']);
    $data['degrees'] = rand(-1 * $degrees, $degrees);
  }

  if (!image_rotate($image, $data['degrees'], $data['bgcolor'])) {
    watchdog('image', 'Image rotate failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
