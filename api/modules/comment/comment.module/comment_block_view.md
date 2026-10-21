# comment_block_view()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 454–461 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L454-L461)
- **Module/theme:** comment
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function comment_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generates a block with the most recent comments.
```

## Code

```php
function comment_block_view($delta = '') {
  if (user_access('access comments')) {
    $block['subject'] = t('Recent comments');
    $block['content'] = theme('comment_block');

    return $block;
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
