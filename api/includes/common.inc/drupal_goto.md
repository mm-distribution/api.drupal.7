# drupal_goto()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 682–715 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L682-L715)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_goto($path = '', array $options = array(), $http_response_code = 302)
```

## Documentation

```text
Sends the user to a different page.

This issues an on-site HTTP redirect. The function makes sure the redirected
URL is formatted correctly.

Usually the redirected URL is constructed from this function's input
parameters. However you may override that behavior by setting a
destination in either the $_REQUEST-array (i.e. by using
the query string of an URI) This is used to direct the user back to
the proper page after completing a form. For example, after editing
a post on the 'admin/content'-page or after having logged on using the
'user login'-block in a sidebar. The function drupal_get_destination()
can be used to help set the destination URL.

Drupal will ensure that messages set by drupal_set_message() and other
session data are written to the database before the user is redirected.

This function ends the request; use it instead of a return in your menu
callback.

@param $path
  (optional) A Drupal path or a full URL, which will be passed to url() to
  compute the redirect for the URL.
@param $options
  (optional) An associative array of additional URL options to pass to url().
@param $http_response_code
  (optional) The HTTP status code to use for the redirection, defaults to
  302. The valid values for 3xx redirection status codes are defined in
  @link http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3 RFC 2616 @endlink
  and the
  @link http://tools.ietf.org/html/draft-reschke-http-status-308-07 draft for the new HTTP status codes: @endlink
  - 301: Moved Permanently (the recommended value for most redirects).
  - 302: Found (default in Drupal and PHP, sometimes used for spamming search
    engines).
  - 303: See Other.
  - 304: Not Modified.
  - 305: Use Proxy.
  - 307: Temporary Redirect.

@see drupal_get_destination()
@see url()
```

## Code

```php
function drupal_goto($path = '', array $options = array(), $http_response_code = 302) {
  // A destination in $_GET always overrides the function arguments.
  // We do not allow absolute URLs to be passed via $_GET, as this can be an attack vector.
  if (isset($_GET['destination']) && !url_is_external($_GET['destination'])) {
    $destination = drupal_parse_url($_GET['destination']);
    // Double check the path derived by drupal_parse_url() is not external.
    if (!url_is_external($destination['path'])) {
      $path = $destination['path'];
    }
    $options['query'] = $destination['query'];
    $options['fragment'] = $destination['fragment'];
  }

  // In some cases modules call drupal_goto(current_path()). We need to ensure
  // that such a redirect is not to an external URL.
  if ($path === current_path() && empty($options['external']) && url_is_external($path)) {
    // Force url() to generate a non-external URL.
    $options['external'] = FALSE;
  }

  drupal_alter('drupal_goto', $path, $options, $http_response_code);

  // The 'Location' HTTP header must be absolute.
  $options['absolute'] = TRUE;

  $url = url($path, $options);

  header('Location: ' . $url, TRUE, $http_response_code);

  // The "Location" header sends a redirect status code to the HTTP daemon. In
  // some cases this can be wrong, so we make sure none of the code below the
  // drupal_goto() call gets executed upon redirection.
  drupal_exit($url);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
