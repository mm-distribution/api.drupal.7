# aggregator_save_feed()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 499–567 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L499-L567)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_save_feed($edit)
```

## Documentation

```text
Add/edit/delete an aggregator feed.

@param $edit
  An associative array describing the feed to be added/edited/deleted.
```

## Code

```php
function aggregator_save_feed($edit) {
  if (!empty($edit['fid'])) {
    // An existing feed is being modified, delete the category listings.
    db_delete('aggregator_category_feed')
      ->condition('fid', $edit['fid'])
      ->execute();
  }
  if (!empty($edit['fid']) && !empty($edit['title'])) {
    db_update('aggregator_feed')
      ->condition('fid', $edit['fid'])
      ->fields(array(
        'title' => $edit['title'],
        'url' => $edit['url'],
        'refresh' => $edit['refresh'],
        'block' => $edit['block'],
      ))
      ->execute();
  }
  elseif (!empty($edit['fid'])) {
    $iids = db_query('SELECT iid FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $edit['fid']))->fetchCol();
    if ($iids) {
      db_delete('aggregator_category_item')
        ->condition('iid', $iids, 'IN')
        ->execute();
    }
    db_delete('aggregator_feed')->
      condition('fid', $edit['fid'])
      ->execute();
    db_delete('aggregator_item')
      ->condition('fid', $edit['fid'])
      ->execute();
    // Make sure there is no active block for this feed.
    if (module_exists('block')) {
      db_delete('block')
        ->condition('module', 'aggregator')
        ->condition('delta', 'feed-' . $edit['fid'])
        ->execute();
    }
  }
  elseif (!empty($edit['title'])) {
    $edit['fid'] = db_insert('aggregator_feed')
      ->fields(array(
        'title' => $edit['title'],
        'url' => $edit['url'],
        'refresh' => $edit['refresh'],
        'block' => $edit['block'],
        'link' => '',
        'description' => '',
        'image' => '',
      ))
      ->execute();

  }
  if (!empty($edit['title'])) {
    // The feed is being saved, save the categories as well.
    if (!empty($edit['category'])) {
      foreach ($edit['category'] as $cid => $value) {
        if ($value) {
          db_insert('aggregator_category_feed')
            ->fields(array(
              'fid' => $edit['fid'],
              'cid' => $cid,
            ))
            ->execute();
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
