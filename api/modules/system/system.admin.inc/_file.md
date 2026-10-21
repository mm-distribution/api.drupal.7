# modules/system/system.admin.inc

- **Source:** [local](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · 3270 lines
- **Module/theme:** system

## File documentation

```text
@file
Admin page callbacks for the system module.
```

## Functions (derived index)

- [system_admin_config_page()](system_admin_config_page.md) — Menu callback; Provide the administration overview page.
- [system_admin_menu_block_page()](system_admin_menu_block_page.md) — Provide a single block from the administration menu as a page.
- [system_admin_index()](system_admin_index.md) — Menu callback; prints a listing of admin tasks, organized by module.
- [system_settings_overview()](system_settings_overview.md) — Displays the configuration overview page.
- [system_themes_page()](system_themes_page.md) — Menu callback; displays a listing of all themes.
- [system_themes_admin_form()](system_themes_admin_form.md) — Form to select the administration theme.
- [system_themes_admin_form_submit()](system_themes_admin_form_submit.md) — Process system_themes_admin_form form submissions.
- [system_theme_enable()](system_theme_enable.md) — Menu callback; Enables a theme.
- [system_theme_disable()](system_theme_disable.md) — Menu callback; Disables a theme.
- [system_theme_default()](system_theme_default.md) — Menu callback; Set the default theme.
- [system_theme_settings()](system_theme_settings.md) — Form builder; display theme configuration for entire site and individual themes.
- [system_theme_settings_validate()](system_theme_settings_validate.md) — Validator for the system_theme_settings() form.
- [_system_theme_settings_validate_path()](_system_theme_settings_validate_path.md) — Helper function for the system_theme_settings form.
- [system_theme_settings_submit()](system_theme_settings_submit.md) — Process system_theme_settings form submissions.
- [_system_is_incompatible()](_system_is_incompatible.md) — Recursively check compatibility.
- [system_modules()](system_modules.md) — Menu callback; provides module enable/disable interface.
- [system_sort_modules_by_info_name()](system_sort_modules_by_info_name.md) — Array sorting callback; sorts modules or themes by their name.
- [system_sort_themes()](system_sort_themes.md) — Sorts themes by their names, with the default theme listed first.
- [_system_modules_build_row()](_system_modules_build_row.md) — Build a table row for the system modules page.
- [system_modules_confirm_form()](system_modules_confirm_form.md) — Display confirmation form for required modules.
- [system_modules_submit()](system_modules_submit.md) — Submit callback; handles modules form submission.
- [system_modules_uninstall()](system_modules_uninstall.md) — Builds a form of currently disabled modules.
- [system_modules_uninstall_confirm_form()](system_modules_uninstall_confirm_form.md) — Confirm uninstall of selected modules.
- [system_modules_uninstall_validate()](system_modules_uninstall_validate.md) — Validates the submitted uninstall form.
- [system_modules_uninstall_submit()](system_modules_uninstall_submit.md) — Processes the submitted uninstall form.
- [system_ip_blocking()](system_ip_blocking.md) — Menu callback. Display blocked IP addresses.
- [system_ip_blocking_form()](system_ip_blocking_form.md) — Define the form for blocking IP addresses.
- [system_ip_blocking_form_validate()](system_ip_blocking_form_validate.md)
- [system_ip_blocking_form_submit()](system_ip_blocking_form_submit.md)
- [system_ip_blocking_delete()](system_ip_blocking_delete.md) — IP deletion confirm page.
- [system_ip_blocking_delete_submit()](system_ip_blocking_delete_submit.md) — Process system_ip_blocking_delete form submissions.
- [system_site_information_settings()](system_site_information_settings.md) — Form builder; The general site information form.
- [system_site_information_settings_validate()](system_site_information_settings_validate.md) — Validates the submitted site-information form.
- [system_cron_settings()](system_cron_settings.md) — Form builder; Cron form.
- [system_run_cron_submit()](system_run_cron_submit.md) — Submit callback; run cron.
- [system_logging_settings()](system_logging_settings.md) — Form builder; Configure error reporting settings.
- [system_performance_settings()](system_performance_settings.md) — Form builder; Configure site performance settings.
- [system_clear_cache_submit()](system_clear_cache_submit.md) — Submit callback; clear system caches.
- [system_clear_page_cache_submit()](system_clear_page_cache_submit.md) — Submit callback; clear the page cache.
- [system_file_system_settings()](system_file_system_settings.md) — Form builder; Configure the site file handling.
- [system_image_toolkit_settings()](system_image_toolkit_settings.md) — Form builder; Configure site image toolkit usage.
- [system_rss_feeds_settings()](system_rss_feeds_settings.md) — Form builder; Configure how the site handles RSS feeds.
- [system_regional_settings()](system_regional_settings.md) — Form builder; Configure the site regional settings.
- [system_date_time_settings()](system_date_time_settings.md) — Form builder; Configure the site date and time settings.
- [theme_system_date_time_settings()](theme_system_date_time_settings.md) — Returns HTML for the date settings form.
- [system_add_date_format_type_form()](system_add_date_format_type_form.md) — Add new date type.
- [system_add_date_format_type_form_validate()](system_add_date_format_type_form_validate.md) — Validate system_add_date_format_type form submissions.
- [system_add_date_format_type_form_submit()](system_add_date_format_type_form_submit.md) — Process system_add_date_format_type form submissions.
- [system_date_time_lookup()](system_date_time_lookup.md) — Return the date for a given format string via Ajax.
- [system_site_maintenance_mode()](system_site_maintenance_mode.md) — Form builder; Configure the site's maintenance status.
- [system_clean_url_settings()](system_clean_url_settings.md) — Form builder; Configure clean URL settings.
- [system_status()](system_status.md) — Menu callback: displays the site status report. Can also be used as a pure check.
- [system_run_cron()](system_run_cron.md) — Menu callback: run cron manually.
- [system_php()](system_php.md) — Menu callback: return information about PHP.
- [system_batch_page()](system_batch_page.md) — Default page callback for batches.
- [theme_admin_block()](theme_admin_block.md) — Returns HTML for an administrative block for display.
- [theme_admin_block_content()](theme_admin_block_content.md) — Returns HTML for the content of an administrative block.
- [theme_admin_page()](theme_admin_page.md) — Returns HTML for an administrative page.
- [theme_system_admin_index()](theme_system_admin_index.md) — Returns HTML for the output of the dashboard page.
- [theme_status_report()](theme_status_report.md) — Returns HTML for the status report.
- [theme_system_modules_fieldset()](theme_system_modules_fieldset.md) — Returns HTML for the modules form.
- [theme_system_modules_incompatible()](theme_system_modules_incompatible.md) — Returns HTML for a message about incompatible modules.
- [theme_system_modules_uninstall()](theme_system_modules_uninstall.md) — Returns HTML for a table of currently disabled modules.
- [theme_system_themes_page()](theme_system_themes_page.md) — Returns HTML for the Appearance page.
- [system_date_delete_format_form()](system_date_delete_format_form.md) — Menu callback; present a form for deleting a date format.
- [system_date_delete_format_form_submit()](system_date_delete_format_form_submit.md) — Delete a configured date format.
- [system_delete_date_format_type_form()](system_delete_date_format_type_form.md) — Menu callback; present a form for deleting a date type.
- [system_delete_date_format_type_form_submit()](system_delete_date_format_type_form_submit.md) — Delete a configured date type.
- [system_date_time_formats()](system_date_time_formats.md) — Displays the date format strings overview page.
- [system_configure_date_formats_form()](system_configure_date_formats_form.md) — Allow users to add additional date formats.
- [system_add_date_formats_form_validate()](system_add_date_formats_form_validate.md) — Validate new date format string submission.
- [system_add_date_formats_form_submit()](system_add_date_formats_form_submit.md) — Process new date format string submission.
- [system_actions_manage()](system_actions_manage.md) — Menu callback; Displays an overview of available and configured actions.
- [system_actions_manage_form()](system_actions_manage_form.md) — Define the form for the actions overview page.
- [system_actions_manage_form_submit()](system_actions_manage_form_submit.md) — Process system_actions_manage form submissions.
- [system_actions_configure()](system_actions_configure.md) — Menu callback; Creates the form for configuration of a single action.
- [system_actions_configure_validate()](system_actions_configure_validate.md) — Validate system_actions_configure() form submissions.
- [system_actions_configure_submit()](system_actions_configure_submit.md) — Process system_actions_configure() form submissions.
- [system_actions_delete_form()](system_actions_delete_form.md) — Create the form for confirmation of deleting an action.
- [system_actions_delete_form_submit()](system_actions_delete_form_submit.md) — Process system_actions_delete form submissions.
- [system_action_delete_orphans_post()](system_action_delete_orphans_post.md) — Post-deletion operations for deleting action orphans.
- [system_actions_remove_orphans()](system_actions_remove_orphans.md) — Remove actions that are in the database but not supported by any enabled module.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
