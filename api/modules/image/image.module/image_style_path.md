# image_style_path()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1175–1185 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1175-L1185)
- **Module/theme:** image

## Signature

```php
function image_style_path($style_name, $uri)
```

## Documentation

```text
Returns the URI of an image when using a style.

The path returned by this function may not exist. The default generation
method only creates images when they are requested by a user's browser.

@param $style_name
  The name of the style to be used with this image.
@param $uri
  The URI or path to the image.

@return
  The URI to an image style image.
@see image_style_url()
```

## Code

```php
function image_style_path($style_name, $uri) {
  $scheme = file_uri_scheme($uri);
  if ($scheme) {
    $path = file_uri_target($uri);
  }
  else {
    $path = $uri;
    $scheme = file_default_scheme();
  }
  return $scheme . '://styles/' . $style_name . '/' . $scheme . '/' . $path;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
