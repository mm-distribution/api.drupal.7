# image_gd_get_info()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 399–415 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L399-L415)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_get_info(stdClass $image)
```

## Documentation

```text
Get details about an image.

@param $image
  An image object.
@return
  FALSE, if the file could not be found or is not an image. Otherwise, a
  keyed array containing information about the image:
  - "width": Width, in pixels.
  - "height": Height, in pixels.
  - "extension": Commonly used file extension for the image.
  - "mime_type": MIME type ('image/jpeg', 'image/gif', 'image/png').

@see image_get_info()
```

## Code

```php
function image_gd_get_info(stdClass $image) {
  $details = FALSE;
  $data = @getimagesize($image->source);

  if (isset($data) && is_array($data)) {
    $extensions = array('1' => 'gif', '2' => 'jpg', '3' => 'png');
    $extension = isset($extensions[$data[2]]) ?  $extensions[$data[2]] : '';
    $details = array(
      'width'     => $data[0],
      'height'    => $data[1],
      'extension' => $extension,
      'mime_type' => $data['mime'],
    );
  }

  return $details;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
