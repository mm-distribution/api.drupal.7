# node_block_configure()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2280–2291 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2280-L2291)
- **Module/theme:** node
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function node_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function node_block_configure($delta = '') {
  $form = array();
  if ($delta == 'recent') {
    $form['node_recent_block_count'] = array(
      '#type' => 'select',
      '#title' => t('Number of recent content items to display'),
      '#default_value' => variable_get('node_recent_block_count', 10),
      '#options' => drupal_map_assoc(array(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30)),
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
