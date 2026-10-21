# includes/install.core.inc

- **Source:** [local](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · 1937 lines

## File documentation

```text
@file
API functions for installing Drupal.
```

## Functions (derived index)

- [install_drupal()](install_drupal.md) — Installs Drupal either interactively or via an array of passed-in settings.
- [install_state_defaults()](install_state_defaults.md) — Returns an array of default settings for the global installation state.
- [install_begin_request()](install_begin_request.md) — Begins an installation request, modifying the installation state as needed.
- [install_run_tasks()](install_run_tasks.md) — Runs all tasks for the current installation request.
- [install_run_task()](install_run_task.md) — Runs an individual installation task.
- [install_tasks_to_perform()](install_tasks_to_perform.md) — Returns a list of tasks to perform during the current installation request.
- [install_tasks()](install_tasks.md) — Returns a list of all tasks the installer currently knows about.
- [install_tasks_to_display()](install_tasks_to_display.md) — Returns a list of tasks that should be displayed to the end user.
- [install_redirect_url()](install_redirect_url.md) — Returns the URL that should be redirected to during an installation request.
- [install_full_redirect_url()](install_full_redirect_url.md) — Returns the complete URL redirected to during an installation request.
- [install_display_output()](install_display_output.md) — Displays themed installer output and ends the page request.
- [install_verify_requirements()](install_verify_requirements.md) — Verifies the requirements for installing Drupal.
- [install_system_module()](install_system_module.md) — Installation task; install the Drupal system module.
- [install_verify_completed_task()](install_verify_completed_task.md) — Verifies and returns the last installation task that was completed.
- [install_verify_settings()](install_verify_settings.md) — Verifies the existing settings in settings.php.
- [install_verify_pdo()](install_verify_pdo.md) — Verifies the PDO library.
- [install_settings_form()](install_settings_form.md) — Form constructor for a form to configure and rewrite settings.php.
- [install_settings_form_validate()](install_settings_form_validate.md) — Form validation handler for install_settings_form().
- [install_database_errors()](install_database_errors.md) — Checks a database connection and returns any errors.
- [install_settings_form_submit()](install_settings_form_submit.md) — Form submission handler for install_settings_form().
- [install_find_profiles()](install_find_profiles.md) — Finds all .profile files.
- [install_select_profile()](install_select_profile.md) — Selects which profile to install.
- [_install_select_profile()](_install_select_profile.md) — Selects an installation profile.
- [install_select_profile_form()](install_select_profile_form.md) — Form constructor for the profile selection form.
- [install_find_locales()](install_find_locales.md) — Find all .po files for the current profile.
- [install_select_locale()](install_select_locale.md) — Installation task; select which locale to use for the current profile.
- [install_select_locale_form()](install_select_locale_form.md) — Form constructor for the language selection form.
- [install_no_profile_error()](install_no_profile_error.md) — Indicates that there are no profiles available.
- [install_already_done_error()](install_already_done_error.md) — Indicates that Drupal has already been installed.
- [install_load_profile()](install_load_profile.md) — Loads information about the chosen profile during installation.
- [install_bootstrap_full()](install_bootstrap_full.md) — Performs a full bootstrap of Drupal during installation.
- [install_profile_modules()](install_profile_modules.md) — Installs required modules via a batch process.
- [install_import_locales()](install_import_locales.md) — Imports languages via a batch process during installation.
- [install_configure_form()](install_configure_form.md) — Form constructor for a form to configure the new site.
- [install_import_locales_remaining()](install_import_locales_remaining.md) — Installation task; import remaining languages via a batch process.
- [install_finished()](install_finished.md) — Finishes importing files at end of installation.
- [_install_module_batch()](_install_module_batch.md) — Implements callback_batch_operation().
- [_install_profile_modules_finished()](_install_profile_modules_finished.md) — Implements callback_batch_finished().
- [install_check_requirements()](install_check_requirements.md) — Checks installation requirements and reports any errors.
- [_install_configure_form()](_install_configure_form.md) — Form constructor for a site configuration form.
- [install_configure_form_validate()](install_configure_form_validate.md) — Form validation handler for install_configure_form().
- [install_configure_form_submit()](install_configure_form_submit.md) — Form submission handler for install_configure_form().

## Constants

### INSTALL_TASK_SKIP

- Line 19

```php
define('INSTALL_TASK_SKIP', 1);
```

```text
Do not run the task during the current installation request.

This can be used to skip running an installation task when certain
conditions are met, even though the task may still show on the list of
installation tasks presented to the user. For example, the Drupal installer
uses this flag to skip over the database configuration form when valid
database connection information is already available from settings.php. It
also uses this flag to skip language import tasks when the installation is
being performed in English.
```

### INSTALL_TASK_RUN_IF_REACHED

- Line 26

```php
define('INSTALL_TASK_RUN_IF_REACHED', 2);
```

```text
Run the task on each installation request until the database is set up.

This is primarily used by the Drupal installer for bootstrap-related tasks.
```

### INSTALL_TASK_RUN_IF_NOT_COMPLETED

- Line 40

```php
define('INSTALL_TASK_RUN_IF_NOT_COMPLETED', 3);
```

```text
Global flag to indicate that a task should be run on each installation
request that reaches it, until the database is set up and we are able to
record the fact that it already ran.

This is the default method for running tasks and should be used for most
tasks that occur after the database is set up; these tasks will then run
once and be marked complete once they are successfully finished. For
example, the Drupal installer uses this flag for the batch installation of
modules on the new site, and also for the configuration form that collects
basic site information and sets up the site maintenance account.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
