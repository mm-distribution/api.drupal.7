# node_block_view()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2252–2275 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2252-L2275)
- **Module/theme:** node
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function node_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function node_block_view($delta = '') {
  $block = array();

  switch ($delta) {
    case 'syndicate':
      $block['subject'] = t('Syndicate');
      $block['content'] = theme('feed_icon', array('url' => 'rss.xml', 'title' => t('Syndicate')));
      break;

    case 'recent':
      if (user_access('access content')) {
        $block['subject'] = t('Recent content');
        if ($nodes = node_get_recent(variable_get('node_recent_block_count', 10))) {
          $block['content'] = theme('node_recent_block', array(
            'nodes' => $nodes,
          ));
        } else {
          $block['content'] = t('No content available.');
        }
      }
      break;
  }
  return $block;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
