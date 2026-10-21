# node_search_reset()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1653–1658 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1653-L1658)
- **Module/theme:** node
- **Implements:** [hook_search_reset()](../../search/search.api.php/hook_search_reset.md)

## Signature

```php
function node_search_reset()
```

## Documentation

```text
Implements hook_search_reset().
```

## Code

```php
function node_search_reset() {
  db_update('search_dataset')
    ->fields(array('reindex' => REQUEST_TIME))
    ->condition('type', 'node')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
