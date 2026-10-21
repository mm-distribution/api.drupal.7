# ajax_prepare_response()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 533–585 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L533-L585)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_prepare_response($page_callback_result)
```

## Documentation

```text
Converts the return value of a page callback into an Ajax commands array.

@param $page_callback_result
  The result of a page callback. Can be one of:
  - NULL: to indicate no content.
  - An integer menu status constant: to indicate an error condition.
  - A string of HTML content.
  - A renderable array of content.

@return
  An Ajax commands array that can be passed to ajax_render().
```

## Code

```php
function ajax_prepare_response($page_callback_result) {
  $commands = array();
  if (!isset($page_callback_result)) {
    // Simply delivering an empty commands array is sufficient. This results
    // in the Ajax request being completed, but nothing being done to the page.
  }
  elseif (is_int($page_callback_result)) {
    switch ($page_callback_result) {
      case MENU_NOT_FOUND:
        $commands[] = ajax_command_alert(t('The requested page could not be found.'));
        break;

      case MENU_ACCESS_DENIED:
        $commands[] = ajax_command_alert(t('You are not authorized to access this page.'));
        break;

      case MENU_SITE_OFFLINE:
        $commands[] = ajax_command_alert(filter_xss_admin(variable_get('maintenance_mode_message',
          t('@site is currently under maintenance. We should be back shortly. Thank you for your patience.', array('@site' => variable_get('site_name', 'Drupal'))))));
        break;
    }
  }
  elseif (is_array($page_callback_result) && isset($page_callback_result['#type']) && ($page_callback_result['#type'] == 'ajax')) {
    // Complex Ajax callbacks can return a result that contains an error message
    // or a specific set of commands to send to the browser.
    $page_callback_result += element_info('ajax');
    $error = $page_callback_result['#error'];
    if (isset($error) && $error !== FALSE) {
      if ((empty($error) || $error === TRUE)) {
        $error = t('An error occurred while handling the request: The server received invalid input.');
      }
      $commands[] = ajax_command_alert($error);
    }
    else {
      $commands = $page_callback_result['#commands'];
    }
  }
  else {
    // Like normal page callbacks, simple Ajax callbacks can return HTML
    // content, as a string or render array. This HTML is inserted in some
    // relationship to #ajax['wrapper'], as determined by which jQuery DOM
    // manipulation method is used. The method used is specified by
    // #ajax['method']. The default method is 'replaceWith', which completely
    // replaces the old wrapper element and its content with the new HTML.
    $html = is_string($page_callback_result) ? $page_callback_result : drupal_render($page_callback_result);
    $commands[] = ajax_command_insert(NULL, $html);
    // Add the status messages inside the new content's wrapper element, so that
    // on subsequent Ajax requests, it is treated as old content.
    $commands[] = ajax_command_prepend(NULL, theme('status_messages'));
  }

  return $commands;
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
