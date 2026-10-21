# modules/system/system.module

- **Source:** [local](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · 4150 lines
- **Module/theme:** system

## File documentation

```text
@file
Configuration system that lets administrators modify the workings of the site.
```

## Functions (derived index)

- [system_help()](system_help.md) — Implements hook_help().
- [system_theme()](system_theme.md) — Implements hook_theme().
- [system_permission()](system_permission.md) — Implements hook_permission().
- [system_hook_info()](system_hook_info.md) — Implements hook_hook_info().
- [system_entity_info()](system_entity_info.md) — Implements hook_entity_info().
- [system_element_info()](system_element_info.md) — Implements hook_element_info().
- [system_menu()](system_menu.md) — Implements hook_menu().
- [_system_batch_theme()](_system_batch_theme.md) — Theme callback for the default batch page.
- [system_library()](system_library.md) — Implements hook_library().
- [system_stream_wrappers()](system_stream_wrappers.md) — Implements hook_stream_wrappers().
- [blocked_ip_load()](blocked_ip_load.md) — Retrieve a blocked IP address from the database.
- [_system_themes_access()](_system_themes_access.md) — Menu item access callback - only admin or enabled themes can be accessed.
- [system_authorized_init()](system_authorized_init.md) — Setup a given callback to run via authorize.php with elevated privileges.
- [system_authorized_get_url()](system_authorized_get_url.md) — Return the URL for the authorize.php script.
- [system_authorized_batch_processing_url()](system_authorized_batch_processing_url.md) — Returns the URL for the authorize.php script when it is processing a batch.
- [system_authorized_run()](system_authorized_run.md) — Setup and invoke an operation using authorize.php.
- [system_authorized_batch_process()](system_authorized_batch_process.md) — Use authorize.php to run batch_process().
- [system_updater_info()](system_updater_info.md) — Implements hook_updater_info().
- [system_filetransfer_info()](system_filetransfer_info.md) — Implements hook_filetransfer_info().
- [system_init()](system_init.md) — Implements hook_init().
- [system_add_module_assets()](system_add_module_assets.md) — Adds CSS and JavaScript files declared in module .info files.
- [system_custom_theme()](system_custom_theme.md) — Implements hook_custom_theme().
- [system_form_user_profile_form_alter()](system_form_user_profile_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [system_form_user_register_form_alter()](system_form_user_register_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [system_user_login()](system_user_login.md) — Implements hook_user_login().
- [system_user_timezone()](system_user_timezone.md) — Add the time zone field to the user edit and register forms.
- [system_block_info()](system_block_info.md) — Implements hook_block_info().
- [system_block_view()](system_block_view.md) — Implements hook_block_view().
- [system_preprocess_block()](system_preprocess_block.md) — Implements hook_preprocess_block().
- [system_admin_menu_block()](system_admin_menu_block.md) — Provide a single block on the administration overview page.
- [system_check_directory()](system_check_directory.md) — Checks the existence of the directory specified in $form_element.
- [system_get_files_database()](system_get_files_database.md) — Retrieves the current status of an array of files in the system table.
- [system_update_files_database()](system_update_files_database.md) — Updates the records in the system table based on the files array.
- [system_get_info()](system_get_info.md) — Returns an array of information about enabled modules or themes.
- [_system_rebuild_module_data()](_system_rebuild_module_data.md) — Helper function to scan and collect module .info data.
- [system_rebuild_module_data()](system_rebuild_module_data.md) — Rebuild, save, and return data about all currently available modules.
- [_system_update_bootstrap_status()](_system_update_bootstrap_status.md) — Refresh bootstrap column in the system table.
- [_system_rebuild_theme_data()](_system_rebuild_theme_data.md) — Helper function to scan and collect theme .info data and their engines.
- [system_rebuild_theme_data()](system_rebuild_theme_data.md) — Rebuild, save, and return data about all currently available themes.
- [_system_info_add_path()](_system_info_add_path.md) — Prefixes all values in an .info file array with a given path.
- [_system_default_theme_features()](_system_default_theme_features.md) — Returns an array of default theme features.
- [system_find_base_themes()](system_find_base_themes.md) — Find all the base themes for the specified theme.
- [system_region_list()](system_region_list.md) — Get a list of available regions from a specified theme.
- [system_system_info_alter()](system_system_info_alter.md) — Implements hook_system_info_alter().
- [system_default_region()](system_default_region.md) — Get the name of the default region for a given theme.
- [system_settings_form()](system_settings_form.md) — Sets up a form to save information automatically.
- [system_settings_form_submit()](system_settings_form_submit.md) — Form submission handler for system_settings_form().
- [_system_sort_requirements()](_system_sort_requirements.md) — Helper function to sort requirements.
- [confirm_form()](confirm_form.md) — Generates a form array for a confirmation form.
- [system_admin_compact_mode()](system_admin_compact_mode.md) — Determines whether the current user is in compact mode.
- [system_admin_compact_page()](system_admin_compact_page.md) — Menu callback; Sets whether the admin menu is in compact mode or not.
- [system_get_module_admin_tasks()](system_get_module_admin_tasks.md) — Generate a list of tasks offered by a specified module.
- [system_cron()](system_cron.md) — Implements hook_cron().
- [system_flush_caches()](system_flush_caches.md) — Implements hook_flush_caches().
- [system_action_info()](system_action_info.md) — Implements hook_action_info().
- [system_send_email_action_form()](system_send_email_action_form.md) — Return a form definition so the Send email action can be configured.
- [system_send_email_action_validate()](system_send_email_action_validate.md) — Validate system_send_email_action form submissions.
- [system_send_email_action_submit()](system_send_email_action_submit.md) — Process system_send_email_action form submissions.
- [system_send_email_action()](system_send_email_action.md) — Sends an e-mail message.
- [system_mail()](system_mail.md) — Implements hook_mail().
- [system_message_action_form()](system_message_action_form.md)
- [system_message_action_submit()](system_message_action_submit.md)
- [system_message_action()](system_message_action.md) — Sends a message to the current user's screen.
- [system_goto_action_form()](system_goto_action_form.md) — Settings form for system_goto_action().
- [system_goto_action_submit()](system_goto_action_submit.md)
- [system_goto_action()](system_goto_action.md) — Redirects to a different URL.
- [system_block_ip_action()](system_block_ip_action.md) — Blocks the current user's IP address.
- [system_time_zones()](system_time_zones.md) — Generate an array of time zones and their local time&date.
- [system_check_http_request()](system_check_http_request.md) — Checks whether the server is capable of issuing HTTP requests.
- [system_timezone()](system_timezone.md) — Menu callback; Retrieve a JSON object containing a suggested time zone name.
- [theme_system_powered_by()](theme_system_powered_by.md) — Returns HTML for the Powered by Drupal text.
- [theme_system_compact_link()](theme_system_compact_link.md) — Returns HTML for a link to show or hide inline help descriptions.
- [system_image_toolkits()](system_image_toolkits.md) — Implements hook_image_toolkits().
- [system_retrieve_file()](system_retrieve_file.md) — Attempts to get a file using drupal_http_request and to store it locally.
- [system_page_alter()](system_page_alter.md) — Implements hook_page_alter().
- [system_run_automated_cron()](system_run_automated_cron.md) — Run the automated cron if enabled.
- [system_get_date_types()](system_get_date_types.md) — Gets the list of available date types and attributes.
- [system_date_format_types()](system_date_format_types.md) — Implements hook_date_format_types().
- [system_date_formats()](system_date_formats.md) — Implements hook_date_formats().
- [system_get_date_formats()](system_get_date_formats.md) — Gets the list of defined date formats and attributes.
- [system_get_date_format()](system_get_date_format.md) — Gets the format details for a particular format ID.
- [system_date_formats_rebuild()](system_date_formats_rebuild.md) — Resets the database cache of date formats and saves all new date formats.
- [system_date_format_locale()](system_date_format_locale.md) — Gets the appropriate date format string for a date type and locale.
- [_system_date_format_types_build()](_system_date_format_types_build.md) — Builds and returns information about available date types.
- [_system_date_formats_build()](_system_date_formats_build.md) — Builds and returns information about available date formats.
- [system_date_format_type_save()](system_date_format_type_save.md) — Saves a date type to the database.
- [system_date_format_type_delete()](system_date_format_type_delete.md) — Deletes a date type from the database.
- [system_date_format_save()](system_date_format_save.md) — Saves a date format to the database.
- [system_date_format_delete()](system_date_format_delete.md) — Deletes a date format from the database.
- [system_archiver_info()](system_archiver_info.md) — Implements hook_archiver_info().
- [theme_confirm_form()](theme_confirm_form.md) — Returns HTML for a confirmation form.
- [theme_system_settings_form()](theme_system_settings_form.md) — Returns HTML for a system settings form.
- [theme_exposed_filters()](theme_exposed_filters.md) — Returns HTML for an exposed filter form.
- [system_admin_paths()](system_admin_paths.md) — Implements hook_admin_paths().
- [system_file_download()](system_file_download.md) — Implements hook_file_download().
- [system_registry_files_alter()](system_registry_files_alter.md) — Implements hook_registry_files_alter

## Constants

### DRUPAL_MAXIMUM_TEMP_FILE_AGE

- Line 11

```php
define('DRUPAL_MAXIMUM_TEMP_FILE_AGE', 21600);
```

```text
Maximum age of temporary files in seconds.
```

### DRUPAL_CRON_DEFAULT_THRESHOLD

- Line 16

```php
define('DRUPAL_CRON_DEFAULT_THRESHOLD', 10800);
```

```text
Default interval for automatic cron executions in seconds.
```

### DRUPAL_CRON_DETAILED_LOGGING

- Line 21

```php
define('DRUPAL_CRON_DETAILED_LOGGING', 0);
```

```text
Detailed cron logging disabled by default.
```

### DRUPAL_USER_TIMEZONE_DEFAULT

- Line 26

```php
define('DRUPAL_USER_TIMEZONE_DEFAULT', 0);
```

```text
New users will be set to the default time zone at registration.
```

### DRUPAL_USER_TIMEZONE_EMPTY

- Line 31

```php
define('DRUPAL_USER_TIMEZONE_EMPTY', 1);
```

```text
New users will get an empty time zone at registration.
```

### DRUPAL_USER_TIMEZONE_SELECT

- Line 36

```php
define('DRUPAL_USER_TIMEZONE_SELECT', 2);
```

```text
New users will select their own timezone at registration.
```

### DRUPAL_DISABLED

- Line 41

```php
define('DRUPAL_DISABLED', 0);
```

```text
Disabled option on forms and settings
```

### DRUPAL_OPTIONAL

- Line 46

```php
define('DRUPAL_OPTIONAL', 1);
```

```text
Optional option on forms and settings
```

### DRUPAL_REQUIRED

- Line 51

```php
define('DRUPAL_REQUIRED', 2);
```

```text
Required option on forms and settings
```

### DRUPAL_WEIGHT_SELECT_MAX

- Line 58

```php
define('DRUPAL_WEIGHT_SELECT_MAX', 100);
```

```text
Maximum number of values in a weight select element.

If the number of values is over the maximum, a text field is used instead.
```

### REGIONS_VISIBLE

- Line 65

```php
define('REGIONS_VISIBLE', 'visible');
```

```text
Return only visible regions.

@see system_region_list()
```

### REGIONS_ALL

- Line 72

```php
define('REGIONS_ALL', 'all');
```

```text
Return all regions.

@see system_region_list()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
