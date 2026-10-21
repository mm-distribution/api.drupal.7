# comment_node_prepare()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1302–1306 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1302-L1306)
- **Module/theme:** comment
- **Implements:** [hook_node_prepare()](../../node/node.api.php/hook_node_prepare.md)

## Signature

```php
function comment_node_prepare($node)
```

## Documentation

```text
Implements hook_node_prepare().
```

## Code

```php
function comment_node_prepare($node) {
  if (!isset($node->comment)) {
    $node->comment = variable_get("comment_$node->type", COMMENT_NODE_OPEN);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
