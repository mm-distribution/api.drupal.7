# overlay_display_empty_page()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 569–575 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L569-L575)
- **Module/theme:** overlay

## Signature

```php
function overlay_display_empty_page($value = NULL)
```

## Documentation

```text
Stores and returns whether an empty page override is needed.

This is used to prevent a page request which closes the overlay (for
example, a form submission) from being fully re-rendered before the overlay
is closed. Instead, we store a variable which will cause the page to be
rendered by a delivery callback function that does not actually print
visible HTML (but rather only the bare minimum scripts and styles necessary
to trigger the overlay to close), thereby allowing the dialog to be closed
faster and with less interruption, and also allowing the display of messages
to be deferred to the parent window (rather than displaying them in the
child window, which will close before the user has had a chance to read
them).

@param $value
  By default, an empty page will not be displayed. Set to TRUE to request
  an empty page display, or FALSE to disable the empty page display (if it
  was previously enabled on this page request).

@return
  TRUE if the current behavior is to display an empty page, or FALSE if not.

@see overlay_page_delivery_callback_alter()
```

## Code

```php
function overlay_display_empty_page($value = NULL) {
  $display_empty_page = &drupal_static(__FUNCTION__, FALSE);
  if (isset($value)) {
    $display_empty_page = $value;
  }
  return $display_empty_page;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
