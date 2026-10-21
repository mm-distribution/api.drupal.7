# _openid_get_params()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 594–607 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L594-L607)
- **Module/theme:** openid

## Signature

```php
function _openid_get_params($str)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_get_params($str) {
  $chunks = explode("&", $str);

  $data = array();
  foreach ($chunks as $chunk) {
    $parts = explode("=", $chunk, 2);

    if (count($parts) == 2) {
      list($k, $v) = $parts;
      $data[$k] = urldecode($v);
    }
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
