# aggregator_aggregator_parse()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 21–54 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L21-L54)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_parse()](../aggregator.api.php/hook_aggregator_parse.md)

## Signature

```php
function aggregator_aggregator_parse($feed)
```

## Documentation

```text
Implements hook_aggregator_parse().
```

## Code

```php
function aggregator_aggregator_parse($feed) {
  global $channel, $image;

  // Filter the input data.
  if (aggregator_parse_feed($feed->source_string, $feed)) {
    $modified = empty($feed->http_headers['last-modified']) ? 0 : strtotime($feed->http_headers['last-modified']);

    // Prepare the channel data.
    foreach ($channel as $key => $value) {
      $channel[$key] = trim($value);
    }

    // Prepare the image data (if any).
    foreach ($image as $key => $value) {
      $image[$key] = trim($value);
    }

    $etag = empty($feed->http_headers['etag']) ? '' : $feed->http_headers['etag'];

    // Add parsed data to the feed object.
    $feed->link = !empty($channel['link']) ? $channel['link'] : '';
    $feed->description = !empty($channel['description']) ? $channel['description'] : '';
    $feed->image = !empty($image['url']) ? $image['url'] : '';
    $feed->etag = $etag;
    $feed->modified = $modified;

    // Clear the cache.
    cache_clear_all();

    return TRUE;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
