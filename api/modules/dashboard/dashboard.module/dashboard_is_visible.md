# dashboard_is_visible()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 448–458 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L448-L458)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_is_visible()
```

## Documentation

```text
Determines if the dashboard should be displayed on the current page.

This function checks if the user is currently viewing the dashboard and has
access to see it. It is used by other functions in the dashboard module to
decide whether or not the dashboard content should be displayed to the
current user.

Although the menu system normally handles the above tasks, it only does so
for the main page content. However, the dashboard is not part of the main
page content, but rather is displayed in special regions of the page (so it
can interface with the Block module's method of managing page regions). We
therefore need to maintain this separate function to check the menu item for
us.

@return
  TRUE if the dashboard should be visible on the current page, FALSE
  otherwise.

@see dashboard_block_list_alter()
@see dashboard_page_build()
```

## Code

```php
function dashboard_is_visible() {
  static $is_visible;
  if (!isset($is_visible)) {
    // If the current menu item represents the page on which we want to display
    // the dashboard, and if the current user has access to see it, return
    // TRUE.
    $menu_item = menu_get_item();
    $is_visible = isset($menu_item['page_callback']) && $menu_item['page_callback'] == 'dashboard_admin' && !empty($menu_item['access']);
  }
  return $is_visible;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
