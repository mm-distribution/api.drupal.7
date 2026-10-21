# hook_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1314–1329 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1314-L1329)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_view($node, $view_mode, $langcode = NULL)
```

## Documentation

```text
Display a node.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_view() to respond to node view of all node types.

This hook is invoked during node viewing after the node is fully loaded, so
that the node type module can define a custom method for display, or add to
the default display.

@param $node
  The node to be displayed, as returned by node_load().
@param $view_mode
  View mode, e.g. 'full', 'teaser', ...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.

@return
  The passed $node parameter should be modified as necessary and returned so
  it can be properly presented. Nodes are prepared for display by assembling
  a structured array, formatted as in the Form API, in $node->content. As
  with Form API arrays, the #weight property can be used to control the
  relative positions of added elements. After this hook is invoked,
  node_view() calls field_attach_view() to add field views to $node->content,
  and then invokes hook_node_view() and hook_node_view_alter(), so if you
  want to affect the final view of the node, you might consider implementing
  one of these hooks instead.

@ingroup node_api_hooks
```

## Code

```php
function hook_view($node, $view_mode, $langcode = NULL) {
  if ($view_mode == 'full' && node_is_page($node)) {
    $breadcrumb = array();
    $breadcrumb[] = l(t('Home'), NULL);
    $breadcrumb[] = l(t('Example'), 'example');
    $breadcrumb[] = l($node->field1, 'example/' . $node->field1);
    drupal_set_breadcrumb($breadcrumb);
  }

  $node->content['myfield'] = array(
    '#markup' => theme('mymodule_myfield', $node->myfield),
    '#weight' => 1,
  );

  return $node;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_view()".

- [blog_view()](../../blog/blog.module/blog_view.md) — `modules/blog/blog.module`
- [poll_view()](../../poll/poll.module/poll_view.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
