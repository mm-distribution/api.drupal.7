# image_style_path_token()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1155–1158 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1155-L1158)
- **Module/theme:** image

## Signature

```php
function image_style_path_token($style_name, $uri)
```

## Documentation

```text
Generates a token to protect an image style derivative.

This prevents unauthorized generation of an image style derivative,
which can be costly both in CPU time and disk space.

@param $style_name
  The name of the image style.
@param $uri
  The URI of the image for this style, for example as returned by
  image_style_path().

@return
  An eight-character token which can be used to protect image style
  derivatives against denial-of-service attacks.
```

## Code

```php
function image_style_path_token($style_name, $uri) {
  // Return the first eight characters.
  return substr(drupal_hmac_base64($style_name . ':' . $uri, drupal_get_private_key() . drupal_get_hash_salt()), 0, 8);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
