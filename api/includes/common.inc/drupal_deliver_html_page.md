# drupal_deliver_html_page()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2730–2841 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2730-L2841)

## Signature

```php
function drupal_deliver_html_page($page_callback_result)
```

## Documentation

```text
Packages and sends the result of a page callback to the browser as HTML.

@param $page_callback_result
  The result of a page callback. Can be one of:
  - NULL: to indicate no content.
  - An integer menu status constant: to indicate an error condition.
  - A string of HTML content.
  - A renderable array of content.

@see drupal_deliver_page()
```

## Code

```php
function drupal_deliver_html_page($page_callback_result) {
  // Emit the correct charset HTTP header, but not if the page callback
  // result is NULL, since that likely indicates that it printed something
  // in which case, no further headers may be sent, and not if code running
  // for this page request has already set the content type header.
  if (isset($page_callback_result) && is_null(drupal_get_http_header('Content-Type'))) {
    drupal_add_http_header('Content-Type', 'text/html; charset=utf-8');
  }

  // Send appropriate HTTP-Header for browsers and search engines.
  global $language;
  drupal_add_http_header('Content-Language', $language->language);

  // By default, do not allow the site to be rendered in an iframe on another
  // domain, but provide a variable to override this. If the code running for
  // this page request already set the X-Frame-Options header earlier, don't
  // overwrite it here.
  $frame_options = variable_get('x_frame_options', 'SAMEORIGIN');
  if ($frame_options && is_null(drupal_get_http_header('X-Frame-Options'))) {
    drupal_add_http_header('X-Frame-Options', $frame_options);
  }
  drupal_add_http_header('X-Content-Type-Options', 'nosniff');

  // Menu status constants are integers; page content is a string or array.
  if (is_int($page_callback_result)) {
    // @todo: Break these up into separate functions?
    switch ($page_callback_result) {
      case MENU_NOT_FOUND:
        // Print a 404 page.
        drupal_add_http_header('Status', '404 Not Found');

        watchdog('page not found', check_plain($_GET['q']), NULL, WATCHDOG_WARNING);

        // Check for and return a fast 404 page if configured.
        drupal_fast_404();

        // Keep old path for reference, and to allow forms to redirect to it.
        if (!isset($_GET['destination'])) {
          // Make sure that the current path is not interpreted as external URL.
          if (!url_is_external($_GET['q'])) {
            $_GET['destination'] = $_GET['q'];
          }
        }

        $path = drupal_get_normal_path(variable_get('site_404', ''));
        if ($path && $path != $_GET['q']) {
          // Custom 404 handler. Set the active item in case there are tabs to
          // display, or other dependencies on the path.
          menu_set_active_item($path);
          $return = menu_execute_active_handler($path, FALSE);
        }

        if (empty($return) || $return == MENU_NOT_FOUND || $return == MENU_ACCESS_DENIED) {
          // Standard 404 handler.
          drupal_set_title(t('Page not found'));
          $return = t('The requested page "@path" could not be found.', array('@path' => request_uri()));
        }

        drupal_set_page_content($return);
        $page = element_info('page');
        print drupal_render_page($page);
        break;

      case MENU_ACCESS_DENIED:
        // Print a 403 page.
        drupal_add_http_header('Status', '403 Forbidden');
        watchdog('access denied', check_plain($_GET['q']), NULL, WATCHDOG_WARNING);

        // Keep old path for reference, and to allow forms to redirect to it.
        if (!isset($_GET['destination'])) {
          // Make sure that the current path is not interpreted as external URL.
          if (!url_is_external($_GET['q'])) {
            $_GET['destination'] = $_GET['q'];
          }
        }

        $path = drupal_get_normal_path(variable_get('site_403', ''));
        if ($path && $path != $_GET['q']) {
          // Custom 403 handler. Set the active item in case there are tabs to
          // display or other dependencies on the path.
          menu_set_active_item($path);
          $return = menu_execute_active_handler($path, FALSE);
        }

        if (empty($return) || $return == MENU_NOT_FOUND || $return == MENU_ACCESS_DENIED) {
          // Standard 403 handler.
          drupal_set_title(t('Access denied'));
          $return = t('You are not authorized to access this page.');
        }

        print drupal_render_page($return);
        break;

      case MENU_SITE_OFFLINE:
        // Print a 503 page.
        drupal_maintenance_theme();
        drupal_add_http_header('Status', '503 Service unavailable');
        drupal_set_title(t('Site under maintenance'));
        print theme('maintenance_page', array('content' => filter_xss_admin(variable_get('maintenance_mode_message',
          t('@site is currently under maintenance. We should be back shortly. Thank you for your patience.', array('@site' => variable_get('site_name', 'Drupal')))))));
        break;
    }
  }
  elseif (isset($page_callback_result)) {
    // Print anything besides a menu constant, assuming it's not NULL or
    // undefined.
    print drupal_render_page($page_callback_result);
  }

  // Perform end-of-request tasks.
  drupal_page_footer();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
