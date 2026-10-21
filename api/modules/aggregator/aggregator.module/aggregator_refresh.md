# aggregator_refresh()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 620–680 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L620-L680)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_refresh($feed)
```

## Documentation

```text
Checks a news feed for new items.

@param $feed
  An object describing the feed to be refreshed.
```

## Code

```php
function aggregator_refresh($feed) {
  // Store feed URL to track changes.
  $feed_url = $feed->url;

  // Fetch the feed.
  list($fetcher, $parser, $processors) = _aggregator_get_variables();
  $success = module_invoke($fetcher, 'aggregator_fetch', $feed);

  // We store the hash of feed data in the database. When refreshing a
  // feed we compare stored hash and new hash calculated from downloaded
  // data. If both are equal we say that feed is not updated.
  $hash = hash('sha256', $feed->source_string);

  if ($success && ($feed->hash != $hash)) {
    // Parse the feed.
    if (module_invoke($parser, 'aggregator_parse', $feed)) {
      // Update feed with parsed data.
      db_merge('aggregator_feed')
        ->key(array('fid' => $feed->fid))
        ->fields(array(
          'url' => $feed->url,
          'link' => empty($feed->link) ? $feed->url : $feed->link,
          'description' => empty($feed->description) ? '' : $feed->description,
          'image' => empty($feed->image) ? '' : $feed->image,
          'hash' => $hash,
          'etag' => empty($feed->etag) ? '' : $feed->etag,
          'modified' => empty($feed->modified) ? 0 : $feed->modified,
        ))
        ->execute();

      // Log if feed URL has changed.
      if ($feed->url != $feed_url) {
        watchdog('aggregator', 'Updated URL for feed %title to %url.', array('%title' => $feed->title, '%url' => $feed->url));
      }

      watchdog('aggregator', 'There is new syndicated content from %site.', array('%site' => $feed->title));
      drupal_set_message(t('There is new syndicated content from %site.', array('%site' => $feed->title)));

      // If there are items on the feed, let all enabled processors do their work on it.
      if (@count($feed->items)) {
        foreach ($processors as $processor) {
          module_invoke($processor, 'aggregator_process', $feed);
        }
      }
    }
  }
  else {
    drupal_set_message(t('There is no new syndicated content from %site.', array('%site' => $feed->title)));
  }

  // Regardless of successful or not, indicate that this feed has been checked.
  db_update('aggregator_feed')
    ->fields(array('checked' => REQUEST_TIME, 'queued' => 0))
    ->condition('fid', $feed->fid)
    ->execute();

  // Expire old feed items.
  if (function_exists('aggregator_expire')) {
    aggregator_expire($feed);
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
