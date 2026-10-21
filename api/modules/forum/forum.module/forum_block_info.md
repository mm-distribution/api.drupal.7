# forum_block_info()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 645–657 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L645-L657)
- **Module/theme:** forum
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function forum_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function forum_block_info() {
  $blocks['active'] = array(
    'info' => t('Active forum topics'),
    'cache' => DRUPAL_CACHE_CUSTOM,
    'properties' => array('administrative' => TRUE),
  );
  $blocks['new'] = array(
    'info' => t('New forum topics'),
    'cache' => DRUPAL_CACHE_CUSTOM,
    'properties' => array('administrative' => TRUE),
  );
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
