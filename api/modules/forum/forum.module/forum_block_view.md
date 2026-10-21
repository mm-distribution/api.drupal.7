# forum_block_view()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 685–710 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L685-L710)
- **Module/theme:** forum
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function forum_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generates a block containing the currently active forum topics and the most
recently added forum topics.
```

## Code

```php
function forum_block_view($delta = '') {
  $query = db_select('forum_index', 'f')
    ->fields('f')
    ->addTag('node_access');
  switch ($delta) {
    case 'active':
      $title = t('Active forum topics');
      $query
        ->orderBy('f.last_comment_timestamp', 'DESC')
        ->range(0, variable_get('forum_block_num_active', '5'));
      break;

    case 'new':
      $title = t('New forum topics');
      $query
        ->orderBy('f.created', 'DESC')
        ->range(0, variable_get('forum_block_num_new', '5'));
      break;
  }

  $block['subject'] = $title;
  // Cache based on the altered query. Enables us to cache with node access enabled.
  $block['content'] = drupal_render_cache_by_query($query, 'forum_block_view');
  $block['content']['#access'] = user_access('access content');
  return $block;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
