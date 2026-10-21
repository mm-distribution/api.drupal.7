# DrupalRequestSanitizer::stripDangerousValues()

- **Type:** Method
- **File:** [`includes/request-sanitizer.inc`](../_file.md), lines 99–112 · [local source](../../../../source/includes/request-sanitizer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc#L99-L112)
- **Class:** [DrupalRequestSanitizer](../DrupalRequestSanitizer.md)

## Signature

```php
protected static function stripDangerousValues($input, array $whitelist, array &$sanitized_keys)
```

## Documentation

```text
Strips dangerous keys from the provided input.

@param mixed $input
  The input to sanitize.
@param string[] $whitelist
  An array of keys to whitelist as safe.
@param string[] $sanitized_keys
  An array of keys that have been removed.

@return mixed
  The sanitized input.
```

## Code

```php
  protected static function stripDangerousValues($input, array $whitelist, array &$sanitized_keys) {
    if (is_array($input)) {
      foreach ($input as $key => $value) {
        if ($key !== '' && is_string($key) && $key[0] === '#' && !in_array($key, $whitelist, TRUE)) {
          unset($input[$key]);
          $sanitized_keys[] = $key;
        }
        else {
          $input[$key] = self::stripDangerousValues($input[$key], $whitelist, $sanitized_keys);
        }
      }
    }
    return $input;
  }
```

---
_Drupal 7.103 · [includes/request-sanitizer.inc](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
