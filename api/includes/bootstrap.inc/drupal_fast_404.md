# drupal_fast_404()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2995–3007 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2995-L3007)

## Signature

```php
function drupal_fast_404()
```

## Documentation

```text
Returns a simple 404 Not Found page.

If fast 404 pages are enabled, and this is a matching page then print a
simple 404 page and exit.

This function is called from drupal_deliver_html_page() at the time when a
a normal 404 page is generated, but it can also optionally be called directly
from settings.php to prevent a Drupal bootstrap on these pages. See
documentation in settings.php for the benefits and drawbacks of using this.

Paths to dynamically-generated content, such as image styles, should also be
accounted for in this function.
```

## Code

```php
function drupal_fast_404() {
  $exclude_paths = variable_get('404_fast_paths_exclude', FALSE);
  if ($exclude_paths && !preg_match($exclude_paths, $_GET['q'])) {
    $fast_paths = variable_get('404_fast_paths', FALSE);
    if ($fast_paths && preg_match($fast_paths, $_GET['q'])) {
      drupal_add_http_header('Status', '404 Not Found');
      $fast_404_html = variable_get('404_fast_html', '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" "http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL "@path" was not found on this server.</p></body></html>');
      // Replace @path in the variable with the page path.
      print strtr($fast_404_html, array('@path' => check_plain(request_uri())));
      exit;
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
