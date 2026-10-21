# node_block_save()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2296–2300 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2296-L2300)
- **Module/theme:** node
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function node_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function node_block_save($delta = '', $edit = array()) {
  if ($delta == 'recent') {
    variable_set('node_recent_block_count', $edit['node_recent_block_count']);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
