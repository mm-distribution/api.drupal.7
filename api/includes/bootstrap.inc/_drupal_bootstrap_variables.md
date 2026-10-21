# _drupal_bootstrap_variables()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2852–2889 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2852-L2889)

## Signature

```php
function _drupal_bootstrap_variables()
```

## Documentation

```text
Loads system variables and all enabled bootstrap modules.
```

## Code

```php
function _drupal_bootstrap_variables() {
  global $conf;

  // Initialize the lock system.
  require_once DRUPAL_ROOT . '/' . variable_get('lock_inc', 'includes/lock.inc');
  lock_initialize();

  // Load variables from the database, but do not overwrite variables set in settings.php.
  $conf = variable_initialize(isset($conf) ? $conf : array());
  // Load bootstrap modules.
  require_once DRUPAL_ROOT . '/includes/module.inc';
  module_load_all(TRUE);

  // Sanitize the destination parameter (which is often used for redirects) to
  // prevent open redirect attacks leading to other domains. Sanitize both
  // $_GET['destination'] and $_REQUEST['destination'] to protect code that
  // relies on either, but do not sanitize $_POST to avoid interfering with
  // unrelated form submissions. The sanitization happens here because
  // url_is_external() requires the variable system to be available.
  if (isset($_GET['destination']) || isset($_REQUEST['destination'])) {
    require_once DRUPAL_ROOT . '/includes/common.inc';
    // If the destination is an external URL, remove it.
    if (isset($_GET['destination']) && url_is_external($_GET['destination'])) {
      unset($_GET['destination']);
      unset($_REQUEST['destination']);
    }
    // Use the DrupalRequestSanitizer to ensure that the destination's query
    // parameters are not dangerous.
    if (isset($_GET['destination'])) {
      DrupalRequestSanitizer::cleanDestination();
    }
    // If there's still something in $_REQUEST['destination'] that didn't come
    // from $_GET, check it too.
    if (isset($_REQUEST['destination']) && (!isset($_GET['destination']) || $_REQUEST['destination'] != $_GET['destination']) && url_is_external($_REQUEST['destination'])) {
      unset($_REQUEST['destination']);
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
