# search_menu()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 162–230 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L162-L230)
- **Module/theme:** search
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function search_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function search_menu() {
  $items['search'] = array(
    'title' => 'Search',
    'page callback' => 'search_view',
    'access callback' => 'search_is_active',
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'search.pages.inc',
  );
  $items['admin/config/search/settings'] = array(
    'title' => 'Search settings',
    'description' => 'Configure relevance settings for search and other indexing options.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('search_admin_settings'),
    'access arguments' => array('administer search'),
    'weight' => -10,
    'file' => 'search.admin.inc',
  );
  $items['admin/config/search/settings/reindex'] = array(
    'title' => 'Clear index',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('search_reindex_confirm'),
    'access arguments' => array('administer search'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'search.admin.inc',
  );

  // Add paths for searching. We add each module search path twice: once without
  // and once with %menu_tail appended. The reason for this is that we want to
  // preserve keywords when switching tabs, and also to have search tabs
  // highlighted properly. The only way to do that within the Drupal menu
  // system appears to be having two sets of tabs. See discussion on issue
  // http://drupal.org/node/245103 for details.

  drupal_static_reset('search_get_info');
  $default_info = search_get_default_module_info();
  if ($default_info) {
    foreach (search_get_info() as $module => $search_info) {
      $path = 'search/' . $search_info['path'];
      $items[$path] = array(
        'title' => $search_info['title'],
        'page callback' => 'search_view',
        'page arguments' => array($module, ''),
        'access callback' => '_search_menu_access',
        'access arguments' => array($module),
        'type' => MENU_LOCAL_TASK,
        'file' => 'search.pages.inc',
        'weight' => $module == $default_info['module'] ? -10 : 0,
      );
      $items["$path/%menu_tail"] = array(
        'title' => $search_info['title'],
        'load arguments' => array('%map', '%index'),
        'page callback' => 'search_view',
        'page arguments' => array($module, 2),
        'access callback' => '_search_menu_access',
        'access arguments' => array($module),
        // The default local task points to its parent, but this item points to
        // where it should so it should not be changed.
        'type' => MENU_LOCAL_TASK,
        'file' => 'search.pages.inc',
        'weight' => 0,
        // These tabs are not subtabs.
        'tab_root' => 'search/' . $default_info['path'] . '/%',
        // These tabs need to display at the same level.
        'tab_parent' => 'search/' . $default_info['path'],
      );
    }
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
