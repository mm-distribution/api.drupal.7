# _module_build_dependencies()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 250–268 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L250-L268)

## Signature

```php
function _module_build_dependencies($files)
```

## Documentation

```text
Determines which modules require and are required by each module.

@param $files
  The array of filesystem objects used to rebuild the cache.

@return
  The same array with the new keys for each module:
  - requires: An array with the keys being the modules that this module
    requires.
  - required_by: An array with the keys being the modules that will not work
    without this module.
```

## Code

```php
function _module_build_dependencies($files) {
  require_once DRUPAL_ROOT . '/includes/graph.inc';
  foreach ($files as $filename => $file) {
    $graph[$file->name]['edges'] = array();
    if (isset($file->info['dependencies']) && is_array($file->info['dependencies'])) {
      foreach ($file->info['dependencies'] as $dependency) {
        $dependency_data = drupal_parse_dependency($dependency);
        $graph[$file->name]['edges'][$dependency_data['name']] = $dependency_data;
      }
    }
  }
  drupal_depth_first_search($graph);
  foreach ($graph as $module => $data) {
    $files[$module]->required_by = isset($data['reverse_paths']) ? $data['reverse_paths'] : array();
    $files[$module]->requires = isset($data['paths']) ? $data['paths'] : array();
    $files[$module]->sort = $data['weight'];
  }
  return $files;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
