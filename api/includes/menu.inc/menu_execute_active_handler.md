# menu_execute_active_handler()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 510–547 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L510-L547)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_execute_active_handler($path = NULL, $deliver = TRUE)
```

## Documentation

```text
Execute the page callback associated with the current path.

@param $path
  The drupal path whose handler is to be be executed. If set to NULL, then
  the current path is used.
@param $deliver
  (optional) A boolean to indicate whether the content should be sent to the
  browser using the appropriate delivery callback (TRUE) or whether to return
  the result to the caller (FALSE).
```

## Code

```php
function menu_execute_active_handler($path = NULL, $deliver = TRUE) {
  // Check if site is offline.
  $page_callback_result = _menu_site_is_offline() ? MENU_SITE_OFFLINE : MENU_SITE_ONLINE;

  // Allow other modules to change the site status but not the path because that
  // would not change the global variable. hook_url_inbound_alter() can be used
  // to change the path. Code later will not use the $read_only_path variable.
  $read_only_path = !empty($path) ? $path : $_GET['q'];
  drupal_alter('menu_site_status', $page_callback_result, $read_only_path);

  // Only continue if the site status is not set.
  if ($page_callback_result == MENU_SITE_ONLINE) {
    if ($router_item = menu_get_item($path)) {
      if ($router_item['access']) {
        if ($router_item['include_file']) {
          require_once DRUPAL_ROOT . '/' . $router_item['include_file'];
        }
        $page_callback_result = call_user_func_array($router_item['page_callback'], $router_item['page_arguments']);
      }
      else {
        $page_callback_result = MENU_ACCESS_DENIED;
      }
    }
    else {
      $page_callback_result = MENU_NOT_FOUND;
    }
  }

  // Deliver the result of the page callback to the browser, or if requested,
  // return it raw, so calling code can do more processing.
  if ($deliver) {
    $default_delivery_callback = (isset($router_item) && $router_item) ? $router_item['delivery_callback'] : NULL;
    drupal_deliver_page($page_callback_result, $default_delivery_callback);
  }
  else {
    return $page_callback_result;
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
