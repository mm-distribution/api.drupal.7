# menu_router_build()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2826–2845 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2826-L2845)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_router_build()
```

## Documentation

```text
Collects and alters the menu definitions.
```

## Code

```php
function menu_router_build() {
  // We need to manually call each module so that we can know which module
  // a given item came from.
  $callbacks = array();
  foreach (module_implements('menu') as $module) {
    $router_items = call_user_func($module . '_menu');
    if (isset($router_items) && is_array($router_items)) {
      foreach (array_keys($router_items) as $path) {
        $router_items[$path]['module'] = $module;
      }
      $callbacks = array_merge($callbacks, $router_items);
    }
  }
  // Alter the menu as defined in modules, keys are like user/%user.
  drupal_alter('menu', $callbacks);
  list($menu, $masks) = _menu_router_build($callbacks);
  _menu_router_cache($menu);

  return array($menu, $masks);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
