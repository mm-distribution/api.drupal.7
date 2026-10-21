# modules/simpletest/simpletest.module

- **Source:** [local](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · 656 lines
- **Module/theme:** simpletest

## File documentation

```text
@file
Provides testing functionality.
```

## Functions (derived index)

- [simpletest_help()](simpletest_help.md) — Implements hook_help().
- [simpletest_menu()](simpletest_menu.md) — Implements hook_menu().
- [simpletest_permission()](simpletest_permission.md) — Implements hook_permission().
- [simpletest_theme()](simpletest_theme.md) — Implements hook_theme().
- [simpletest_js_alter()](simpletest_js_alter.md) — Implements hook_js_alter().
- [_simpletest_format_summary_line()](_simpletest_format_summary_line.md)
- [simpletest_run_tests()](simpletest_run_tests.md) — Actually runs tests.
- [_simpletest_batch_operation()](_simpletest_batch_operation.md) — Implements callback_batch_operation().
- [_simpletest_batch_finished()](_simpletest_batch_finished.md) — Implements callback_batch_finished().
- [simpletest_last_test_get()](simpletest_last_test_get.md) — Get information about the last test that ran given a test ID.
- [simpletest_log_read()](simpletest_log_read.md) — Read the error log and report any errors as assertion failures.
- [simpletest_test_get_all()](simpletest_test_get_all.md) — Get a list of all of the tests provided by the system.
- [simpletest_classloader_register()](simpletest_classloader_register.md)
- [_simpletest_autoload_psr4_psr0()](_simpletest_autoload_psr4_psr0.md) — Autoload callback to find PSR-4 and PSR-0 test classes.
- [simpletest_registry_files_alter()](simpletest_registry_files_alter.md) — Implements hook_registry_files_alter().
- [simpletest_generate_file()](simpletest_generate_file.md) — Generate test file.
- [simpletest_clean_environment()](simpletest_clean_environment.md) — Remove all temporary database tables and directories.
- [simpletest_clean_database()](simpletest_clean_database.md) — Removed prefixed tables from the database that are left over from crashed tests.
- [simpletest_clean_temporary_directories()](simpletest_clean_temporary_directories.md) — Find all leftover temporary directories and remove them.
- [simpletest_clean_results_table()](simpletest_clean_results_table.md) — Clear the test result tables.
- [simpletest_mail_alter()](simpletest_mail_alter.md) — Implements hook_mail_alter().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
