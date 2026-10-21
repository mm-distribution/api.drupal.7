# update.php

- **Source:** [local](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php) · 508 lines

## File documentation

```text
@file
Administrative page for handling updates from one Drupal version to another.

Point your browser to "http://www.example.com/update.php" and follow the
instructions.

If you are not logged in using either the site maintenance account or an
account with the "Administer software updates" permission, you will need to
modify the access check statement inside your settings.php file. After
finishing the upgrade, be sure to open settings.php again, and change it
back to its original state!
```

## Functions (derived index)

- [update_selection_page()](update_selection_page.md) — Renders a form with a list of available database updates.
- [update_script_selection_form()](update_script_selection_form.md) — Form constructor for the list of available database module updates.
- [update_helpful_links()](update_helpful_links.md) — Provides links to the homepage and administration pages.
- [update_results_page()](update_results_page.md) — Displays results of the update script with any accompanying errors.
- [update_info_page()](update_info_page.md) — Provides an overview of the Drupal database update.
- [update_access_denied_page()](update_access_denied_page.md) — Renders a 403 access denied page for update.php.
- [update_access_allowed()](update_access_allowed.md) — Determines if the current user is allowed to run update.php.
- [update_task_list()](update_task_list.md) — Adds the update task list to the current page.
- [update_extra_requirements()](update_extra_requirements.md) — Returns and stores extra requirements that apply during the update process.
- [update_check_requirements()](update_check_requirements.md) — Checks update requirements and reports errors and (optionally) warnings.

## Constants

### DRUPAL_ROOT

- Line 6

```php
define('DRUPAL_ROOT', getcwd());
```

```text
Defines the root directory of the Drupal installation.
```

### MAINTENANCE_MODE

- Line 28

```php
define('MAINTENANCE_MODE', 'update');
```

```text
Global flag indicating that update.php is being run.

When this flag is set, various operations do not take place, such as invoking
hook_init() and hook_exit(), css/js preprocessing, and translation.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
