# aggregator_aggregator_process()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 21–48 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L21-L48)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_process()](../aggregator.api.php/hook_aggregator_process.md)

## Signature

```php
function aggregator_aggregator_process($feed)
```

## Documentation

```text
Implements hook_aggregator_process().
```

## Code

```php
function aggregator_aggregator_process($feed) {
  if (is_object($feed)) {
    if (is_array($feed->items)) {
      foreach ($feed->items as $item) {
        // Save this item. Try to avoid duplicate entries as much as possible. If
        // we find a duplicate entry, we resolve it and pass along its ID is such
        // that we can update it if needed.
        if (!empty($item['guid'])) {
          $entry = db_query("SELECT iid, timestamp FROM {aggregator_item} WHERE fid = :fid AND guid = :guid", array(':fid' => $feed->fid, ':guid' => $item['guid']))->fetchObject();
        }
        elseif ($item['link'] && $item['link'] != $feed->link && $item['link'] != $feed->url) {
          $entry = db_query("SELECT iid, timestamp FROM {aggregator_item} WHERE fid = :fid AND link = :link", array(':fid' => $feed->fid, ':link' => $item['link']))->fetchObject();
        }
        else {
          $entry = db_query("SELECT iid, timestamp FROM {aggregator_item} WHERE fid = :fid AND title = :title", array(':fid' => $feed->fid, ':title' => $item['title']))->fetchObject();
        }
        if (!$item['timestamp']) {
          $item['timestamp'] = isset($entry->timestamp) ? $entry->timestamp : REQUEST_TIME;
        }

        // Make sure the item title and author fit in the 255 varchar column.
        $item['title'] = truncate_utf8($item['title'], 255, TRUE, TRUE);
        $item['author'] = truncate_utf8($item['author'], 255, TRUE, TRUE);
        aggregator_save_item(array('iid' => (isset($entry->iid) ? $entry->iid : ''), 'fid' => $feed->fid, 'timestamp' => $item['timestamp'], 'title' => $item['title'], 'link' => $item['link'], 'author' => $item['author'], 'description' => $item['description'], 'guid' => $item['guid']));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
