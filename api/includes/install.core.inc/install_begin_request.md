# install_begin_request()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 210–308 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L210-L308)

## Signature

```php
function install_begin_request(&$install_state)
```

## Documentation

```text
Begins an installation request, modifying the installation state as needed.

This function performs commands that must run at the beginning of every page
request. It throws an exception if the installation should not proceed.

@param $install_state
  An array of information about the current installation state. This is
  modified with information gleaned from the beginning of the page request.
```

## Code

```php
function install_begin_request(&$install_state) {
  // Add any installation parameters passed in via the URL.
  $install_state['parameters'] += $_GET;

  // Validate certain core settings that are used throughout the installation.
  if (!empty($install_state['parameters']['profile'])) {
    $install_state['parameters']['profile'] = preg_replace('/[^a-zA-Z_0-9]/', '', $install_state['parameters']['profile']);
  }
  if (!empty($install_state['parameters']['locale'])) {
    $install_state['parameters']['locale'] = preg_replace('/[^a-zA-Z_0-9\-]/', '', $install_state['parameters']['locale']);
  }

  // Allow command line scripts to override server variables used by Drupal.
  require_once DRUPAL_ROOT . '/includes/bootstrap.inc';
  if (!$install_state['interactive']) {
    drupal_override_server_variables($install_state['server']);
  }

  // The user agent header is used to pass a database prefix in the request when
  // running tests. However, for security reasons, it is imperative that no
  // installation be permitted using such a prefix.
  if (isset($_SERVER['HTTP_USER_AGENT']) && strpos($_SERVER['HTTP_USER_AGENT'], "simpletest") !== FALSE) {
    header($_SERVER['SERVER_PROTOCOL'] . ' 403 Forbidden');
    exit;
  }

  drupal_bootstrap(DRUPAL_BOOTSTRAP_CONFIGURATION);

  // This must go after drupal_bootstrap(), which unsets globals!
  global $conf;

  require_once DRUPAL_ROOT . '/modules/system/system.install';
  require_once DRUPAL_ROOT . '/includes/common.inc';
  require_once DRUPAL_ROOT . '/includes/file.inc';
  require_once DRUPAL_ROOT . '/includes/install.inc';
  require_once DRUPAL_ROOT . '/' . variable_get('path_inc', 'includes/path.inc');

  // Load module basics (needed for hook invokes).
  include_once DRUPAL_ROOT . '/includes/module.inc';
  include_once DRUPAL_ROOT . '/includes/session.inc';

  // Set up $language, so t() caller functions will still work.
  drupal_language_initialize();

  include_once DRUPAL_ROOT . '/includes/entity.inc';
  require_once DRUPAL_ROOT . '/includes/ajax.inc';
  $module_list['system']['filename'] = 'modules/system/system.module';
  $module_list['user']['filename'] = 'modules/user/user.module';
  module_list(TRUE, FALSE, FALSE, $module_list);
  drupal_load('module', 'system');
  drupal_load('module', 'user');

  // Load the cache infrastructure using a "fake" cache implementation that
  // does not attempt to write to the database. We need this during the initial
  // part of the installer because the database is not available yet. We
  // continue to use it even when the database does become available, in order
  // to preserve consistency between interactive and command-line installations
  // (the latter complete in one page request and therefore are forced to
  // continue using the cache implementation they started with) and also
  // because any data put in the cache during the installer is inherently
  // suspect, due to the fact that Drupal is not fully set up yet.
  require_once DRUPAL_ROOT . '/includes/cache.inc';
  require_once DRUPAL_ROOT . '/includes/cache-install.inc';
  $conf['cache_default_class'] = 'DrupalFakeCache';

  // Prepare for themed output. We need to run this at the beginning of the
  // page request to avoid a different theme accidentally getting set. (We also
  // need to run it even in the case of command-line installations, to prevent
  // any code in the installer that happens to initialize the theme system from
  // accessing the database before it is set up yet.)
  drupal_maintenance_theme();

  // Check existing settings.php.
  $install_state['settings_verified'] = install_verify_settings();

  if ($install_state['settings_verified']) {
    // Initialize the database system. Note that the connection
    // won't be initialized until it is actually requested.
    require_once DRUPAL_ROOT . '/includes/database/database.inc';

    // Verify the last completed task in the database, if there is one.
    $task = install_verify_completed_task();
  }
  else {
    $task = NULL;

    // Do not install over a configured settings.php. Check the 'db_url'
    // variable in addition to 'databases', since previous versions of Drupal
    // used that (and we do not want to allow installations on an existing site
    // whose settings file has not yet been updated).
    if (!empty($GLOBALS['databases']) || !empty($GLOBALS['db_url'])) {
      throw new Exception(install_already_done_error());
    }
  }

  // Modify the installation state as appropriate.
  $install_state['completed_task'] = $task;
  $install_state['database_tables_exist'] = !empty($task);
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
