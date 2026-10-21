# install_system_module()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 785–819 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L785-L819)

## Signature

```php
function install_system_module(&$install_state)
```

## Documentation

```text
Installation task; install the Drupal system module.

@param $install_state
  An array of information about the current installation state.
```

## Code

```php
function install_system_module(&$install_state) {
  // Install system.module.
  drupal_install_system();

  // Call file_ensure_htaccess() to ensure that all of Drupal's standard
  // directories (e.g., the public and private files directories) have
  // appropriate .htaccess files. These directories will have already been
  // created by this point in the installer, since Drupal creates them during
  // the install_verify_requirements() task. Note that we cannot call
  // file_ensure_htaccess() any earlier than this, since it relies on
  // system.module in order to work.
  file_ensure_htaccess();

  // Enable the user module so that sessions can be recorded during the
  // upcoming bootstrap step.
  module_enable(array('user'), FALSE);

  // Save the list of other modules to install for the upcoming tasks.
  // variable_set() can be used now that system.module is installed.
  $modules = $install_state['profile_info']['dependencies'];

  // The installation profile is also a module, which needs to be installed
  // after all the dependencies have been installed.
  $modules[] = drupal_get_profile();

  variable_set('install_profile_modules', array_diff($modules, array('system')));
  $install_state['database_tables_exist'] = TRUE;

  // Prevent the hook_requirements() check from telling us to convert the
  // database to utf8mb4.
  $connection = Database::getConnection();
  if ($connection->utf8mb4IsConfigurable() && $connection->utf8mb4IsActive()) {
    variable_set('drupal_all_databases_are_utf8mb4', TRUE);
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
