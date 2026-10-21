# aggregator_block_view()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 396–432 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L396-L432)
- **Module/theme:** aggregator
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function aggregator_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generates blocks for the latest news items in each category and feed.
```

## Code

```php
function aggregator_block_view($delta = '') {
  if (user_access('access news feeds')) {
    $block = array();
    list($type, $id) = explode('-', $delta);
    $result = FALSE;
    switch ($type) {
      case 'feed':
        if ($feed = db_query('SELECT fid, title, block FROM {aggregator_feed} WHERE block <> 0 AND fid = :fid', array(':fid' => $id))->fetchObject()) {
          $block['subject'] = check_plain($feed->title);
          $result = db_query_range("SELECT * FROM {aggregator_item} WHERE fid = :fid ORDER BY timestamp DESC, iid DESC", 0, $feed->block, array(':fid' => $id));
          $read_more = theme('more_link', array('url' => 'aggregator/sources/' . $feed->fid, 'title' => t("View this feed's recent news.")));
        }
        break;

      case 'category':
        if ($category = db_query('SELECT cid, title, block FROM {aggregator_category} WHERE cid = :cid', array(':cid' => $id))->fetchObject()) {
          $block['subject'] = check_plain($category->title);
          $result = db_query_range('SELECT i.* FROM {aggregator_category_item} ci LEFT JOIN {aggregator_item} i ON ci.iid = i.iid WHERE ci.cid = :cid ORDER BY i.timestamp DESC, i.iid DESC', 0, $category->block, array(':cid' => $category->cid));
          $read_more = theme('more_link', array('url' => 'aggregator/categories/' . $category->cid, 'title' => t("View this category's recent news.")));
        }
        break;
    }

    $items = array();
    if (!empty($result)) {
      foreach ($result as $item) {
        $items[] = theme('aggregator_block_item', array('item' => $item));
      }
    }

    // Only display the block if there are items to show.
    if (count($items) > 0) {
      $block['content'] = theme('item_list', array('items' => $items)) . $read_more;
    }
    return $block;
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
