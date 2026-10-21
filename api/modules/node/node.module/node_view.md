# node_view()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1330–1362 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1330-L1362)
- **Module/theme:** node

## Signature

```php
function node_view($node, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Generates an array for rendering the given node.

@param $node
  A node object.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.

@return
  An array as expected by drupal_render().
```

## Code

```php
function node_view($node, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Populate $node->content with a render() array.
  node_build_content($node, $view_mode, $langcode);

  $build = $node->content;
  // We don't need duplicate rendering info in node->content.
  unset($node->content);

  $build += array(
    '#theme' => 'node',
    '#node' => $node,
    '#view_mode' => $view_mode,
    '#language' => $langcode,
  );

  // Add contextual links for this node, except when the node is already being
  // displayed on its own page. Modules may alter this behavior (for example,
  // to restrict contextual links to certain view modes) by implementing
  // hook_node_view_alter().
  if (!empty($node->nid) && !($view_mode == 'full' && node_is_page($node))) {
    $build['#contextual_links']['node'] = array('node', array($node->nid));
  }

  // Allow modules to modify the structured node.
  $type = 'node';
  drupal_alter(array('node_view', 'entity_view'), $build, $type);

  return $build;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
