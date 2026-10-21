# drupal_valid_test_ua()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2922–2948 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2922-L2948)

## Signature

```php
function drupal_valid_test_ua()
```

## Documentation

```text
Returns the test prefix if this is an internal request from SimpleTest.

@return
  Either the simpletest prefix (the string "simpletest" followed by any
  number of digits) or FALSE if the user agent does not contain a valid
  HMAC and timestamp.
```

## Code

```php
function drupal_valid_test_ua() {
  // No reason to reset this.
  static $test_prefix;

  if (isset($test_prefix)) {
    return $test_prefix;
  }

  if (isset($_SERVER['HTTP_USER_AGENT']) && preg_match("/^(simpletest\d+);(.+);(.+);(.+)$/", $_SERVER['HTTP_USER_AGENT'], $matches)) {
    list(, $prefix, $time, $salt, $hmac) = $matches;
    $check_string =  $prefix . ';' . $time . ';' . $salt;
    // We use the salt from settings.php to make the HMAC key, since
    // the database is not yet initialized and we can't access any Drupal variables.
    // The file properties add more entropy not easily accessible to others.
    $key = drupal_get_hash_salt() . filectime(__FILE__) . fileinode(__FILE__);
    $time_diff = REQUEST_TIME - $time;
    // Since we are making a local request a 5 second time window is allowed,
    // and the HMAC must match.
    if ($time_diff >= 0 && $time_diff <= 5 && $hmac == drupal_hmac_base64($check_string, $key)) {
      $test_prefix = $prefix;
      return $test_prefix;
    }
  }

  $test_prefix = FALSE;
  return $test_prefix;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
