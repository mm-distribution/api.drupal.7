# node_block_info()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2238–2247 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2238-L2247)
- **Module/theme:** node
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function node_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function node_block_info() {
  $blocks['syndicate']['info'] = t('Syndicate');
  // Not worth caching.
  $blocks['syndicate']['cache'] = DRUPAL_NO_CACHE;

  $blocks['recent']['info'] = t('Recent content');
  $blocks['recent']['properties']['administrative'] = TRUE;

  return $blocks;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
