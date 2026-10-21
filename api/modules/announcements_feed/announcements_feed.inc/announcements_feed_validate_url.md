# announcements_feed_validate_url()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 222–231 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L222-L231)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_validate_url($url)
```

## Documentation

```text
Check whether a link is controlled by drupal.org.

@param string $url
  URL to check.

@return bool
  Return TRUE if the URL is controlled by drupal.org.
```

## Code

```php
function announcements_feed_validate_url($url) {
  if (empty($url)) {
    return FALSE;
  }
  $host = parse_url($url, PHP_URL_HOST);

  // First character can only be a letter or a digit.
  // @see https://www.rfc-editor.org/rfc/rfc1123#page-13
  return $host && preg_match('/^([a-zA-Z0-9][a-zA-Z0-9\-_]*\.)?drupal\.org$/', $host);
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
