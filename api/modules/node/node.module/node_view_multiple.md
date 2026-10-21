# node_view_multiple()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2661–2683 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2661-L2683)
- **Module/theme:** node

## Signature

```php
function node_view_multiple($nodes, $view_mode = 'teaser', $weight = 0, $langcode = NULL)
```

## Documentation

```text
Constructs a drupal_render() style array from an array of loaded nodes.

@param $nodes
  An array of nodes as returned by node_load_multiple().
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $weight
  An integer representing the weight of the first node in the list.
@param $langcode
  (optional) A language code to use for rendering. Defaults to NULL which is
  the global content language of the current request.

@return
  An array in the format expected by drupal_render().
```

## Code

```php
function node_view_multiple($nodes, $view_mode = 'teaser', $weight = 0, $langcode = NULL) {
  $build = array('nodes' => array());
  $entities_by_view_mode = entity_view_mode_prepare('node', $nodes, $view_mode, $langcode);
  foreach ($entities_by_view_mode as $entity_view_mode => $entities) {
    field_attach_prepare_view('node', $entities, $entity_view_mode, $langcode);
    entity_prepare_view('node', $entities, $langcode);

    foreach ($entities as $entity) {
      $build['nodes'][$entity->nid] = node_view($entity, $entity_view_mode, $langcode);
    }
  }

  foreach ($nodes as $node) {
    $build['nodes'][$node->nid]['#weight'] = $weight;
    $weight++;
  }
  // Sort here, to preserve the input order of the entities that were passed to
  // this function.
  uasort($build['nodes'], 'element_sort');
  $build['nodes']['#sorted'] = TRUE;

  return $build;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
