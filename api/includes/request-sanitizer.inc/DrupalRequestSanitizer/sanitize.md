# DrupalRequestSanitizer::sanitize()

- **Type:** Method
- **File:** [`includes/request-sanitizer.inc`](../_file.md), lines 21–52 · [local source](../../../../source/includes/request-sanitizer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc#L21-L52)
- **Class:** [DrupalRequestSanitizer](../DrupalRequestSanitizer.md)

## Signature

```php
public static function sanitize()
```

## Documentation

```text
Modifies the request to strip dangerous keys from user input.
```

## Code

```php
  public static function sanitize() {
    if (!self::$sanitized) {
      $whitelist = variable_get('sanitize_input_whitelist', array());
      $log_sanitized_keys = variable_get('sanitize_input_logging', FALSE);

      // Process query string parameters.
      $get_sanitized_keys = array();
      $_GET = self::stripDangerousValues($_GET, $whitelist, $get_sanitized_keys);
      if ($log_sanitized_keys && $get_sanitized_keys) {
        _drupal_trigger_error_with_delayed_logging(format_string('Potentially unsafe keys removed from query string parameters (GET): @keys', array('@keys' => implode(', ', $get_sanitized_keys))), E_USER_NOTICE);
      }

      // Process request body parameters.
      $post_sanitized_keys = array();
      $_POST = self::stripDangerousValues($_POST, $whitelist, $post_sanitized_keys);
      if ($log_sanitized_keys && $post_sanitized_keys) {
        _drupal_trigger_error_with_delayed_logging(format_string('Potentially unsafe keys removed from request body parameters (POST): @keys', array('@keys' => implode(', ', $post_sanitized_keys))), E_USER_NOTICE);
      }

      // Process cookie parameters.
      $cookie_sanitized_keys = array();
      $_COOKIE = self::stripDangerousValues($_COOKIE, $whitelist, $cookie_sanitized_keys);
      if ($log_sanitized_keys && $cookie_sanitized_keys) {
        _drupal_trigger_error_with_delayed_logging(format_string('Potentially unsafe keys removed from cookie parameters (COOKIE): @keys', array('@keys' => implode(', ', $cookie_sanitized_keys))), E_USER_NOTICE);
      }

      $request_sanitized_keys = array();
      $_REQUEST = self::stripDangerousValues($_REQUEST, $whitelist, $request_sanitized_keys);

      self::$sanitized = TRUE;
    }
  }
```

---
_Drupal 7.103 · [includes/request-sanitizer.inc](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
