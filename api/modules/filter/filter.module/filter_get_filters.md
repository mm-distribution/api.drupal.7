# filter_get_filters()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 599–625 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L599-L625)
- **Module/theme:** filter

## Signature

```php
function filter_get_filters()
```

## Documentation

```text
Returns a list of all filters provided by modules.

@return array
  An array of filter formats.
```

## Code

```php
function filter_get_filters() {
  $filters = &drupal_static(__FUNCTION__, array());

  if (empty($filters)) {
    foreach (module_implements('filter_info') as $module) {
      $info = module_invoke($module, 'filter_info');
      if (isset($info) && is_array($info)) {
        // Assign the name of the module implementing the filters and ensure
        // default values.
        foreach (array_keys($info) as $name) {
          $info[$name]['module'] = $module;
          $info[$name] += array(
            'description' => '',
            'weight' => 0,
          );
        }
        $filters = array_merge($filters, $info);
      }
    }
    // Allow modules to alter filter definitions.
    drupal_alter('filter_info', $filters);

    uasort($filters, '_filter_list_cmp');
  }

  return $filters;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
