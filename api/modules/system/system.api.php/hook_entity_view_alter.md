# hook_entity_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 459–467 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L459-L467)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_view_alter(&$build, $type)
```

## Documentation

```text
Alter the results of ENTITY_view().

This hook is called after the content has been assembled in a structured
array and may be used for doing processing which requires that the complete
entity content structure has been built.

If a module wishes to act on the rendered HTML of the entity rather than the
structured content array, it may use this hook to add a #post_render
callback. Alternatively, it could also implement hook_preprocess_ENTITY().
See drupal_render() and theme() for details.

@param $build
  A renderable array representing the entity content.
@param $type
  The type of entity being rendered (i.e. node, user, comment).

@see hook_entity_view()
@see hook_comment_view_alter()
@see hook_node_view_alter()
@see hook_taxonomy_term_view_alter()
@see hook_user_view_alter()
```

## Code

```php
function hook_entity_view_alter(&$build, $type) {
  if ($build['#view_mode'] == 'full' && isset($build['an_additional_field'])) {
    // Change its weight.
    $build['an_additional_field']['#weight'] = -10;

    // Add a #post_render callback to act on the rendered HTML of the entity.
    $build['#post_render'][] = 'my_module_node_post_render';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_view_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
