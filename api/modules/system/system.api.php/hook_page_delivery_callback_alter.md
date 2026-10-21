# hook_page_delivery_callback_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4283–4290 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4283-L4290)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_page_delivery_callback_alter(&$callback)
```

## Documentation

```text
Alters the delivery callback used to send the result of the page callback to the browser.

Called by drupal_deliver_page() to allow modules to alter how the
page is delivered to the browser.

This hook is intended for altering the delivery callback based on
information unrelated to the path of the page accessed. For example,
it can be used to set the delivery callback based on a HTTP request
header (as shown in the code sample). To specify a delivery callback
based on path information, use hook_menu() or hook_menu_alter().

This hook can also be used as an API function that can be used to explicitly
set the delivery callback from some other function. For example, for a module
named MODULE:
@code
function MODULE_page_delivery_callback_alter(&$callback, $set = FALSE) {
  static $stored_callback;
  if ($set) {
    $stored_callback = $callback;
  }
  elseif (isset($stored_callback)) {
    $callback = $stored_callback;
  }
}
function SOMEWHERE_ELSE() {
  $desired_delivery_callback = 'foo';
  MODULE_page_delivery_callback_alter($desired_delivery_callback, TRUE);
}
@endcode

@param $callback
  The name of a function.

@see drupal_deliver_page()
```

## Code

```php
function hook_page_delivery_callback_alter(&$callback) {
  // jQuery sets a HTTP_X_REQUESTED_WITH header of 'XMLHttpRequest'.
  // If a page would normally be delivered as an html page, and it is called
  // from jQuery, deliver it instead as an Ajax response.
  if (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest' && $callback == 'drupal_deliver_html_page') {
    $callback = 'ajax_deliver';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_page_delivery_callback_alter()".

- [overlay_page_delivery_callback_alter()](../../overlay/overlay.module/overlay_page_delivery_callback_alter.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
