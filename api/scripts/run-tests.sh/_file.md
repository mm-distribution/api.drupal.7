# scripts/run-tests.sh

- **Source:** [local](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · 870 lines

## File documentation

```text
@file
This script runs Drupal tests from command line.
```

## Functions (derived index)

- [simpletest_script_help()](simpletest_script_help.md) — Print help text.
- [simpletest_script_parse_args()](simpletest_script_parse_args.md) — Parse execution argument and ensure that all are valid.
- [simpletest_script_init()](simpletest_script_init.md) — Initialize script variables and perform general setup requirements.
- [simpletest_script_execute_batch()](simpletest_script_execute_batch.md) — Execute a batch of tests.
- [simpletest_script_run_one_test()](simpletest_script_run_one_test.md) — Bootstrap Drupal and run a single test.
- [simpletest_script_command()](simpletest_script_command.md) — Return a command used to run a test in a separate process.
- [simpletest_script_get_test_list()](simpletest_script_get_test_list.md) — Get list of tests based on arguments. If --all specified then returns all available tests, otherwise reads list of tests.
- [simpletest_script_reporter_init()](simpletest_script_reporter_init.md) — Initialize the reporter.
- [simpletest_script_reporter_write_xml_results()](simpletest_script_reporter_write_xml_results.md) — Display jUnit XML test results.
- [simpletest_script_reporter_timer_stop()](simpletest_script_reporter_timer_stop.md) — Stop the test timer.
- [simpletest_script_reporter_display_results()](simpletest_script_reporter_display_results.md) — Display test results.
- [simpletest_script_format_result()](simpletest_script_format_result.md) — Format the result so that it fits within the default 80 character terminal size.
- [simpletest_script_print_error()](simpletest_script_print_error.md) — Print error message prefixed with "  ERROR: " and displayed in fail color if color output is enabled.
- [simpletest_script_print()](simpletest_script_print.md) — Print a message to the console, if color is enabled then the specified color code will be used.
- [simpletest_script_color_code()](simpletest_script_color_code.md) — Get the color code associated with the specified status.
- [simpletest_script_print_alternatives()](simpletest_script_print_alternatives.md) — Prints alternative test names.

## Constants

### SIMPLETEST_SCRIPT_COLOR_PASS

- Line 7

```php
define('SIMPLETEST_SCRIPT_COLOR_PASS', 32); // Green.
```

### SIMPLETEST_SCRIPT_COLOR_FAIL

- Line 8

```php
define('SIMPLETEST_SCRIPT_COLOR_FAIL', 31); // Red.
```

### SIMPLETEST_SCRIPT_COLOR_EXCEPTION

- Line 9

```php
define('SIMPLETEST_SCRIPT_COLOR_EXCEPTION', 33); // Brown.
```

### SIMPLETEST_SCRIPT_EXIT_SUCCESS

- Line 11

```php
define('SIMPLETEST_SCRIPT_EXIT_SUCCESS', 0);
```

### SIMPLETEST_SCRIPT_EXIT_FAILURE

- Line 12

```php
define('SIMPLETEST_SCRIPT_EXIT_FAILURE', 1);
```

### SIMPLETEST_SCRIPT_EXIT_EXCEPTION

- Line 13

```php
define('SIMPLETEST_SCRIPT_EXIT_EXCEPTION', 2);
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
