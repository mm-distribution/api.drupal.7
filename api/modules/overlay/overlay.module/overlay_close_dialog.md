# overlay_close_dialog()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 736–753 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L736-L753)
- **Module/theme:** overlay

## Signature

```php
function overlay_close_dialog($redirect = NULL, $redirect_options = array())
```

## Documentation

```text
Requests that the overlay closes when the page is displayed.

@param $redirect
  (optional) The path that should open in the parent window after the
  overlay closes. If not set, no redirect will be performed on the parent
  window.

@param $redirect_options
  (optional) An associative array of options to use when generating the
  redirect URL.
```

## Code

```php
function overlay_close_dialog($redirect = NULL, $redirect_options = array()) {
  $settings = array(
    'overlayChild' => array(
      'closeOverlay' => TRUE,
    ),
  );

  // Tell the child window to perform the redirection when requested to.
  if (isset($redirect)) {
    $settings['overlayChild']['redirect'] = url($redirect, $redirect_options);
  }

  drupal_add_js($settings, array('type' => 'setting'));

  // Since we are closing the overlay as soon as the page is displayed, we do
  // not want to show any of the page's actual content.
  overlay_display_empty_page(TRUE);
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
