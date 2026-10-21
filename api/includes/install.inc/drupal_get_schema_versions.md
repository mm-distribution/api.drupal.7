# drupal_get_schema_versions()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 98–130 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L98-L130)

## Signature

```php
function drupal_get_schema_versions($module)
```

## Documentation

```text
Returns an array of available schema versions for a module.

@param $module
  A module name.
@return
  If the module has updates, an array of available updates sorted by version.
  Otherwise, FALSE.
```

## Code

```php
function drupal_get_schema_versions($module) {
  $updates = &drupal_static(__FUNCTION__, NULL);
  if (!isset($updates[$module])) {
    $updates = array();

    foreach (module_list() as $loaded_module) {
      $updates[$loaded_module] = array();
    }

    // Prepare regular expression to match all possible defined hook_update_N().
    $regexp = '/^(?P<module>.+)_update_(?P<version>\d+)$/';
    $functions = get_defined_functions();
    // Narrow this down to functions ending with an integer, since all
    // hook_update_N() functions end this way, and there are other
    // possible functions which match '_update_'. We use preg_grep() here
    // instead of foreaching through all defined functions, since the loop
    // through all PHP functions can take significant page execution time
    // and this function is called on every administrative page via
    // system_requirements().
    foreach (preg_grep('/_\d+$/', $functions['user']) as $function) {
      // If this function is a module update function, add it to the list of
      // module updates.
      if (preg_match($regexp, $function, $matches)) {
        $updates[$matches['module']][] = $matches['version'];
      }
    }
    // Ensure that updates are applied in numerical order.
    foreach ($updates as &$module_updates) {
      sort($module_updates, SORT_NUMERIC);
    }
  }
  return empty($updates[$module]) ? FALSE : $updates[$module];
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
