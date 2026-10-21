# drupal_deliver_page()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2699–2716 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2699-L2716)

## Signature

```php
function drupal_deliver_page($page_callback_result, $default_delivery_callback = NULL)
```

## Documentation

```text
Delivers a page callback result to the browser in the appropriate format.

This function is most commonly called by menu_execute_active_handler(), but
can also be called by error conditions such as drupal_not_found(),
drupal_access_denied(), and drupal_site_offline().

When a user requests a page, index.php calls menu_execute_active_handler(),
which calls the 'page callback' function registered in hook_menu(). The page
callback function can return one of:
- NULL: to indicate no content.
- An integer menu status constant: to indicate an error condition.
- A string of HTML content.
- A renderable array of content.
Returning a renderable array rather than a string of HTML is preferred,
because that provides modules with more flexibility in customizing the final
result.

When the page callback returns its constructed content to
menu_execute_active_handler(), this function gets called. The purpose of
this function is to determine the most appropriate 'delivery callback'
function to route the content to. The delivery callback function then
sends the content to the browser in the needed format. The default delivery
callback is drupal_deliver_html_page(), which delivers the content as an HTML
page, complete with blocks in addition to the content. This default can be
overridden on a per menu router item basis by setting 'delivery callback' in
hook_menu() or hook_menu_alter(), and can also be overridden on a per request
basis in hook_page_delivery_callback_alter().

For example, the same page callback function can be used for an HTML
version of the page and an Ajax version of the page. The page callback
function just needs to decide what content is to be returned and the
delivery callback function will send it as an HTML page or an Ajax
response, as appropriate.

In order for page callbacks to be reusable in different delivery formats,
they should not issue any "print" or "echo" statements, but instead just
return content.

Also note that this function does not perform access checks. The delivery
callback function specified in hook_menu(), hook_menu_alter(), or
hook_page_delivery_callback_alter() will be called even if the router item
access checks fail. This is intentional (it is needed for JSON and other
purposes), but it has security implications. Do not call this function
directly unless you understand the security implications, and be careful in
writing delivery callbacks, so that they do not violate security. See
drupal_deliver_html_page() for an example of a delivery callback that
respects security.

@param $page_callback_result
  The result of a page callback. Can be one of:
  - NULL: to indicate no content.
  - An integer menu status constant: to indicate an error condition.
  - A string of HTML content.
  - A renderable array of content.
@param $default_delivery_callback
  (Optional) If given, it is the name of a delivery function most likely
  to be appropriate for the page request as determined by the calling
  function (e.g., menu_execute_active_handler()). If not given, it is
  determined from the menu router information of the current page.

@see menu_execute_active_handler()
@see hook_menu()
@see hook_menu_alter()
@see hook_page_delivery_callback_alter()
```

## Code

```php
function drupal_deliver_page($page_callback_result, $default_delivery_callback = NULL) {
  if (!isset($default_delivery_callback) && ($router_item = menu_get_item())) {
    $default_delivery_callback = $router_item['delivery_callback'];
  }
  $delivery_callback = !empty($default_delivery_callback) ? $default_delivery_callback : 'drupal_deliver_html_page';
  // Give modules a chance to alter the delivery callback used, based on
  // request-time context (e.g., HTTP request headers).
  drupal_alter('page_delivery_callback', $delivery_callback);
  if (function_exists($delivery_callback)) {
    $delivery_callback($page_callback_result);
  }
  else {
    // If a delivery callback is specified, but doesn't exist as a function,
    // something is wrong, but don't print anything, since it's not known
    // what format the response needs to be in.
    watchdog('delivery callback not found', 'callback %callback not found: %q.', array('%callback' => $delivery_callback, '%q' => $_GET['q']), WATCHDOG_ERROR);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
