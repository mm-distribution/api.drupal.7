# hook_block_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/block/block.api.php`](_file.md), lines 217–246 · [local source](../../../../source/modules/block/block.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php#L217-L246)
- **Module/theme:** block
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_block_view($delta = '')
```

## Documentation

```text
Return a rendered or renderable view of a block.

@param $delta
  Which block to render. This is a unique identifier for the block
  within the module, defined in hook_block_info().

@return
  Either an empty array so the block will not be shown or an array containing
  the following elements:
  - subject: The default localized title of the block. If the block does not
    have a default title, this should be set to NULL.
  - content: The content of the block's body. This may be a renderable array
    (preferable) or a string containing rendered HTML content. If the content
    is empty the block will not be shown.

For a detailed usage example, see block_example.module.

@see hook_block_info()
@see hook_block_view_alter()
@see hook_block_view_MODULE_DELTA_alter()
```

## Code

```php
function hook_block_view($delta = '') {
  // This example is adapted from node.module.
  $block = array();

  switch ($delta) {
    case 'syndicate':
      $block['subject'] = t('Syndicate');
      $block['content'] = array(
        '#theme' => 'feed_icon',
        '#url' => 'rss.xml',
        '#title' => t('Syndicate'),
      );
      break;

    case 'recent':
      if (user_access('access content')) {
        $block['subject'] = t('Recent content');
        if ($nodes = node_get_recent(variable_get('node_recent_block_count', 10))) {
          $block['content'] = array(
            '#theme' => 'node_recent_block',
            '#nodes' => $nodes,
          );
        } else {
          $block['content'] = t('No content available.');
        }
      }
      break;
  }
  return $block;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_block_view()".

- [aggregator_block_view()](../../aggregator/aggregator.module/aggregator_block_view.md) — `modules/aggregator/aggregator.module`
- [taxonomy_test_block_view()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_block_view.md) — `modules/simpletest/tests/taxonomy_test.module`
- [block_block_view()](../block.module/block_block_view.md) — `modules/block/block.module`
- [block_test_block_view()](../tests/block_test.module/block_test_block_view.md) — `modules/block/tests/block_test.module`
- [blog_block_view()](../../blog/blog.module/blog_block_view.md) — `modules/blog/blog.module`
- [book_block_view()](../../book/book.module/book_block_view.md) — `modules/book/book.module`
- [comment_block_view()](../../comment/comment.module/comment_block_view.md) — `modules/comment/comment.module`
- [forum_block_view()](../../forum/forum.module/forum_block_view.md) — `modules/forum/forum.module`
- [locale_block_view()](../../locale/locale.module/locale_block_view.md) — `modules/locale/locale.module`
- [menu_block_view()](../../menu/menu.module/menu_block_view.md) — `modules/menu/menu.module`
- [node_block_view()](../../node/node.module/node_block_view.md) — `modules/node/node.module`
- [poll_block_view()](../../poll/poll.module/poll_block_view.md) — `modules/poll/poll.module`
- [profile_block_view()](../../profile/profile.module/profile_block_view.md) — `modules/profile/profile.module`
- [search_block_view()](../../search/search.module/search_block_view.md) — `modules/search/search.module`
- [shortcut_block_view()](../../shortcut/shortcut.module/shortcut_block_view.md) — `modules/shortcut/shortcut.module`
- [statistics_block_view()](../../statistics/statistics.module/statistics_block_view.md) — `modules/statistics/statistics.module`
- [system_block_view()](../../system/system.module/system_block_view.md) — `modules/system/system.module`
- [user_block_view()](../../user/user.module/user_block_view.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/block/block.api.php](https://github.com/drupal/drupal/blob/7.103/modules/block/block.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
