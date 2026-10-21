# drupal_base64_encode()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2303–2307 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2303-L2307)

## Signature

```php
function drupal_base64_encode($string)
```

## Documentation

```text
Returns a URL-safe, base64 encoded version of the supplied string.

@param $string
  The string to convert to base64.

@return string
```

## Code

```php
function drupal_base64_encode($string) {
  $data = base64_encode($string);
  // Modify the output so it's safe to use in URLs.
  return strtr($data, array('+' => '-', '/' => '_', '=' => ''));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
