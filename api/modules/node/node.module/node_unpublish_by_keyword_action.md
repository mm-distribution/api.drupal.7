# node_unpublish_by_keyword_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4102–4111 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4102-L4111)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_unpublish_by_keyword_action($node, $context)
```

## Documentation

```text
Unpublishes a node containing certain keywords.

@param $node
  A node object to modify.
@param $context
  Array with the following elements:
  - 'keywords': Array of keywords. If any keyword is present in the rendered
    node, the node's status flag is set to unpublished.

@ingroup actions
```

## Code

```php
function node_unpublish_by_keyword_action($node, $context) {
  foreach ($context['keywords'] as $keyword) {
    $elements = node_view(clone $node);
    if (strpos(drupal_render($elements), $keyword) !== FALSE || strpos($node->title, $keyword) !== FALSE) {
      $node->status = NODE_NOT_PUBLISHED;
      watchdog('action', 'Set @type %title to unpublished.', array('@type' => node_type_get_name($node), '%title' => $node->title));
      break;
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
