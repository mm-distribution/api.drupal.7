# error_displayable()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 149–157 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L149-L157)

## Signature

```php
function error_displayable($error = NULL)
```

## Documentation

```text
Determines whether an error should be displayed.

When in maintenance mode or when error_level is ERROR_REPORTING_DISPLAY_ALL,
all errors should be displayed. For ERROR_REPORTING_DISPLAY_SOME, $error
will be examined to determine if it should be displayed.

@param $error
  Optional error to examine for ERROR_REPORTING_DISPLAY_SOME.

@return
  TRUE if an error should be displayed.
```

## Code

```php
function error_displayable($error = NULL) {
  $error_level = variable_get('error_level', ERROR_REPORTING_DISPLAY_ALL);
  $updating = (defined('MAINTENANCE_MODE') && MAINTENANCE_MODE == 'update');
  $all_errors_displayed = ($error_level == ERROR_REPORTING_DISPLAY_ALL);
  $error_needs_display = ($error_level == ERROR_REPORTING_DISPLAY_SOME &&
    isset($error) && $error['%type'] != 'Notice' && $error['%type'] != 'Strict warning');

  return ($updating || $all_errors_displayed || $error_needs_display);
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
