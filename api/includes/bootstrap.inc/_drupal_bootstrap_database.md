# _drupal_bootstrap_database()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2797–2847 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2797-L2847)

## Signature

```php
function _drupal_bootstrap_database()
```

## Documentation

```text
Initializes the database system and registers autoload functions.
```

## Code

```php
function _drupal_bootstrap_database() {
  // Redirect the user to the installation script if Drupal has not been
  // installed yet (i.e., if no $databases array has been defined in the
  // settings.php file) and we are not already installing.
  if (empty($GLOBALS['databases']) && !drupal_installation_attempted()) {
    include_once DRUPAL_ROOT . '/includes/install.inc';
    install_goto('install.php');
  }

  // The user agent header is used to pass a database prefix in the request when
  // running tests. However, for security reasons, it is imperative that we
  // validate we ourselves made the request.
  if ($test_prefix = drupal_valid_test_ua()) {
    // Set the test run id for use in other parts of Drupal.
    $test_info = &$GLOBALS['drupal_test_info'];
    $test_info['test_run_id'] = $test_prefix;
    $test_info['in_child_site'] = TRUE;

    foreach ($GLOBALS['databases']['default'] as &$value) {
      // Extract the current default database prefix.
      if (!isset($value['prefix'])) {
        $current_prefix = '';
      }
      elseif (is_array($value['prefix'])) {
        $current_prefix = $value['prefix']['default'];
      }
      else {
        $current_prefix = $value['prefix'];
      }

      // Remove the current database prefix and replace it by our own.
      $value['prefix'] = array(
        'default' => $current_prefix . $test_prefix,
      );
    }
  }

  // Initialize the database system. Note that the connection
  // won't be initialized until it is actually requested.
  require_once DRUPAL_ROOT . '/includes/database/database.inc';

  // Register autoload functions so that we can access classes and interfaces.
  // The database autoload routine comes first so that we can load the database
  // system without hitting the database. That is especially important during
  // the install or upgrade process.
  spl_autoload_register('drupal_autoload_class');
  spl_autoload_register('drupal_autoload_interface');
  if (version_compare(PHP_VERSION, '5.4') >= 0) {
    spl_autoload_register('drupal_autoload_trait');
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
