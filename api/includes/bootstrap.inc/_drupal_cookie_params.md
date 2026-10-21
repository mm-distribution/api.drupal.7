# _drupal_cookie_params()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 4040–4052 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L4040-L4052)

## Signature

```php
function _drupal_cookie_params($options)
```

## Documentation

```text
Process the params for cookies. This emulates support for the SameSite
attribute in earlier versions of PHP, and allows the value of that attribute
to be overridden.

@param $options
  An associative array which may have any of the keys expires, path, domain,
  secure, httponly, samesite.

@return
  An associative array which may have any of the keys expires, path, domain,
  secure, httponly, and samesite.
```

## Code

```php
function _drupal_cookie_params($options) {
  $options['samesite'] = _drupal_samesite_cookie($options);
  if (\PHP_VERSION_ID < 70300) {
    // Emulate SameSite support in older PHP versions.
    if (!empty($options['samesite'])) {
      // Ensure the SameSite attribute is only added once.
      if (!preg_match('/SameSite=/i', $options['path'])) {
        $options['path'] .= '; SameSite=' . $options['samesite'];
      }
    }
  }
  return $options;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
