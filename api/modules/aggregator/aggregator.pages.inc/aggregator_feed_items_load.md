# aggregator_feed_items_load()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 114–155 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L114-L155)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_feed_items_load($type, $data = NULL)
```

## Documentation

```text
Loads and optionally filters feed items.

@param $type
  The type of filter for the items. Possible values are:
  - sum: No filtering.
  - source: Filter the feed items, limiting the result to items from a
    single source.
  - category: Filter the feed items by category.
@param $data
  Feed or category data used for filtering. The type and value of $data
  depends on $type:
  - source: $data is an object with $data->fid identifying the feed used to
    as filter.
  - category: $data is an array with $data['cid'] being the category id to
    filter on.
  The $data parameter is not used when $type is 'sum'.

@return
  An array of the feed items.
```

## Code

```php
function aggregator_feed_items_load($type, $data = NULL) {
  $items = array();
  switch ($type) {
    case 'sum':
      $query = db_select('aggregator_item', 'i');
      $query->join('aggregator_feed', 'f', 'i.fid = f.fid');
      $query->fields('i');
      $query->addField('f', 'title', 'ftitle');
      $query->addField('f', 'link', 'flink');
      break;
    case 'source':
      $query = db_select('aggregator_item', 'i');
      $query
        ->fields('i')
        ->condition('i.fid', $data->fid);
      break;
    case 'category':
      $query = db_select('aggregator_category_item', 'c');
      $query->leftJoin('aggregator_item', 'i', 'c.iid = i.iid');
      $query->leftJoin('aggregator_feed', 'f', 'i.fid = f.fid');
      $query
        ->fields('i')
        ->condition('cid', $data['cid']);
      $query->addField('f', 'title', 'ftitle');
      $query->addField('f', 'link', 'flink');
      break;
  }

  $result = $query
    ->extend('PagerDefault')
    ->limit(20)
    ->orderBy('i.timestamp', 'DESC')
    ->orderBy('i.iid', 'DESC')
    ->execute();

  foreach ($result as $item) {
    $item->categories = db_query('SELECT c.title, c.cid FROM {aggregator_category_item} ci LEFT JOIN {aggregator_category} c ON ci.cid = c.cid WHERE ci.iid = :iid ORDER BY c.title', array(':iid' => $item->iid))->fetchAll();
    $items[] = $item;
  }

  return $items;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
