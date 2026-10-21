# search_touch_node()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 783–789 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L783-L789)
- **Module/theme:** search

## Signature

```php
function search_touch_node($nid)
```

## Documentation

```text
Changes a node's changed timestamp to 'now' to force reindexing.

@param $nid
  The node ID of the node that needs reindexing.
```

## Code

```php
function search_touch_node($nid) {
  db_update('search_dataset')
    ->fields(array('reindex' => REQUEST_TIME))
    ->condition('type', 'node')
    ->condition('sid', $nid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
