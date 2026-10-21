# hook_user_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 385–394 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L385-L394)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_view_alter(&$build)
```

## Documentation

```text
The user was built; the module may modify the structured content.

This hook is called after the content has been assembled in a structured array
and may be used for doing processing which requires that the complete user
content structure has been built.

If the module wishes to act on the rendered HTML of the user rather than the
structured content array, it may use this hook to add a #post_render callback.
Alternatively, it could also implement hook_preprocess_user_profile(). See
drupal_render() and theme() documentation respectively for details.

@param $build
  A renderable array representing the user.

@see user_view()
@see hook_entity_view_alter()
```

## Code

```php
function hook_user_view_alter(&$build) {
  // Check for the existence of a field added by another module.
  if (isset($build['an_additional_field'])) {
    // Change its weight.
    $build['an_additional_field']['#weight'] = -10;
  }

  // Add a #post_render callback to act on the rendered HTML of the user.
  $build['#post_render'][] = 'my_module_user_post_render';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_view_alter()".

_None found._

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
