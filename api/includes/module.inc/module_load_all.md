# module_load_all()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 19–30 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L19-L30)

## Signature

```php
function module_load_all($bootstrap = FALSE)
```

## Documentation

```text
Loads all the modules that have been enabled in the system table.

@param $bootstrap
  Whether to load only the reduced set of modules loaded in "bootstrap mode"
  for cached pages. See bootstrap.inc.

@return
  If $bootstrap is NULL, return a boolean indicating whether all modules
  have been loaded.
```

## Code

```php
function module_load_all($bootstrap = FALSE) {
  static $has_run = FALSE;

  if (isset($bootstrap)) {
    foreach (module_list(TRUE, $bootstrap) as $module) {
      drupal_load('module', $module);
    }
    // $has_run will be TRUE if $bootstrap is FALSE.
    $has_run = !$bootstrap;
  }
  return $has_run;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
