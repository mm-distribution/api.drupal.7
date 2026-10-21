# modules/simpletest/tests/system_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · 623 lines
- **Module/theme:** batch_test

## Functions (derived index)

- [system_test_menu()](system_test_menu.md) — Implements hook_menu().
- [system_test_sleep()](system_test_sleep.md)
- [system_test_basic_auth_page()](system_test_basic_auth_page.md)
- [system_test_redirect()](system_test_redirect.md)
- [system_test_multiple_redirects()](system_test_multiple_redirects.md) — Menu callback; sends a redirect header to itself until $count argument is 0.
- [system_test_set_header()](system_test_set_header.md)
- [system_test_redirect_noscheme()](system_test_redirect_noscheme.md)
- [system_test_redirect_protocol_relative()](system_test_redirect_protocol_relative.md)
- [system_test_redirect_noparse()](system_test_redirect_noparse.md)
- [system_test_redirect_invalid_scheme()](system_test_redirect_invalid_scheme.md)
- [system_test_page_cache_headers()](system_test_page_cache_headers.md) — Menu callback to test headers stored in the page cache.
- [system_test_modules_installed()](system_test_modules_installed.md) — Implements hook_modules_installed().
- [system_test_modules_enabled()](system_test_modules_enabled.md) — Implements hook_modules_enabled().
- [system_test_modules_disabled()](system_test_modules_disabled.md) — Implements hook_modules_disabled().
- [system_test_modules_uninstalled()](system_test_modules_uninstalled.md) — Implements hook_modules_uninstalled().
- [system_test_boot()](system_test_boot.md) — Implements hook_boot().
- [system_test_init()](system_test_init.md) — Implements hook_init().
- [system_test_exit()](system_test_exit.md) — Implements hook_exit().
- [system_test_system_info_alter()](system_test_system_info_alter.md) — Implements hook_system_info_alter().
- [system_test_lock_acquire()](system_test_lock_acquire.md) — Try to acquire a named lock and report the outcome.
- [system_test_lock_exit()](system_test_lock_exit.md) — Try to acquire a specific lock, and then exit.
- [system_test_page_build()](system_test_page_build.md) — Implements hook_page_build().
- [system_test_main_content_fallback()](system_test_main_content_fallback.md) — Menu callback to test main content fallback().
- [system_test_page_shutdown_functions()](system_test_page_shutdown_functions.md) — A simple page callback which adds a register shutdown function.
- [_system_test_first_shutdown_function()](_system_test_first_shutdown_function.md) — Dummy shutdown function which registers another shutdown function.
- [_system_test_second_shutdown_function()](_system_test_second_shutdown_function.md) — Dummy shutdown function.
- [system_test_filetransfer_info()](system_test_filetransfer_info.md) — Implements hook_filetransfer_info().
- [system_test_authorize_init_page()](system_test_authorize_init_page.md) — Page callback to initialize authorize.php during testing.
- [system_test_drupal_set_message()](system_test_drupal_set_message.md) — Sets two messages and removes the first one before the messages are displayed.
- [system_test_get_destination()](system_test_get_destination.md) — Page callback to print out $_GET['destination'] for testing.
- [system_test_request_destination()](system_test_request_destination.md) — Page callback to print out $_REQUEST['destination'] for testing.
- [system_test_drupal_get_filename()](system_test_drupal_get_filename.md) — Page callback to run drupal_get_filename() on a particular module.
- [system_test_drupal_get_filename_with_schema_rebuild()](system_test_drupal_get_filename_with_schema_rebuild.md) — Page callback to run drupal_get_filename() and do a schema rebuild.
- [system_test_empty_page()](system_test_empty_page.md) — Page callback to output an empty page.
- [system_test_watchdog()](system_test_watchdog.md) — Implements hook_watchdog().
- [system_test_module_implements_alter()](system_test_module_implements_alter.md) — Implements hook_module_implements_alter().

## Classes and interfaces (derived index)

- [SystemTestFileTransfer](SystemTestFileTransfer.md) — Mock FileTransfer object to test the settings form functionality.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
