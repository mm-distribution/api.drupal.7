# DrupalRequestSanitizer::cleanDestination()

- **Type:** Method
- **File:** [`includes/request-sanitizer.inc`](../_file.md), lines 62–84 · [local source](../../../../source/includes/request-sanitizer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc#L62-L84)
- **Class:** [DrupalRequestSanitizer](../DrupalRequestSanitizer.md)

## Signature

```php
public static function cleanDestination()
```

## Documentation

```text
Removes the destination if it is dangerous.

Note this can only be called after common.inc has been included.

@return bool
  TRUE if the destination has been removed from $_GET, FALSE if not.
```

## Code

```php
  public static function cleanDestination() {
    $dangerous_keys = array();
    $log_sanitized_keys = variable_get('sanitize_input_logging', FALSE);

    $parts = drupal_parse_url($_GET['destination']);
    // If there is a query string, check its query parameters.
    if (!empty($parts['query'])) {
      $whitelist = variable_get('sanitize_input_whitelist', array());

      self::stripDangerousValues($parts['query'], $whitelist, $dangerous_keys);
      if (!empty($dangerous_keys)) {
        // The destination is removed rather than sanitized to mirror the
        // handling of external destinations.
        unset($_GET['destination']);
        unset($_REQUEST['destination']);
        if ($log_sanitized_keys) {
          trigger_error(format_string('Potentially unsafe destination removed from query string parameters (GET) because it contained the following keys: @keys', array('@keys' => implode(', ', $dangerous_keys))));
        }
        return TRUE;
      }
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/request-sanitizer.inc](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
