# hook_node_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 834–840 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L834-L840)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_view($node, $view_mode, $langcode)
```

## Documentation

```text
Act on a node that is being assembled before rendering.

The module may add elements to $node->content prior to rendering. This hook
will be called after hook_view(). The structure of $node->content is a
renderable array as expected by drupal_render().

When $view_mode is 'rss', modules can also add extra RSS elements and
namespaces to $node->rss_elements and $node->rss_namespaces respectively for
the RSS item generated for this node.
For details on how this is used, see node_feed().

@see blog_node_view()
@see forum_node_view()
@see comment_node_view()

@param $node
  The node that is being assembled for rendering.
@param $view_mode
  The $view_mode parameter from node_view().
@param $langcode
  The language code used for rendering.

@see hook_entity_view()

@ingroup node_api_hooks
```

## Code

```php
function hook_node_view($node, $view_mode, $langcode) {
  $node->content['my_additional_field'] = array(
    '#markup' => $additional_field,
    '#weight' => 10,
    '#theme' => 'mymodule_my_additional_field',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_view()".

- [blog_node_view()](../../blog/blog.module/blog_node_view.md) — `modules/blog/blog.module`
- [book_node_view()](../../book/book.module/book_node_view.md) — `modules/book/book.module`
- [comment_node_view()](../../comment/comment.module/comment_node_view.md) — `modules/comment/comment.module`
- [forum_node_view()](../../forum/forum.module/forum_node_view.md) — `modules/forum/forum.module`
- [node_test_node_view()](../tests/node_test.module/node_test_node_view.md) — `modules/node/tests/node_test.module`
- [statistics_node_view()](../../statistics/statistics.module/statistics_node_view.md) — `modules/statistics/statistics.module`
- [translation_node_view()](../../translation/translation.module/translation_node_view.md) — `modules/translation/translation.module`
- [trigger_node_view()](../../trigger/trigger.module/trigger_node_view.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
