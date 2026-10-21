# openid_redirect_http()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 75–85 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L75-L85)
- **Module/theme:** openid

## Signature

```php
function openid_redirect_http($url, $message)
```

## Documentation

```text
Performs an HTTP 302 redirect (for the 1.x protocol).
```

## Code

```php
function openid_redirect_http($url, $message) {
  $query = array();
  foreach ($message as $key => $val) {
    $query[] = $key . '=' . urlencode($val);
  }

  $sep = (strpos($url, '?') === FALSE) ? '?' : '&';
  header('Location: ' . $url . $sep . implode('&', $query), TRUE, 302);

  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
