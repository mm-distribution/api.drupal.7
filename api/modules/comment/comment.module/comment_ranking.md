# comment_ranking()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2690–2705 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2690-L2705)
- **Module/theme:** comment
- **Implements:** [hook_ranking()](../../node/node.api.php/hook_ranking.md)

## Signature

```php
function comment_ranking()
```

## Documentation

```text
Implements hook_ranking().
```

## Code

```php
function comment_ranking() {
  return array(
    'comments' => array(
      'title' => t('Number of comments'),
      'join' => array(
        'type' => 'LEFT',
        'table' => 'node_comment_statistics',
        'alias' => 'node_comment_statistics',
        'on' => 'node_comment_statistics.nid = i.sid',
      ),
      // Inverse law that maps the highest reply count on the site to 1 and 0 to 0.
      'score' => '2.0 - 2.0 / (1.0 + node_comment_statistics.comment_count * CAST(:scale AS DECIMAL))',
      'arguments' => array(':scale' => variable_get('node_cron_comments_scale', 0)),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
