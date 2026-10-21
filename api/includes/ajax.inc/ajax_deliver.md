# ajax_deliver()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 469–518 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L469-L518)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_deliver($page_callback_result)
```

## Documentation

```text
Packages and sends the result of a page callback as an Ajax response.

This function is the equivalent of drupal_deliver_html_page(), but for Ajax
requests. Like that function, it:
- Adds needed HTTP headers.
- Prints rendered output.
- Performs end-of-request tasks.

@param $page_callback_result
  The result of a page callback. Can be one of:
  - NULL: to indicate no content.
  - An integer menu status constant: to indicate an error condition.
  - A string of HTML content.
  - A renderable array of content.

@see drupal_deliver_html_page()
```

## Code

```php
function ajax_deliver($page_callback_result) {
  // Browsers do not allow JavaScript to read the contents of a user's local
  // files. To work around that, the jQuery Form plugin submits forms containing
  // a file input element to an IFRAME, instead of using XHR. Browsers do not
  // normally expect JSON strings as content within an IFRAME, so the response
  // must be customized accordingly.
  // @see http://malsup.com/jquery/form/#file-upload
  // @see Drupal.ajax.prototype.beforeSend()
  $iframe_upload = !empty($_POST['ajax_iframe_upload']);

  // Emit a Content-Type HTTP header if none has been added by the page callback
  // or by a wrapping delivery callback.
  if (is_null(drupal_get_http_header('Content-Type'))) {
    if (!$iframe_upload) {
      // Standard JSON can be returned to a browser's XHR object, and to
      // non-browser user agents.
      // @see http://www.ietf.org/rfc/rfc4627.txt?number=4627
      drupal_add_http_header('Content-Type', 'application/json; charset=utf-8');
    }
    else {
      // Browser IFRAMEs expect HTML. With most other content types, Internet
      // Explorer presents the user with a download prompt.
      drupal_add_http_header('Content-Type', 'text/html; charset=utf-8');
    }
  }

  // Let ajax.js know that this response is safe to process.
  ajax_set_verification_header();

  // Print the response.
  $commands = ajax_prepare_response($page_callback_result);
  $json = ajax_render($commands);
  if (!$iframe_upload) {
    // Standard JSON can be returned to a browser's XHR object, and to
    // non-browser user agents.
    print $json;
  }
  else {
    // Browser IFRAMEs expect HTML. Browser extensions, such as Linkification
    // and Skype's Browser Highlighter, convert URLs, phone numbers, etc. into
    // links. This corrupts the JSON response. Protect the integrity of the
    // JSON data by making it the value of a textarea.
    // @see http://malsup.com/jquery/form/#file-upload
    // @see http://drupal.org/node/1009382
    print '<textarea>' . $json . '</textarea>';
  }

  // Perform end-of-request tasks.
  ajax_footer();
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
