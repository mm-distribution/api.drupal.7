# image_style_deliver()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 817–926 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L817-L926)
- **Module/theme:** image

## Signature

```php
function image_style_deliver($style, $scheme = NULL)
```

## Documentation

```text
Page callback: Generates a derivative, given a style and image path.

After generating an image, transfer it to the requesting agent.

@param $style
  The image style
@param $scheme
  The file scheme, for example 'public' for public files.
```

## Code

```php
function image_style_deliver($style, $scheme = NULL) {
  $args = func_get_args();
  array_shift($args);
  array_shift($args);
  $target = implode('/', $args);
  $image_uri = $scheme . '://' . $target;
  $image_uri = file_uri_normalize_dot_segments($image_uri);

  if (file_stream_wrapper_valid_scheme($scheme)) {
    $normalized_target = file_uri_target($image_uri);
    if ($normalized_target !== FALSE) {
      if (!in_array($scheme, variable_get('file_sa_core_2023_005_schemes', array()))) {
        $parts = explode('/', $normalized_target);
        if (array_intersect($parts, array('.', '..'))) {
          return MENU_NOT_FOUND;
        }
      }
    }
  }

  // Check that the style is defined, the scheme is valid.
  $valid = !empty($style) && !empty($scheme) && file_stream_wrapper_valid_scheme($scheme);

  // Also validate the derivative token. Sites which require image derivatives
  // to be generated without a token can set the 'image_allow_insecure_derivatives'
  // variable to TRUE to bypass the latter check, but this will increase the
  // site's vulnerability to denial-of-service attacks. To prevent this
  // variable from leaving the site vulnerable to the most serious attacks, a
  // token is always required when a derivative of a derivative is requested.)
  $token = isset($_GET[IMAGE_DERIVATIVE_TOKEN]) ? $_GET[IMAGE_DERIVATIVE_TOKEN] : '';
  $token_is_valid =
    $token === image_style_path_token($style['name'], $image_uri)
    || $token === image_style_path_token($style['name'], $scheme . '://' . $target);
  if (!variable_get('image_allow_insecure_derivatives', FALSE) || strpos(ltrim($target, '\/'), 'styles/') === 0) {
    $valid = $valid && $token_is_valid;
  }
  if (!$valid) {
    return MENU_ACCESS_DENIED;
  }

  $derivative_uri = image_style_path($style['name'], $image_uri);
  $derivative_scheme = file_uri_scheme($derivative_uri);

  if ($token_is_valid) {
    $is_public = ($scheme !== 'private');
  }
  else {
    $core_schemes = array('public', 'private', 'temporary');
    $additional_public_schemes = array_diff(variable_get('file_additional_public_schemes', array()), $core_schemes);
    $public_schemes = array_merge(array('public'), $additional_public_schemes);
    $is_public = in_array($derivative_scheme, $public_schemes, TRUE);
  }

  if ($scheme == 'private' && file_exists($derivative_uri)) {
    file_download($scheme, file_uri_target($derivative_uri));
  }

  $headers = array();

  if (!$is_public) {
    $headers = file_download_headers($image_uri);
    if (empty($headers)) {
      return MENU_ACCESS_DENIED;
    }
  }

  // Confirm that the original source image exists before trying to process it.
  if (!_image_source_image_exists($image_uri, $token_is_valid)) {
    watchdog('image', 'Source image at %source_image_path not found while trying to generate derivative image at %derivative_path.',  array('%source_image_path' => $image_uri, '%derivative_path' => $derivative_uri));
    return MENU_NOT_FOUND;
  }

  // Don't start generating the image if the derivative already exists or if
  // generation is in progress in another thread.
  $lock_name = 'image_style_deliver:' . $style['name'] . ':' . drupal_hash_base64($image_uri);
  if (!file_exists($derivative_uri)) {
    $lock_acquired = lock_acquire($lock_name);
    if (!$lock_acquired) {
      // Tell client to retry again in 3 seconds. Currently no browsers are known
      // to support Retry-After.
      drupal_add_http_header('Status', '503 Service Unavailable');
      drupal_add_http_header('Content-Type', 'text/html; charset=utf-8');
      drupal_add_http_header('Retry-After', 3);
      print t('Image generation in progress. Try again shortly.');
      drupal_exit();
    }
  }

  // Try to generate the image, unless another thread just did it while we were
  // acquiring the lock.
  $success = file_exists($derivative_uri) || image_style_create_derivative($style, $image_uri, $derivative_uri);

  if (!empty($lock_acquired)) {
    lock_release($lock_name);
  }

  if ($success) {
    $image = image_load($derivative_uri);
    $headers['Content-Type'] = $image->info['mime_type'];
    $headers['Content-Length'] = $image->info['file_size'];
    file_transfer($image->source, $headers);
  }
  else {
    watchdog('image', 'Unable to generate the derived image located at %path.', array('%path' => $derivative_uri));
    drupal_add_http_header('Status', '500 Internal Server Error');
    drupal_add_http_header('Content-Type', 'text/html; charset=utf-8');
    print t('Error generating image.');
    drupal_exit();
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
