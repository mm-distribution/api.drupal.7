# aggregator_block_info()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 348–359 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L348-L359)
- **Module/theme:** aggregator
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function aggregator_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function aggregator_block_info() {
  $blocks = array();
  $result = db_query('SELECT cid, title FROM {aggregator_category} ORDER BY title');
  foreach ($result as $category) {
    $blocks['category-' . $category->cid]['info'] = t('!title category latest items', array('!title' => $category->title));
  }
  $result = db_query('SELECT fid, title FROM {aggregator_feed} WHERE block <> 0 ORDER BY fid');
  foreach ($result as $feed) {
    $blocks['feed-' . $feed->fid]['info'] = t('!title feed latest items', array('!title' => $feed->title));
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
