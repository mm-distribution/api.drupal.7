# search_view()

- **Type:** Function
- **File:** [`modules/search/search.pages.inc`](_file.md), lines 16–73 · [local source](../../../../source/modules/search/search.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc#L16-L73)
- **Module/theme:** search

## Signature

```php
function search_view($module = NULL, $keys = '')
```

## Documentation

```text
Menu callback; presents the search form and/or search results.

@param $module
  Search module to use for the search.
@param $keys
  Keywords to use for the search.
```

## Code

```php
function search_view($module = NULL, $keys = '') {
  $info = FALSE;
  $keys = trim($keys);
  // Also try to pull search keywords out of the $_REQUEST variable to
  // support old GET format of searches for existing links.
  if (!$keys && !empty($_REQUEST['keys'])) {
    $keys = trim($_REQUEST['keys']);
  }

  if (!empty($module)) {
    $active_module_info = search_get_info();
    if (isset($active_module_info[$module])) {
      $info = $active_module_info[$module];
    }
  }

  if (empty($info)) {
    // No path or invalid path: find the default module. Note that if there
    // are no enabled search modules, this function should never be called,
    // since hook_menu() would not have defined any search paths.
    $info = search_get_default_module_info();
    // Redirect from bare /search or an invalid path to the default search path.
    $path = 'search/' . $info['path'];
    if ($keys) {
      $path .= '/' . $keys;
    }
    drupal_goto($path);
  }

  // Default results output is an empty string.
  $results = array('#markup' => '');
  // Process the search form. Note that if there is $_POST data,
  // search_form_submit() will cause a redirect to search/[module path]/[keys],
  // which will get us back to this page callback. In other words, the search
  // form submits with POST but redirects to GET. This way we can keep
  // the search query URL clean as a whistle.
  if (empty($_POST['form_id']) || ($_POST['form_id'] != 'search_form' && $_POST['form_id'] != 'search_block_form')) {
    $conditions =  NULL;
    if (isset($info['conditions_callback']) && function_exists($info['conditions_callback'])) {
      // Build an optional array of more search conditions.
      $conditions = call_user_func($info['conditions_callback'], $keys);
    }
    // Only search if there are keywords or non-empty conditions.
    if ($keys || !empty($conditions)) {
       if (variable_get('search_logging', TRUE)) {
         // Log the search keys.
         watchdog('search', 'Searched %type for %keys.', array('%keys' => $keys, '%type' => $info['title']), WATCHDOG_NOTICE, l(t('results'), 'search/' . $info['path'] . '/' . $keys));
       }
      // Collect the search results.
      $results = search_data($keys, $info['module'], $conditions);
    }
  }
  // The form may be altered based on whether the search was run.
  $build['search_form'] = drupal_get_form('search_form', NULL, $keys, $info['module']);
  $build['search_results'] = $results;

  return $build;
}
```

---
_Drupal 7.103 · [modules/search/search.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
