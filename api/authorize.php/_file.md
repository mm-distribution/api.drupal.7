# authorize.php

- **Source:** [local](../../source/authorize.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/authorize.php) · 175 lines

## File documentation

```text
@file
Administrative script for running authorized file operations.

Using this script, the site owner (the user actually owning the files on the
webserver) can authorize certain file-related operations to proceed with
elevated privileges, for example to deploy and upgrade modules or themes.
Users should not visit this page directly, but instead use an administrative
user interface which knows how to redirect the user to this script as part of
a multistep process. This script actually performs the selected operations
without loading all of Drupal, to be able to more gracefully recover from
errors. Access to the script is controlled by a global killswitch in
settings.php ('allow_authorize_operations') and via the 'administer software
updates' permission.

There are helper functions for setting up an operation to run via this
system in modules/system/system.module. For more information, see:
@link authorize Authorized operation helper functions @endlink
```

## Functions (derived index)

- [authorize_access_denied_page()](authorize_access_denied_page.md) — Renders a 403 access denied page for authorize.php.
- [authorize_access_allowed()](authorize_access_allowed.md) — Determines if the current user is allowed to run authorize.php.

## Constants

### DRUPAL_ROOT

- Line 26

```php
define('DRUPAL_ROOT', getcwd());
```

```text
Defines the root directory of the Drupal installation.
```

### MAINTENANCE_MODE

- Line 36

```php
define('MAINTENANCE_MODE', 'update');
```

```text
Global flag to identify update.php and authorize.php runs.

Identifies update.php and authorize.php runs, avoiding unwanted operations
such as hook_init() and hook_exit() invokes, css/js preprocessing and
translation, and solves some theming issues. The flag is checked in other
places in Drupal code (not just authorize.php).
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
