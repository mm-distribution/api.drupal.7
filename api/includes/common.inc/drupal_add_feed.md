# drupal_add_feed()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 368–384 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L368-L384)

## Signature

```php
function drupal_add_feed($url = NULL, $title = '')
```

## Documentation

```text
Adds a feed URL for the current page.

This function can be called as long the HTML header hasn't been sent.

@param $url
  An internal system path or a fully qualified external URL of the feed.
@param $title
  The title of the feed.
```

## Code

```php
function drupal_add_feed($url = NULL, $title = '') {
  $stored_feed_links = &drupal_static(__FUNCTION__, array());

  if (isset($url)) {
    $stored_feed_links[$url] = theme('feed_icon', array('url' => $url, 'title' => $title));

    drupal_add_html_head_link(array(
      'rel' => 'alternate',
      'type' => 'application/rss+xml',
      'title' => $title,
      // Force the URL to be absolute, for consistency with other <link> tags
      // output by Drupal.
      'href' => url($url, array('absolute' => TRUE)),
    ));
  }
  return $stored_feed_links;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
