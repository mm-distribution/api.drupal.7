# _drupal_html_to_mail_urls()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 637–657 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L637-L657)

## Signature

```php
function _drupal_html_to_mail_urls($match = NULL, $reset = FALSE)
```

## Documentation

```text
Keeps track of URLs and replaces them with placeholder tokens.

Callback for preg_replace_callback() within drupal_html_to_text().
```

## Code

```php
function _drupal_html_to_mail_urls($match = NULL, $reset = FALSE) {
  global $base_url, $base_path;
  static $urls = array(), $regexp;

  if ($reset) {
    // Reset internal URL list.
    $urls = array();
  }
  else {
    if (empty($regexp)) {
      $regexp = '@^' . preg_quote($base_path, '@') . '@';
    }
    if ($match) {
      list(, , $url, $label) = $match;
      // Ensure all URLs are absolute.
      $urls[] = strpos($url, '://') ? $url : preg_replace($regexp, $base_url . '/', $url);
      return $label . ' [' . count($urls) . ']';
    }
  }
  return $urls;
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
