# help_links_as_list()

- **Type:** Function
- **File:** [`modules/help/help.admin.inc`](_file.md), lines 58–85 · [local source](../../../../source/modules/help/help.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc#L58-L85)
- **Module/theme:** help

## Signature

```php
function help_links_as_list()
```

## Documentation

```text
Provides a formatted list of available help topics.

@return
  A string containing the formatted list.
```

## Code

```php
function help_links_as_list() {
  $empty_arg = drupal_help_arg();
  $module_info = system_rebuild_module_data();

  $modules = array();
  foreach (module_implements('help', TRUE) as $module) {
    if (module_invoke($module, 'help', "admin/help#$module", $empty_arg)) {
      $modules[$module] = $module_info[$module]->info['name'];
    }
  }
  asort($modules);

  // Output pretty four-column list.
  $count = count($modules);
  $break = ceil($count / 4);
  $output = '<div class="clearfix"><div class="help-items"><ul>';
  $i = 0;
  foreach ($modules as $module => $name) {
    $output .= '<li>' . l($name, 'admin/help/' . $module) . '</li>';
    if (($i + 1) % $break == 0 && ($i + 1) != $count) {
      $output .= '</ul></div><div class="help-items' . ($i + 1 == $break * 3 ? ' help-items-last' : '') . '"><ul>';
    }
    $i++;
  }
  $output .= '</ul></div></div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/help/help.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
