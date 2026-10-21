# image_style_url()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1100–1137 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1100-L1137)
- **Module/theme:** image

## Signature

```php
function image_style_url($style_name, $path)
```

## Documentation

```text
Returns the URL for an image derivative given a style and image path.

@param $style_name
  The name of the style to be used with this image.
@param $path
  The path to the image.

@return
  The absolute URL where a style image can be downloaded, suitable for use
  in an <img> tag. Requesting the URL will cause the image to be created.
@see image_style_deliver()
```

## Code

```php
function image_style_url($style_name, $path) {
  $uri = image_style_path($style_name, $path);
  $uri = file_uri_normalize_dot_segments($uri);

  // The passed-in $path variable can be either a relative path or a full URI.
  $original_uri = file_uri_scheme($path) ? file_stream_wrapper_uri_normalize($path) : file_build_uri($path);
  $original_uri = file_uri_normalize_dot_segments($original_uri);

  // The token query is added even if the 'image_allow_insecure_derivatives'
  // variable is TRUE, so that the emitted links remain valid if it is changed
  // back to the default FALSE.
  // However, sites which need to prevent the token query from being emitted at
  // all can additionally set the 'image_suppress_itok_output' variable to TRUE
  // to achieve that (if both are set, the security token will neither be
  // emitted in the image derivative URL nor checked for in
  // image_style_deliver()).
  $token_query = array();
  if (!variable_get('image_suppress_itok_output', FALSE)) {
    $token_query = array(IMAGE_DERIVATIVE_TOKEN => image_style_path_token($style_name, $original_uri));
  }

  // If not using clean URLs, the image derivative callback is only available
  // with the query string. If the file does not exist, use url() to ensure
  // that it is included. Once the file exists it's fine to fall back to the
  // actual file path, this avoids bootstrapping PHP once the files are built.
  if (!variable_get('clean_url') && file_uri_scheme($uri) == 'public' && !file_exists($uri)) {
    $directory_path = file_stream_wrapper_get_instance_by_uri($uri)->getDirectoryPath();
    return url($directory_path . '/' . file_uri_target($uri), array('absolute' => TRUE, 'query' => $token_query));
  }

  $file_url = file_create_url($uri);
  // Append the query string with the token, if necessary.
  if ($token_query) {
    $file_url .= (strpos($file_url, '?') !== FALSE ? '&' : '?') . drupal_http_build_query($token_query);
  }

  return $file_url;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
