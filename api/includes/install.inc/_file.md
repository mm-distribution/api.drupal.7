# includes/install.inc

- **Source:** [local](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · 1347 lines

## File documentation

```text
@file
API functions for installing modules and themes.
```

## Functions (derived index)

- [drupal_load_updates()](drupal_load_updates.md) — Loads .install files for installed modules to initialize the update system.
- [drupal_get_schema_versions()](drupal_get_schema_versions.md) — Returns an array of available schema versions for a module.
- [drupal_get_installed_schema_version()](drupal_get_installed_schema_version.md) — Returns the currently installed schema version for a module.
- [drupal_set_installed_schema_version()](drupal_set_installed_schema_version.md) — Update the installed version information for a module.
- [drupal_install_profile_distribution_name()](drupal_install_profile_distribution_name.md) — Loads the installation profile, extracting its defined distribution name.
- [drupal_detect_baseurl()](drupal_detect_baseurl.md) — Detects the base URL using the PHP $_SERVER variables.
- [drupal_detect_database_types()](drupal_detect_database_types.md) — Detects all supported databases that are compiled into PHP.
- [drupal_get_database_types()](drupal_get_database_types.md) — Returns all supported database installer objects that are compiled into PHP.
- [drupal_rewrite_settings()](drupal_rewrite_settings.md) — Replaces values in settings.php with values in the submitted array.
- [drupal_verify_profile()](drupal_verify_profile.md) — Verifies an installation profile for installation.
- [drupal_install_system()](drupal_install_system.md) — Installs the system module.
- [drupal_uninstall_modules()](drupal_uninstall_modules.md) — Uninstalls a given list of disabled modules.
- [drupal_verify_install_file()](drupal_verify_install_file.md) — Verifies the state of the specified file.
- [drupal_install_mkdir()](drupal_install_mkdir.md) — Creates a directory with the specified permissions.
- [drupal_install_fix_file()](drupal_install_fix_file.md) — Attempts to fix file permissions.
- [install_goto()](install_goto.md) — Sends the user to a different installer page.
- [drupal_current_script_url()](drupal_current_script_url.md) — Returns the URL of the current script, with modified query parameters.
- [drupal_requirements_url()](drupal_requirements_url.md) — Returns a URL for proceeding to the next page after a requirements problem.
- [st()](st.md) — Translates a string when some systems are not available.
- [drupal_check_profile()](drupal_check_profile.md) — Checks an installation profile's requirements.
- [drupal_requirements_severity()](drupal_requirements_severity.md) — Extracts the highest severity from the requirements array.
- [drupal_check_module()](drupal_check_module.md) — Checks a module's requirements.
- [install_profile_info()](install_profile_info.md) — Retrieves information about an installation profile from its .info file.
- [db_run_tasks()](db_run_tasks.md) — Ensures the environment for a Drupal database on a predefined connection.
- [db_installer_object()](db_installer_object.md) — Returns a database installer object.

## Classes and interfaces (derived index)

- [DatabaseTasks](DatabaseTasks.md) — Database installer structure.
- [DatabaseTaskException](DatabaseTaskException.md) — Exception thrown if the database installer fails.

## Constants

### SCHEMA_UNINSTALLED

- Line 11

```php
define('SCHEMA_UNINSTALLED', -1);
```

```text
Indicates that a module has not been installed yet.
```

### SCHEMA_INSTALLED

- Line 16

```php
define('SCHEMA_INSTALLED', 0);
```

```text
Indicates that a module has been installed.
```

### REQUIREMENT_INFO

- Line 21

```php
define('REQUIREMENT_INFO', -1);
```

```text
Requirement severity -- Informational message only.
```

### REQUIREMENT_OK

- Line 26

```php
define('REQUIREMENT_OK', 0);
```

```text
Requirement severity -- Requirement successfully met.
```

### REQUIREMENT_WARNING

- Line 31

```php
define('REQUIREMENT_WARNING', 1);
```

```text
Requirement severity -- Warning condition; proceed but flag warning.
```

### REQUIREMENT_ERROR

- Line 36

```php
define('REQUIREMENT_ERROR', 2);
```

```text
Requirement severity -- Error condition; abort installation.
```

### FILE_EXIST

- Line 41

```php
define('FILE_EXIST', 1);
```

```text
File permission check -- File exists.
```

### FILE_READABLE

- Line 46

```php
define('FILE_READABLE', 2);
```

```text
File permission check -- File is readable.
```

### FILE_WRITABLE

- Line 51

```php
define('FILE_WRITABLE', 4);
```

```text
File permission check -- File is writable.
```

### FILE_EXECUTABLE

- Line 56

```php
define('FILE_EXECUTABLE', 8);
```

```text
File permission check -- File is executable.
```

### FILE_NOT_EXIST

- Line 61

```php
define('FILE_NOT_EXIST', 16);
```

```text
File permission check -- File does not exist.
```

### FILE_NOT_READABLE

- Line 66

```php
define('FILE_NOT_READABLE', 32);
```

```text
File permission check -- File is not readable.
```

### FILE_NOT_WRITABLE

- Line 71

```php
define('FILE_NOT_WRITABLE', 64);
```

```text
File permission check -- File is not writable.
```

### FILE_NOT_EXECUTABLE

- Line 76

```php
define('FILE_NOT_EXECUTABLE', 128);
```

```text
File permission check -- File is not executable.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
