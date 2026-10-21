# _drupal_bootstrap_configuration()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2711–2736 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2711-L2736)

## Signature

```php
function _drupal_bootstrap_configuration()
```

## Documentation

```text
Sets up the script environment and loads settings.php.
```

## Code

```php
function _drupal_bootstrap_configuration() {
  // Set the Drupal custom error handler.
  set_error_handler('_drupal_error_handler');
  set_exception_handler('_drupal_exception_handler');

  drupal_environment_initialize();
  // Start a page timer:
  timer_start('page');
  // Initialize the configuration, including variables from settings.php.
  drupal_settings_initialize();

  // Check trusted HTTP Host headers to protect against header attacks.
  if (PHP_SAPI !== 'cli') {
    $host_patterns = variable_get('trusted_host_patterns', array());
    if (!empty($host_patterns)) {
      if (!drupal_check_trusted_hosts($_SERVER['HTTP_HOST'], $host_patterns)) {
        header($_SERVER['SERVER_PROTOCOL'] . ' 400 Bad Request');
        print 'The provided host name is not valid for this server.';
        exit;
      }
    }
  }

  // Sanitize unsafe keys from the request.
  DrupalRequestSanitizer::sanitize();
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
