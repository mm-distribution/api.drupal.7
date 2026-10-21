# hook_block_save()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 188–193 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L188-L193)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_save($delta = '', $edit = array())
```

## Documentation

```text
Save the configuration options from hook_block_configure().

This hook allows you to save the block-specific configuration settings
defined within your hook_block_configure().

@param $delta
  Which block is being configured. This is a unique identifier for the block
  within the module, defined in hook_block_info().
@param $edit
  The submitted form data from the configuration form.

For a detailed usage example, see block_example.module.

@see hook_block_configure()
@see hook_block_info()
```

## Code

```php
function hook_block_save($delta = '', $edit = array()) {
  // This example comes from node.module.
  if ($delta == 'recent') {
    variable_set('node_recent_block_count', $edit['node_recent_block_count']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_save()".

- [aggregator_block_save()](../../aggregator/aggregator.module/aggregator_block_save.md) — `modules/aggregator/aggregator.module`
- [block_block_save()](../block.module/block_block_save.md) — `modules/block/block.module`
- [blog_block_save()](../../blog/blog.module/blog_block_save.md) — `modules/blog/blog.module`
- [book_block_save()](../../book/book.module/book_block_save.md) — `modules/book/book.module`
- [comment_block_save()](../../comment/comment.module/comment_block_save.md) — `modules/comment/comment.module`
- [forum_block_save()](../../forum/forum.module/forum_block_save.md) — `modules/forum/forum.module`
- [node_block_save()](../../node/node.module/node_block_save.md) — `modules/node/node.module`
- [profile_block_save()](../../profile/profile.module/profile_block_save.md) — `modules/profile/profile.module`
- [statistics_block_save()](../../statistics/statistics.module/statistics_block_save.md) — `modules/statistics/statistics.module`
- [user_block_save()](../../user/user.module/user_block_save.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
