# hook_taxonomy_term_view_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 219–227 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L219-L227)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_view_alter(&$build)
```

## Documentation

```text
Alter the results of taxonomy_term_view().

This hook is called after the content has been assembled in a structured
array and may be used for doing processing which requires that the complete
taxonomy term content structure has been built.

If the module wishes to act on the rendered HTML of the term rather than the
structured content array, it may use this hook to add a #post_render
callback. Alternatively, it could also implement
hook_preprocess_taxonomy_term(). See drupal_render() and theme()
documentation respectively for details.

@param $build
  A renderable array representing the term.

@see hook_entity_view_alter()
```

## Code

```php
function hook_taxonomy_term_view_alter(&$build) {
  if ($build['#view_mode'] == 'full' && isset($build['an_additional_field'])) {
    // Change its weight.
    $build['an_additional_field']['#weight'] = -10;
  }

  // Add a #post_render callback to act on the rendered HTML of the term.
  $build['#post_render'][] = 'my_module_node_post_render';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_view_alter()".

_None found._

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
