# menu_contextual_links()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2183–2246 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2183-L2246)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_contextual_links($module, $parent_path, $args)
```

## Documentation

```text
Retrieves contextual links for a path based on registered local tasks.

This leverages the menu system to retrieve the first layer of registered
local tasks for a given system path. All local tasks of the tab type
MENU_CONTEXT_INLINE are taken into account.

For example, when considering the following registered local tasks:
- node/%node/view (default local task) with no 'context' defined
- node/%node/edit with context: MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE
- node/%node/revisions with context: MENU_CONTEXT_PAGE
- node/%node/report-as-spam with context: MENU_CONTEXT_INLINE

If the path "node/123" is passed to this function, then it will return the
links for 'edit' and 'report-as-spam'.

@param $module
  The name of the implementing module. This is used to prefix the key for
  each contextual link, which is transformed into a CSS class during
  rendering by theme_links(). For example, if $module is 'block' and the
  retrieved local task path argument is 'edit', then the resulting CSS class
  will be 'block-edit'.
@param $parent_path
  The static menu router path of the object to retrieve local tasks for, for
  example 'node' or 'admin/structure/block/manage'.
@param $args
  A list of dynamic path arguments to append to $parent_path to form the
  fully-qualified menu router path; for example, array(123) for a certain
  node or array('system', 'navigation') for a certain block.

@return
  A list of menu router items that are local tasks for the passed-in path.

@see contextual_links_preprocess()
@see hook_menu()
```

## Code

```php
function menu_contextual_links($module, $parent_path, $args) {
  static $path_empty = array();

  $links = array();
  // Performance: In case a previous invocation for the same parent path did not
  // return any links, we immediately return here.
  if (isset($path_empty[$parent_path]) && strpos($parent_path, '%') !== FALSE) {
    return $links;
  }
  // Construct the item-specific parent path.
  $path = $parent_path . '/' . implode('/', $args);

  // Get the router item for the given parent link path.
  $router_item = menu_get_item($path);
  if (!$router_item || !$router_item['access']) {
    $path_empty[$parent_path] = TRUE;
    return $links;
  }
  $data = &drupal_static(__FUNCTION__, array());
  $root_path = $router_item['path'];

  // Performance: For a single, normalized path (such as 'node/%') we only query
  // available tasks once per request.
  if (!isset($data[$root_path])) {
    // Get all contextual links that are direct children of the router item and
    // not of the tab type 'view'.
    $data[$root_path] = db_select('menu_router', 'm')
      ->fields('m')
      ->condition('tab_parent', $router_item['tab_root'])
      ->condition('context', MENU_CONTEXT_NONE, '<>')
      ->condition('context', MENU_CONTEXT_PAGE, '<>')
      ->orderBy('weight')
      ->orderBy('title')
      ->execute()
      ->fetchAllAssoc('path', PDO::FETCH_ASSOC);
  }
  $parent_length = drupal_strlen($root_path) + 1;
  $map = $router_item['original_map'];
  foreach ($data[$root_path] as $item) {
    // Extract the actual "task" string from the path argument.
    $key = drupal_substr($item['path'], $parent_length);

    // Denormalize and translate the contextual link.
    _menu_translate($item, $map, TRUE);
    if (!$item['access']) {
      continue;
    }
    // All contextual links are keyed by the actual "task" path argument,
    // prefixed with the name of the implementing module.
    $links[$module . '-' . $key] = $item;
  }

  // Allow modules to alter contextual links.
  drupal_alter('menu_contextual_links', $links, $router_item, $root_path);

  // Performance: If the current user does not have access to any links for this
  // router path and no other module added further links, we assign FALSE here
  // to skip the entire process the next time the same router path is requested.
  if (empty($links)) {
    $path_empty[$parent_path] = TRUE;
  }

  return $links;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
