# update_is_missing()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1403–1405 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1403-L1405)

## Signature

```php
function update_is_missing($module, $number, $update_functions)
```

## Documentation

```text
Determines if a module update is missing or unavailable.

@param $module
  The name of the module.
@param $number
  The number of the update within that module.
@param $update_functions
  An organized array of update functions, in the format returned by
  update_get_update_function_list(). This should represent all module
  updates that are requested to run at the time this function is called.

@return
  TRUE if the provided module update is not installed or is not in the
  provided list of updates to run; FALSE otherwise.
```

## Code

```php
function update_is_missing($module, $number, $update_functions) {
  return !isset($update_functions[$module][$number]) || !function_exists($update_functions[$module][$number]);
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
