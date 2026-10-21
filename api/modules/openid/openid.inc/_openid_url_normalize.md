# _openid_url_normalize()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 315–330 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L315-L330)
- **Module/theme:** openid

## Signature

```php
function _openid_url_normalize($url)
```

## Documentation

```text
OpenID normalization method: normalize URL identifiers.
```

## Code

```php
function _openid_url_normalize($url) {
  $normalized_url = $url;

  if (stristr($url, '://') === FALSE) {
    $normalized_url = 'http://' . $url;
  }

  // Strip the fragment and fragment delimiter if present.
  $normalized_url = strtok($normalized_url, '#');

  if (substr_count($normalized_url, '/') < 3) {
    $normalized_url .= '/';
  }

  return $normalized_url;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
