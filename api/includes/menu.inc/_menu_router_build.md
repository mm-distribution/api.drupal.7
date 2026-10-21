# _menu_router_build()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3624–3846 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3624-L3846)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_router_build($callbacks)
```

## Documentation

```text
Builds the router table based on the data from hook_menu().
```

## Code

```php
function _menu_router_build($callbacks) {
  // First pass: separate callbacks from paths, making paths ready for
  // matching. Calculate fitness, and fill some default values.
  $menu = array();
  $masks = array();
  foreach ($callbacks as $path => $item) {
    $load_functions = array();
    $to_arg_functions = array();
    $fit = 0;
    $move = FALSE;

    $parts = explode('/', $path, MENU_MAX_PARTS);
    $number_parts = count($parts);
    // We store the highest index of parts here to save some work in the fit
    // calculation loop.
    $slashes = $number_parts - 1;
    // Extract load and to_arg functions.
    foreach ($parts as $k => $part) {
      $match = FALSE;
      // Look for wildcards in the form allowed to be used in PHP functions,
      // because we are using these to construct the load function names.
      if (preg_match('/^%(|' . DRUPAL_PHP_FUNCTION_PATTERN . ')$/', $part, $matches)) {
        if (empty($matches[1])) {
          $match = TRUE;
          $load_functions[$k] = NULL;
        }
        else {
          if (function_exists($matches[1] . '_to_arg')) {
            $to_arg_functions[$k] = $matches[1] . '_to_arg';
            $load_functions[$k] = NULL;
            $match = TRUE;
          }
          if (function_exists($matches[1] . '_load')) {
            $function = $matches[1] . '_load';
            // Create an array of arguments that will be passed to the _load
            // function when this menu path is checked, if 'load arguments'
            // exists.
            $load_functions[$k] = isset($item['load arguments']) ? array($function => $item['load arguments']) : $function;
            $match = TRUE;
          }
        }
      }
      if ($match) {
        $parts[$k] = '%';
      }
      else {
        $fit |=  1 << ($slashes - $k);
      }
    }
    if ($fit) {
      $move = TRUE;
    }
    else {
      // If there is no %, it fits maximally.
      $fit = (1 << $number_parts) - 1;
    }
    $masks[$fit] = 1;
    $item['_load_functions'] = $load_functions;
    $item['to_arg_functions'] = empty($to_arg_functions) ? '' : serialize($to_arg_functions);
    $item += array(
      'title' => '',
      'weight' => 0,
      'type' => MENU_NORMAL_ITEM,
      'module' => '',
      '_number_parts' => $number_parts,
      '_parts' => $parts,
      '_fit' => $fit,
    );
    $item += array(
      '_visible' => (bool) ($item['type'] & MENU_VISIBLE_IN_BREADCRUMB),
      '_tab' => (bool) ($item['type'] & MENU_IS_LOCAL_TASK),
    );
    if ($move) {
      $new_path = implode('/', $item['_parts']);
      $menu[$new_path] = $item;
      $sort[$new_path] = $number_parts;
    }
    else {
      $menu[$path] = $item;
      $sort[$path] = $number_parts;
    }
  }
  array_multisort($sort, SORT_NUMERIC, $menu);
  // Apply inheritance rules.
  foreach ($menu as $path => $v) {
    $item = &$menu[$path];
    if (!$item['_tab']) {
      // Non-tab items.
      $item['tab_parent'] = '';
      $item['tab_root'] = $path;
    }
    // If not specified, assign the default tab type for local tasks.
    elseif (!isset($item['context'])) {
      $item['context'] = MENU_CONTEXT_PAGE;
    }
    for ($i = $item['_number_parts'] - 1; $i; $i--) {
      $parent_path = implode('/', array_slice($item['_parts'], 0, $i));
      if (isset($menu[$parent_path])) {

        $parent = &$menu[$parent_path];

        // If we have no menu name, try to inherit it from parent items.
        if (!isset($item['menu_name'])) {
          // If the parent item of this item does not define a menu name (and no
          // previous iteration assigned one already), try to find the menu name
          // of the parent item in the currently stored menu links.
          if (!isset($parent['menu_name'])) {
            $menu_name = db_query("SELECT menu_name FROM {menu_links} WHERE router_path = :router_path AND module = 'system'", array(':router_path' => $parent_path))->fetchField();
            if ($menu_name) {
              $parent['menu_name'] = $menu_name;
            }
          }
          // If the parent item defines a menu name, inherit it.
          if (!empty($parent['menu_name'])) {
            $item['menu_name'] = $parent['menu_name'];
          }
        }
        if (!isset($item['tab_parent'])) {
          // Parent stores the parent of the path.
          $item['tab_parent'] = $parent_path;
        }
        if (!isset($item['tab_root']) && !$parent['_tab']) {
          $item['tab_root'] = $parent_path;
        }
        // If an access callback is not found for a default local task we use
        // the callback from the parent, since we expect them to be identical.
        // In all other cases, the access parameters must be specified.
        if (($item['type'] == MENU_DEFAULT_LOCAL_TASK) && !isset($item['access callback']) && isset($parent['access callback'])) {
          $item['access callback'] = $parent['access callback'];
          if (!isset($item['access arguments']) && isset($parent['access arguments'])) {
            $item['access arguments'] = $parent['access arguments'];
          }
        }
        // Same for page callbacks.
        if (!isset($item['page callback']) && isset($parent['page callback'])) {
          $item['page callback'] = $parent['page callback'];
          if (!isset($item['page arguments']) && isset($parent['page arguments'])) {
            $item['page arguments'] = $parent['page arguments'];
          }
          if (!isset($item['file path']) && isset($parent['file path'])) {
            $item['file path'] = $parent['file path'];
          }
          if (!isset($item['file']) && isset($parent['file'])) {
            $item['file'] = $parent['file'];
            if (empty($item['file path']) && isset($item['module']) && isset($parent['module']) && $item['module'] != $parent['module']) {
              $item['file path'] = drupal_get_path('module', $parent['module']);
            }
          }
        }
        // Same for delivery callbacks.
        if (!isset($item['delivery callback']) && isset($parent['delivery callback'])) {
          $item['delivery callback'] = $parent['delivery callback'];
        }
        // Same for theme callbacks.
        if (!isset($item['theme callback']) && isset($parent['theme callback'])) {
          $item['theme callback'] = $parent['theme callback'];
          if (!isset($item['theme arguments']) && isset($parent['theme arguments'])) {
            $item['theme arguments'] = $parent['theme arguments'];
          }
        }
        // Same for load arguments: if a loader doesn't have any explict
        // arguments, try to find arguments in the parent.
        if (!isset($item['load arguments'])) {
          foreach ($item['_load_functions'] as $k => $function) {
            // This loader doesn't have any explict arguments...
            if (!is_array($function)) {
              // ... check the parent for a loader at the same position
              // using the same function name and defining arguments...
              if (isset($parent['_load_functions'][$k]) && is_array($parent['_load_functions'][$k]) && key($parent['_load_functions'][$k]) === $function) {
                // ... and inherit the arguments on the child.
                $item['_load_functions'][$k] = $parent['_load_functions'][$k];
              }
            }
          }
        }
      }
    }
    if (!isset($item['access callback']) && isset($item['access arguments'])) {
      // Default callback.
      $item['access callback'] = 'user_access';
    }
    if (!isset($item['access callback']) || empty($item['page callback'])) {
      $item['access callback'] = 0;
    }
    if (is_bool($item['access callback'])) {
      $item['access callback'] = intval($item['access callback']);
    }

    $item['load_functions'] = empty($item['_load_functions']) ? '' : serialize($item['_load_functions']);
    $item += array(
      'access arguments' => array(),
      'access callback' => '',
      'page arguments' => array(),
      'page callback' => '',
      'delivery callback' => '',
      'title arguments' => array(),
      'title callback' => 't',
      'theme arguments' => array(),
      'theme callback' => '',
      'description' => '',
      'position' => '',
      'context' => 0,
      'tab_parent' => '',
      'tab_root' => $path,
      'path' => $path,
      'file' => '',
      'file path' => '',
      'include file' => '',
    );

    // Calculate out the file to be included for each callback, if any.
    if ($item['file']) {
      $file_path = $item['file path'] ? $item['file path'] : drupal_get_path('module', $item['module']);
      $item['include file'] = $file_path . '/' . $item['file'];
    }
  }

  // Sort the masks so they are in order of descending fit.
  $masks = array_keys($masks);
  rsort($masks);

  return array($menu, $masks);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
