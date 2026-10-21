# menu_local_tasks()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1923–2145 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1923-L2145)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_local_tasks($level = 0)
```

## Documentation

```text
Collects the local tasks (tabs), action links, and the root path.

@param $level
  The level of tasks you ask for. Primary tasks are 0, secondary are 1.

@return
  An array containing
  - tabs: Local tasks for the requested level:
    - count: The number of local tasks.
    - output: The themed output of local tasks.
  - actions: Action links for the requested level:
    - count: The number of action links.
    - output: The themed output of action links.
  - root_path: The router path for the current page. If the current page is
    a default local task, then this corresponds to the parent tab.
```

## Code

```php
function menu_local_tasks($level = 0) {
  $data = &drupal_static(__FUNCTION__);
  $root_path = &drupal_static(__FUNCTION__ . ':root_path', '');
  $empty = array(
    'tabs' => array('count' => 0, 'output' => array()),
    'actions' => array('count' => 0, 'output' => array()),
    'root_path' => &$root_path,
  );

  if (!isset($data)) {
    $data = array();
    // Set defaults in case there are no actions or tabs.
    $actions = $empty['actions'];
    $tabs = array();

    $router_item = menu_get_item();

    // If this router item points to its parent, start from the parents to
    // compute tabs and actions.
    if ($router_item && ($router_item['type'] & MENU_LINKS_TO_PARENT)) {
      $router_item = menu_get_item($router_item['tab_parent_href']);
    }

    // If we failed to fetch a router item or the current user doesn't have
    // access to it, don't bother computing the tabs.
    if (!$router_item || !$router_item['access']) {
      return $empty;
    }

    // Get all tabs (also known as local tasks) and the root page.
    $cid = 'local_tasks:' . $router_item['tab_root'];
    if ($cache = cache_get($cid, 'cache_menu')) {
      $result = $cache->data;
    }
    else {
      $result = db_select('menu_router', NULL, array('fetch' => PDO::FETCH_ASSOC))
        ->fields('menu_router')
        ->condition('tab_root', $router_item['tab_root'])
        ->condition('context', MENU_CONTEXT_INLINE, '<>')
        ->orderBy('weight')
        ->orderBy('title')
        ->execute()
        ->fetchAll();
      cache_set($cid, $result, 'cache_menu');
    }
    $map = $router_item['original_map'];
    $children = array();
    $tasks = array();
    $root_path = $router_item['path'];

    foreach ($result as $item) {
      _menu_translate($item, $map, TRUE);
      if ($item['tab_parent']) {
        // All tabs, but not the root page.
        $children[$item['tab_parent']][$item['path']] = $item;
      }
      // Store the translated item for later use.
      $tasks[$item['path']] = $item;
    }

    // Find all tabs below the current path.
    $path = $router_item['path'];
    // Tab parenting may skip levels, so the number of parts in the path may not
    // equal the depth. Thus we use the $depth counter (offset by 1000 for ksort).
    $depth = 1001;
    $actions['count'] = 0;
    $actions['output'] = array();
    while (isset($children[$path])) {
      $tabs_current = array();
      $actions_current = array();
      $next_path = '';
      $tab_count = 0;
      $action_count = 0;
      foreach ($children[$path] as $item) {
        // Local tasks can be normal items too, so bitmask with
        // MENU_IS_LOCAL_TASK before checking.
        if (!($item['type'] & MENU_IS_LOCAL_TASK)) {
          // This item is not a tab, skip it.
          continue;
        }
        if ($item['access']) {
          $link = $item;
          // The default task is always active. As tabs can be normal items
          // too, so bitmask with MENU_LINKS_TO_PARENT before checking.
          if (($item['type'] & MENU_LINKS_TO_PARENT) == MENU_LINKS_TO_PARENT) {
            // Find the first parent which is not a default local task or action.
            for ($p = $item['tab_parent']; ($tasks[$p]['type'] & MENU_LINKS_TO_PARENT) == MENU_LINKS_TO_PARENT; $p = $tasks[$p]['tab_parent']);
            // Use the path of the parent instead.
            $link['href'] = $tasks[$p]['href'];
            // Mark the link as active, if the current path happens to be the
            // path of the default local task itself (i.e., instead of its
            // tab_parent_href or tab_root_href). Normally, links for default
            // local tasks link to their parent, but the path of default local
            // tasks can still be accessed directly, in which case this link
            // would not be marked as active, since l() only compares the href
            // with $_GET['q'].
            if ($link['href'] != $_GET['q']) {
              $link['localized_options']['attributes']['class'][] = 'active';
            }
            $tabs_current[] = array(
              '#theme' => 'menu_local_task',
              '#link' => $link,
              '#active' => TRUE,
            );
            $next_path = $item['path'];
            $tab_count++;
          }
          else {
            // Actions can be normal items too, so bitmask with
            // MENU_IS_LOCAL_ACTION before checking.
            if (($item['type'] & MENU_IS_LOCAL_ACTION) == MENU_IS_LOCAL_ACTION) {
              // The item is an action, display it as such.
              $actions_current[] = array(
                '#theme' => 'menu_local_action',
                '#link' => $link,
              );
              $action_count++;
            }
            else {
              // Otherwise, it's a normal tab.
              $tabs_current[] = array(
                '#theme' => 'menu_local_task',
                '#link' => $link,
              );
              $tab_count++;
            }
          }
        }
      }
      $path = $next_path;
      $tabs[$depth]['count'] = $tab_count;
      $tabs[$depth]['output'] = $tabs_current;
      $actions['count'] += $action_count;
      $actions['output'] = array_merge($actions['output'], $actions_current);
      $depth++;
    }
    $data['actions'] = $actions;
    // Find all tabs at the same level or above the current one.
    $parent = $router_item['tab_parent'];
    $path = $router_item['path'];
    $current = $router_item;
    $depth = 1000;
    while (isset($children[$parent])) {
      $tabs_current = array();
      $next_path = '';
      $next_parent = '';
      $count = 0;
      foreach ($children[$parent] as $item) {
        // Skip local actions.
        if ($item['type'] & MENU_IS_LOCAL_ACTION) {
          continue;
        }
        if ($item['access']) {
          $count++;
          $link = $item;
          // Local tasks can be normal items too, so bitmask with
          // MENU_LINKS_TO_PARENT before checking.
          if (($item['type'] & MENU_LINKS_TO_PARENT) == MENU_LINKS_TO_PARENT) {
            // Find the first parent which is not a default local task.
            for ($p = $item['tab_parent']; ($tasks[$p]['type'] & MENU_LINKS_TO_PARENT) == MENU_LINKS_TO_PARENT; $p = $tasks[$p]['tab_parent']);
            // Use the path of the parent instead.
            $link['href'] = $tasks[$p]['href'];
            if ($item['path'] == $router_item['path']) {
              $root_path = $tasks[$p]['path'];
            }
          }
          // We check for the active tab.
          if ($item['path'] == $path) {
            // Mark the link as active, if the current path is a (second-level)
            // local task of a default local task. Since this default local task
            // links to its parent, l() will not mark it as active, as it only
            // compares the link's href to $_GET['q'].
            if ($link['href'] != $_GET['q']) {
              $link['localized_options']['attributes']['class'][] = 'active';
            }
            $tabs_current[] = array(
              '#theme' => 'menu_local_task',
              '#link' => $link,
              '#active' => TRUE,
            );
            $next_path = $item['tab_parent'];
            if (isset($tasks[$next_path])) {
              $next_parent = $tasks[$next_path]['tab_parent'];
            }
          }
          else {
            $tabs_current[] = array(
              '#theme' => 'menu_local_task',
              '#link' => $link,
            );
          }
        }
      }
      $path = $next_path;
      $parent = $next_parent;
      $tabs[$depth]['count'] = $count;
      $tabs[$depth]['output'] = $tabs_current;
      $depth--;
    }
    // Sort by depth.
    ksort($tabs);
    // Remove the depth, we are interested only in their relative placement.
    $tabs = array_values($tabs);
    $data['tabs'] = $tabs;

    // Allow modules to alter local tasks or dynamically append further tasks.
    drupal_alter('menu_local_tasks', $data, $router_item, $root_path);
  }

  if (isset($data['tabs'][$level])) {
    return array(
      'tabs' => $data['tabs'][$level],
      'actions' => $data['actions'],
      'root_path' => $root_path,
    );
  }
  // @todo If there are no tabs, then there still can be actions; for example,
  //   when added via hook_menu_local_tasks_alter().
  elseif (!empty($data['actions']['output'])) {
    return array('actions' => $data['actions']) + $empty;
  }
  return $empty;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
