# field_ui_table_pre_render()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 128–195 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L128-L195)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_table_pre_render($elements)
```

## Documentation

```text
Pre-render callback for field_ui_table elements.
```

## Code

```php
function field_ui_table_pre_render($elements) {
  $js_settings = array();

  // For each region, build the tree structure from the weight and parenting
  // data contained in the flat form structure, to determine row order and
  // indentation.
  $regions = $elements['#regions'];
  $tree = array('' => array('name' => '', 'children' => array()));
  $trees = array_fill_keys(array_keys($regions), $tree);

  $parents = array();
  $list = drupal_map_assoc(element_children($elements));

  // Iterate on rows until we can build a known tree path for all of them.
  while ($list) {
    foreach ($list as $name) {
      $row = &$elements[$name];
      $parent = $row['parent_wrapper']['parent']['#value'];
      // Proceed if parent is known.
      if (empty($parent) || isset($parents[$parent])) {
        // Grab parent, and remove the row from the next iteration.
        $parents[$name] = $parent ? array_merge($parents[$parent], array($parent)) : array();
        unset($list[$name]);

        // Determine the region for the row.
        $function = $row['#region_callback'];
        $region_name = $function($row);

        // Add the element in the tree.
        $target = &$trees[$region_name][''];
        foreach ($parents[$name] as $key) {
          $target = &$target['children'][$key];
        }
        $target['children'][$name] = array('name' => $name, 'weight' => $row['weight']['#value']);

        // Add tabledrag indentation to the first row cell.
        if ($depth = count($parents[$name])) {
          $children = element_children($row);
          $cell = current($children);
          $row[$cell]['#prefix'] = theme('indentation', array('size' => $depth)) . (isset($row[$cell]['#prefix']) ? $row[$cell]['#prefix'] : '');
        }

        // Add row id and associate JS settings.
        $id = drupal_html_class($name);
        $row['#attributes']['id'] = $id;
        if (isset($row['#js_settings'])) {
          $row['#js_settings'] += array(
            'rowHandler' => $row['#row_type'],
            'name' => $name,
            'region' => $region_name,
          );
          $js_settings[$id] = $row['#js_settings'];
        }
      }
    }
  }
  // Determine rendering order from the tree structure.
  foreach ($regions as $region_name => $region) {
    $elements['#regions'][$region_name]['rows_order'] = array_reduce($trees[$region_name], '_field_ui_reduce_order');
  }

  $elements['#attached']['js'][] = array(
    'type' => 'setting',
    'data' => array('fieldUIRowsData' => $js_settings),
  );

  return $elements;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
