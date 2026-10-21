# drupal_generate_test_ua()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2953–2966 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2953-L2966)

## Signature

```php
function drupal_generate_test_ua($prefix)
```

## Documentation

```text
Generates a user agent string with a HMAC and timestamp for simpletest.
```

## Code

```php
function drupal_generate_test_ua($prefix) {
  static $key;

  if (!isset($key)) {
    // We use the salt from settings.php to make the HMAC key, since
    // the database is not yet initialized and we can't access any Drupal variables.
    // The file properties add more entropy not easily accessible to others.
    $key = drupal_get_hash_salt() . filectime(__FILE__) . fileinode(__FILE__);
  }
  // Generate a moderately secure HMAC based on the database credentials.
  $salt = uniqid('', TRUE);
  $check_string = $prefix . ';' . time() . ';' . $salt;
  return $check_string . ';' . drupal_hmac_base64($check_string, $key);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
