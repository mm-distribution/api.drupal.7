# hook_node_prepare()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 645–649 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L645-L649)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_prepare($node)
```

## Documentation

```text
Act on a node object about to be shown on the add/edit form.

This hook is invoked from node_object_prepare() after the type-specific
hook_prepare() is invoked.

@param $node
  The node that is about to be shown on the add/edit form.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_prepare($node) {
  if (!isset($node->comment)) {
    $node->comment = variable_get("comment_$node->type", COMMENT_NODE_OPEN);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_prepare()".

- [book_node_prepare()](../../book/book.module/book_node_prepare.md) — `modules/book/book.module`
- [comment_node_prepare()](../../comment/comment.module/comment_node_prepare.md) — `modules/comment/comment.module`
- [menu_node_prepare()](../../menu/menu.module/menu_node_prepare.md) — `modules/menu/menu.module`
- [translation_node_prepare()](../../translation/translation.module/translation_node_prepare.md) — `modules/translation/translation.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
