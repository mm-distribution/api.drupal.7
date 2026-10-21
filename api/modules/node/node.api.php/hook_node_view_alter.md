# hook_node_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 862–870 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L862-L870)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_view_alter(&$build)
```

## Documentation

```text
Alter the results of node_view().

This hook is called after the content has been assembled in a structured
array and may be used for doing processing which requires that the complete
node content structure has been built.

If the module wishes to act on the rendered HTML of the node rather than the
structured content array, it may use this hook to add a #post_render
callback.  Alternatively, it could also implement hook_preprocess_node(). See
drupal_render() and theme() documentation respectively for details.

@param $build
  A renderable array representing the node content.

@see node_view()
@see hook_entity_view_alter()

@ingroup node_api_hooks
```

## Code

```php
function hook_node_view_alter(&$build) {
  if ($build['#view_mode'] == 'full' && isset($build['an_additional_field'])) {
    // Change its weight.
    $build['an_additional_field']['#weight'] = -10;
  }

  // Add a #post_render callback to act on the rendered HTML of the node.
  $build['#post_render'][] = 'my_module_node_post_render';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_view_alter()".

_None found._

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
