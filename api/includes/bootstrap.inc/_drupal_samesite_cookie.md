# _drupal_samesite_cookie()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 4068–4081 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L4068-L4081)

## Signature

```php
function _drupal_samesite_cookie($options)
```

## Documentation

```text
Determine the value for the samesite cookie attribute, in the following order
of precedence:

1) A value explicitly passed to drupal_setcookie()
2) A value set in $conf['samesite_cookie_value']
3) The setting from php ini
4) The default of None, or FALSE (no attribute) if the cookie is not Secure

@param $options
  An associative array as passed to drupal_setcookie().
@return
  The value for the samesite cookie attribute.
```

## Code

```php
function _drupal_samesite_cookie($options) {
  if (isset($options['samesite'])) {
    return $options['samesite'];
  }
  $override = variable_get('samesite_cookie_value', NULL);
  if ($override !== NULL) {
    return $override;
  }
  $ini_options = session_get_cookie_params();
  if (isset($ini_options['samesite'])) {
    return $ini_options['samesite'];
  }
  return empty($options['secure']) ? FALSE : 'None';
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
