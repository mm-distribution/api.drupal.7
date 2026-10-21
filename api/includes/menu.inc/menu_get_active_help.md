# menu_get_active_help()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1732–1750 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1732-L1750)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_active_help()
```

## Documentation

```text
Returns the help associated with the active menu item.
```

## Code

```php
function menu_get_active_help() {
  $output = '';
  $router_path = menu_tab_root_path();
  // We will always have a path unless we are on a 403 or 404.
  if (!$router_path) {
    return '';
  }

  $arg = drupal_help_arg(arg(NULL));

  foreach (module_implements('help') as $module) {
    $function = $module . '_help';
    // Lookup help for this path.
    if ($help = $function($router_path, $arg)) {
      $output .= $help . "\n";
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
