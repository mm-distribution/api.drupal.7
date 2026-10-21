# overlay_init()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 136–182 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L136-L182)
- **Module/theme:** overlay
- **Implements:** [hook_init()](../../system/system.api.php/hook_init.md)

## Signature

```php
function overlay_init()
```

## Documentation

```text
Implements hook_init().

Determine whether the current page request is destined to appear in the
parent window or in the overlay window, and format the page accordingly.

@see overlay_set_mode()
```

## Code

```php
function overlay_init() {
  global $user;

  $mode = overlay_get_mode();

  // Only act if the user has access to the overlay and a mode was not already
  // set. Other modules can also enable the overlay directly for other uses.
  $use_overlay = !isset($user->data['overlay']) || $user->data['overlay'];
  if (empty($mode) && user_access('access overlay') && $use_overlay) {
    $current_path = current_path();
    // After overlay is enabled on the modules page, redirect to
    // <front>#overlay=admin/modules to actually enable the overlay.
    if (isset($_SESSION['overlay_enable_redirect']) && $_SESSION['overlay_enable_redirect']) {
      unset($_SESSION['overlay_enable_redirect']);
      drupal_goto('<front>', array('fragment' => 'overlay=' . $current_path));
    }

    if (isset($_GET['render']) && $_GET['render'] == 'overlay') {
      // If a previous page requested that we close the overlay, close it and
      // redirect to the final destination.
      if (isset($_SESSION['overlay_close_dialog'])) {
        call_user_func_array('overlay_close_dialog', $_SESSION['overlay_close_dialog']);
        unset($_SESSION['overlay_close_dialog']);
      }
      // If this page shouldn't be rendered inside the overlay, redirect to the
      // parent.
      elseif (!path_is_admin($current_path)) {
        // Prevent open redirects by ensuring the current path is not an absolute URL.
        if (url_is_external($current_path)) {
          $current_path = '<front>';
        }
        overlay_close_dialog($current_path, array('query' => drupal_get_query_parameters(NULL, array('q', 'render'))));
      }

      // Indicate that we are viewing an overlay child page.
      overlay_set_mode('child');

      // Unset the render parameter to avoid it being included in URLs on the page.
      unset($_GET['render']);
    }
    // Do not enable the overlay if we already are on an admin page.
    elseif (!path_is_admin($current_path)) {
      // Otherwise add overlay parent code and our behavior.
      overlay_set_mode('parent');
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
