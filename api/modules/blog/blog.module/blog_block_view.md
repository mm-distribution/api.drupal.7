# blog_block_view()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 232–257 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L232-L257)
- **Module/theme:** blog
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function blog_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Displays the most recent 10 blog titles.
```

## Code

```php
function blog_block_view($delta = '') {
  global $user;

  if (user_access('access content')) {
    $result = db_select('node', 'n')
      ->fields('n', array('nid', 'title', 'created'))
      ->condition('type', 'blog')
      ->condition('status', 1)
      ->orderBy('created', 'DESC')
      ->range(0, variable_get('blog_block_count', 10))
      ->addTag('node_access')
      ->execute();

    if ($node_title_list = node_title_list($result)) {
      $block['subject'] = t('Recent blog posts');
      $block['content']['blog_list'] = $node_title_list;
      $block['content']['blog_more'] = array(
        '#theme' => 'more_link',
        '#url' => 'blog',
        '#title' => t('Read the latest blog entries.'),
      );

      return $block;
    }
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
