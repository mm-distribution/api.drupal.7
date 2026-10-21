# announcements_feed_fetch()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 92–132 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L92-L132)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_fetch($force = FALSE)
```

## Documentation

```text
Fetches the feed either from a local cache or fresh remotely.

The feed follows the "JSON Feed" format:
- https://www.jsonfeed.org/version/1.1/

The structure of an announcement item in the feed is:
  - id: Id.
  - title: Title of the announcement.
  - content_html: Announcement teaser.
  - url: URL
  - date_modified: Last updated timestamp.
  - date_published: Created timestamp.
  - _drupalorg.featured: 1 if featured, 0 if not featured.
  - _drupalorg.version: Target version of Drupal, as a Composer version.

@param bool $force
  (optional) Whether to always fetch new items or not. Defaults to FALSE.

@return array
  An array of announcements from the feed relevant to the Drupal version.
  The array is empty if there were no matching announcements. If an error
  occurred while fetching/decoding the feed, it is thrown as an exception.

@throws Exception
```

## Code

```php
function announcements_feed_fetch($force = FALSE) {
  $announcements = cache_get('announcements_feed');
  if ($force || empty($announcements)) {
    $announcements_feed_json_url = variable_get('announcements_feed_json_url', ANNOUNCEMENTS_FEED_DEFAULT_JSON_URL);
    $response = drupal_http_request($announcements_feed_json_url);
    if ($response->code == 200) {
      $feeds = json_decode($response->data, TRUE);
      if (!isset($feeds['items'])) {
        watchdog('announcements_feed', 'The feed format is not valid.', NULL, WATCHDOG_ERROR);
        throw new Exception('Announcements feed JSON format is invalid');
      }
      $announcements = array();
      if ($feeds['items']) {
        $announcements = $feeds['items'];
      }
      $announcements = array_filter($announcements, 'announcements_feed_filter_announcements');
      cache_set('announcements_feed', $announcements, 'cache', REQUEST_TIME + variable_get('announcements_feed_max_age', ANNOUNCEMENTS_FEED_DEFAULT_MAX_AGE));
    }
    else {
      watchdog(
        'announcements_feed',
        'The feed failed to fetch with an error code: @code, error message: @message.',
        array('@code' => $response->code, '@message' => $response->error),
        WATCHDOG_ERROR
      );
      throw new Exception($response->error, $response->code);
    }
  }
  else {
    $announcements = $announcements->data;
  }
  // The drupal.org endpoint is sorted by created date in descending order.
  // We will limit the announcements based on the configuration limit.
  $announcements_feed_limit = variable_get('announcements_feed_limit', ANNOUNCEMENTS_FEED_DEFAULT_LIMIT);
  $announcements = array_slice($announcements, 0, $announcements_feed_limit);
  // For the remaining announcements, put all the featured announcements
  // before the rest.
  uasort($announcements, 'announcements_feed_sort_featured');

  return $announcements;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
