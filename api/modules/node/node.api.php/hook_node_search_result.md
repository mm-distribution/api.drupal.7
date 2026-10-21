# hook_node_search_result()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 671–674 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L671-L674)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_search_result($node)
```

## Documentation

```text
Act on a node being displayed as a search result.

This hook is invoked from node_search_execute(), after node_load() and
node_view() have been called.

@param $node
  The node being displayed in a search result.

@return array
  Extra information to be displayed with search result. This information
  should be presented as an associative array. It will be concatenated with
  the post information (last updated, author) in the default search result
  theming.

@see template_preprocess_search_result()
@see search-result.tpl.php

@ingroup node_api_hooks
```

## Code

```php
function hook_node_search_result($node) {
  $comments = db_query('SELECT comment_count FROM {node_comment_statistics} WHERE nid = :nid', array('nid' => $node->nid))->fetchField();
  return array('comment' => format_plural($comments, '1 comment', '@count comments'));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_search_result()".

- [comment_node_search_result()](../../comment/comment.module/comment_node_search_result.md) — `modules/comment/comment.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
