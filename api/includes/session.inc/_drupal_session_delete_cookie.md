# _drupal_session_delete_cookie()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 522–539 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L522-L539)

## Signature

```php
function _drupal_session_delete_cookie($name, $secure = NULL)
```

## Documentation

```text
Deletes the session cookie.

@param $name
  Name of session cookie to delete.
@param boolean $secure
  Force the secure value of the cookie.
```

## Code

```php
function _drupal_session_delete_cookie($name, $secure = NULL) {
  global $is_https;
  if (isset($_COOKIE[$name]) || (!$is_https && $secure === TRUE)) {
    $params = session_get_cookie_params();
    if ($secure !== NULL) {
      $params['secure'] = $secure;
    }
    $options = array(
      'expires' => REQUEST_TIME - 3600,
      'path' => $params['path'],
      'domain' => $params['domain'],
      'secure' => $params['secure'],
      'httponly' => $params['httponly'],
    );
    drupal_setcookie($name, '', $options);
    unset($_COOKIE[$name]);
  }
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
