# hook_comment_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 96–105 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L96-L105)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_view_alter(&$build)
```

## Documentation

```text
The comment was built; the module may modify the structured content.

This hook is called after the content has been assembled in a structured array
and may be used for doing processing which requires that the complete comment
content structure has been built.

If the module wishes to act on the rendered HTML of the comment rather than the
structured content array, it may use this hook to add a #post_render callback.
Alternatively, it could also implement hook_preprocess_comment(). See
drupal_render() and theme() documentation respectively for details.

@param $build
  A renderable array representing the comment.

@see comment_view()
@see hook_entity_view_alter()
```

## Code

```php
function hook_comment_view_alter(&$build) {
  // Check for the existence of a field added by another module.
  if ($build['#view_mode'] == 'full' && isset($build['an_additional_field'])) {
    // Change its weight.
    $build['an_additional_field']['#weight'] = -10;
  }

  // Add a #post_render callback to act on the rendered HTML of the comment.
  $build['#post_render'][] = 'my_module_comment_post_render';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_view_alter()".

_None found._

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
