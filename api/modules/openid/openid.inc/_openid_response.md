# _openid_response()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 573–592 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L573-L592)
- **Module/theme:** openid

## Signature

```php
function _openid_response($str = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_response($str = NULL) {
  $data = array();

  if (isset($_SERVER['REQUEST_METHOD'])) {
    $data = _openid_get_params($_SERVER['QUERY_STRING']);

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
      $str = file_get_contents('php://input');

      $post = array();
      if ($str !== FALSE) {
        $post = _openid_get_params($str);
      }

      $data = array_merge($data, $post);
    }
  }

  return $data;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
