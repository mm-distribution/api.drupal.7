# aggregator_save_item()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 151–185 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L151-L185)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_save_item($edit)
```

## Documentation

```text
Adds/edits/deletes an aggregator item.

@param $edit
  An associative array describing the item to be added/edited/deleted.
```

## Code

```php
function aggregator_save_item($edit) {
  if ($edit['title'] && empty($edit['iid'])) {
    $edit['iid'] = db_insert('aggregator_item')
      ->fields(array(
        'title' => $edit['title'],
        'link' => $edit['link'],
        'author' => $edit['author'],
        'description' => $edit['description'],
        'guid' => $edit['guid'],
        'timestamp' => $edit['timestamp'],
        'fid' => $edit['fid'],
      ))
      ->execute();
  }
  if ($edit['iid'] && !$edit['title']) {
    db_delete('aggregator_item')
      ->condition('iid', $edit['iid'])
      ->execute();
    db_delete('aggregator_category_item')
      ->condition('iid', $edit['iid'])
      ->execute();
  }
  elseif ($edit['title'] && $edit['link']) {
    // file the items in the categories indicated by the feed
    $result = db_query('SELECT cid FROM {aggregator_category_feed} WHERE fid = :fid', array(':fid' => $edit['fid']));
    foreach ($result as $category) {
      db_merge('aggregator_category_item')
        ->key(array(
          'iid' => $edit['iid'],
          'cid' => $category->cid,
        ))
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
