# simpletest_script_print_error()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 798–800 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L798-L800)

## Signature

```php
function simpletest_script_print_error($message)
```

## Documentation

```text
Print error message prefixed with "  ERROR: " and displayed in fail color
if color output is enabled.

@param $message The message to print.
```

## Code

```php
function simpletest_script_print_error($message) {
  simpletest_script_print("  ERROR: $message\n", SIMPLETEST_SCRIPT_COLOR_FAIL);
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
