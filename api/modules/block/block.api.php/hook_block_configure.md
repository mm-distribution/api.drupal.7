# hook_block_configure()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 157–169 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L157-L169)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_configure($delta = '')
```

## Documentation

```text
Define a configuration form for a block.

@param $delta
  Which block is being configured. This is a unique identifier for the block
  within the module, defined in hook_block_info().

@return
  A configuration form, if one is needed for your block beyond the standard
  elements that the block module provides (block title, visibility, etc.).

For a detailed usage example, see block_example.module.

@see hook_block_info()
@see hook_block_save()
```

## Code

```php
function hook_block_configure($delta = '') {
  // This example comes from node.module.
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

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_configure()".

- [aggregator_block_configure()](../../aggregator/aggregator.module/aggregator_block_configure.md) — `modules/aggregator/aggregator.module`
- [block_block_configure()](../block.module/block_block_configure.md) — `modules/block/block.module`
- [blog_block_configure()](../../blog/blog.module/blog_block_configure.md) — `modules/blog/blog.module`
- [book_block_configure()](../../book/book.module/book_block_configure.md) — `modules/book/book.module`
- [comment_block_configure()](../../comment/comment.module/comment_block_configure.md) — `modules/comment/comment.module`
- [forum_block_configure()](../../forum/forum.module/forum_block_configure.md) — `modules/forum/forum.module`
- [node_block_configure()](../../node/node.module/node_block_configure.md) — `modules/node/node.module`
- [profile_block_configure()](../../profile/profile.module/profile_block_configure.md) — `modules/profile/profile.module`
- [statistics_block_configure()](../../statistics/statistics.module/statistics_block_configure.md) — `modules/statistics/statistics.module`
- [user_block_configure()](../../user/user.module/user_block_configure.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
