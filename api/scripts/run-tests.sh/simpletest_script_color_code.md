# simpletest_script_color_code()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 825–835 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L825-L835)

## Signature

```php
function simpletest_script_color_code($status)
```

## Documentation

```text
Get the color code associated with the specified status.

@param $status The status string to get code for.
@return Color code.
```

## Code

```php
function simpletest_script_color_code($status) {
  switch ($status) {
    case 'pass':
      return SIMPLETEST_SCRIPT_COLOR_PASS;
    case 'fail':
      return SIMPLETEST_SCRIPT_COLOR_FAIL;
    case 'exception':
      return SIMPLETEST_SCRIPT_COLOR_EXCEPTION;
  }
  return 0; // Default formatting.
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
