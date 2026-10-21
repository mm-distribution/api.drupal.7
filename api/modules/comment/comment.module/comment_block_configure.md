# comment_block_configure()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 431–440 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L431-L440)
- **Module/theme:** comment
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function comment_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function comment_block_configure($delta = '') {
  $form['comment_block_count'] = array(
    '#type' => 'select',
    '#title' => t('Number of recent comments'),
    '#default_value' => variable_get('comment_block_count', 10),
    '#options' => drupal_map_assoc(array(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30)),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
