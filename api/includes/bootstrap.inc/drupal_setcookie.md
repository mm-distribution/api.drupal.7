# drupal_setcookie()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 4009–4025 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L4009-L4025)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_setcookie($name, $value, $options)
```

## Documentation

```text
Drupal's wrapper around PHP's setcookie() function.

This allows the cookie's $value and $options to be altered.

@param $name
  The name of the cookie.
@param $value
  The value of the cookie.
@param $options
  An associative array which may have any of the keys expires, path, domain,
  secure, httponly, samesite.

@see setcookie()
@ingroup php_wrappers
```

## Code

```php
function drupal_setcookie($name, $value, $options) {
  $options = _drupal_cookie_params($options);
  if (\PHP_VERSION_ID >= 70300) {
    setcookie($name, $value, $options);
  }
  else {
    $defaults = array(
      'expires' => 0,
      'path' => '',
      'domain' => '',
      'secure' => FALSE,
      'httponly' => FALSE,
    );
    $options += $defaults;
    setcookie($name, $value, $options['expires'], $options['path'], $options['domain'], $options['secure'], $options['httponly']);
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
