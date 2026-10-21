# modules/update/update.module

- **Source:** [local](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · 998 lines
- **Module/theme:** update

## File documentation

```text
@file
Handles updates of Drupal core and contributed projects.

The module checks for available updates of Drupal core and any installed
contributed modules and themes. It warns site administrators if newer
releases are available via the system status report (admin/reports/status),
the module and theme pages, and optionally via e-mail. It also provides the
ability to install contributed modules and themes via an user interface.
```

## Functions (derived index)

- [update_help()](update_help.md) — Implements hook_help().
- [update_init()](update_init.md) — Implements hook_init().
- [update_menu()](update_menu.md) — Implements hook_menu().
- [update_manager_access()](update_manager_access.md) — Access callback: Resolves if the current user can access updater menu items.
- [update_theme()](update_theme.md) — Implements hook_theme().
- [update_cron()](update_cron.md) — Implements hook_cron().
- [update_themes_enabled()](update_themes_enabled.md) — Implements hook_themes_enabled().
- [update_themes_disabled()](update_themes_disabled.md) — Implements hook_themes_disabled().
- [update_form_system_modules_alter()](update_form_system_modules_alter.md) — Implements hook_form_FORM_ID_alter() for system_modules().
- [update_cache_clear_submit()](update_cache_clear_submit.md) — Form submission handler for system_modules().
- [_update_no_data()](_update_no_data.md) — Returns a warning message when there is no data about available updates.
- [update_get_available()](update_get_available.md) — Tries to get update information from cache and refreshes it when necessary.
- [update_create_fetch_task()](update_create_fetch_task.md) — Creates a new fetch task after loading the necessary include file.
- [update_refresh()](update_refresh.md) — Refreshes the release data after loading the necessary include file.
- [update_fetch_data()](update_fetch_data.md) — Attempts to fetch update data after loading the necessary include file.
- [_update_get_cached_available_releases()](_update_get_cached_available_releases.md) — Returns all currently cached data about available releases for all projects.
- [update_mail()](update_mail.md) — Implements hook_mail().
- [_update_message_text()](_update_message_text.md) — Returns the appropriate message text when site is out of date or not secure.
- [_update_project_status_sort()](_update_project_status_sort.md) — Orders projects based on their status.
- [theme_update_last_check()](theme_update_last_check.md) — Returns HTML for the last time we checked for update data.
- [update_verify_update_archive()](update_verify_update_archive.md) — Implements hook_verify_update_archive().
- [_update_cache_set()](_update_cache_set.md) — Stores data in the private update status cache table.
- [_update_cache_get()](_update_cache_get.md) — Retrieves data from the private update status cache table.
- [_update_get_cache_multiple()](_update_get_cache_multiple.md) — Returns an array of cache items with a given cache ID prefix.
- [_update_cache_clear()](_update_cache_clear.md) — Invalidates cached data relating to update status.
- [update_flush_caches()](update_flush_caches.md) — Implements hook_flush_caches().
- [_update_manager_unique_identifier()](_update_manager_unique_identifier.md) — Returns a short unique identifier for this Drupal installation.
- [_update_manager_extract_directory()](_update_manager_extract_directory.md) — Returns the directory where update archive files should be extracted.
- [_update_manager_cache_directory()](_update_manager_cache_directory.md) — Returns the directory where update archive files should be cached.
- [update_clear_update_disk_cache()](update_clear_update_disk_cache.md) — Clears the temporary files and directories based on file age from disk.
- [update_delete_file_if_stale()](update_delete_file_if_stale.md) — Deletes stale files and directories from the update manager disk cache.

## Constants

### UPDATE_DEFAULT_URL

- Line 17

```php
define('UPDATE_DEFAULT_URL', 'https://updates.drupal.org/release-history');
```

```text
URL to check for updates, if a given project doesn't define its own.
```

### UPDATE_NOT_SECURE

- Line 24

```php
define('UPDATE_NOT_SECURE', 1);
```

```text
Project is missing security update(s).
```

### UPDATE_REVOKED

- Line 29

```php
define('UPDATE_REVOKED', 2);
```

```text
Current release has been unpublished and is no longer available.
```

### UPDATE_NOT_SUPPORTED

- Line 34

```php
define('UPDATE_NOT_SUPPORTED', 3);
```

```text
Current release is no longer supported by the project maintainer.
```

### UPDATE_NOT_CURRENT

- Line 39

```php
define('UPDATE_NOT_CURRENT', 4);
```

```text
Project has a new release available, but it is not a security release.
```

### UPDATE_CURRENT

- Line 44

```php
define('UPDATE_CURRENT', 5);
```

```text
Project is up to date.
```

### UPDATE_NOT_CHECKED

- Line 49

```php
define('UPDATE_NOT_CHECKED', -1);
```

```text
Project's status cannot be checked.
```

### UPDATE_UNKNOWN

- Line 54

```php
define('UPDATE_UNKNOWN', -2);
```

```text
No available update data was found for project.
```

### UPDATE_NOT_FETCHED

- Line 59

```php
define('UPDATE_NOT_FETCHED', -3);
```

```text
There was a failure fetching available update data for this project.
```

### UPDATE_FETCH_PENDING

- Line 64

```php
define('UPDATE_FETCH_PENDING', -4);
```

```text
We need to (re)fetch available update data for this project.
```

### UPDATE_MAX_FETCH_ATTEMPTS

- Line 69

```php
define('UPDATE_MAX_FETCH_ATTEMPTS', 2);
```

```text
Maximum number of attempts to fetch available update data from a given host.
```

### UPDATE_MAX_FETCH_TIME

- Line 74

```php
define('UPDATE_MAX_FETCH_TIME', 30);
```

```text
Maximum number of seconds to try fetching available update data at a time.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
