# hook_taxonomy_term_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 193–199 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L193-L199)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_view($term, $view_mode, $langcode)
```

## Documentation

```text
Act on a taxonomy term that is being assembled before rendering.

The module may add elements to $term->content prior to rendering. The
structure of $term->content is a renderable array as expected by
drupal_render().

@param $term
  The term that is being assembled for rendering.
@param $view_mode
  The $view_mode parameter from taxonomy_term_view().
@param $langcode
  The language code used for rendering.

@see hook_entity_view()
```

## Code

```php
function hook_taxonomy_term_view($term, $view_mode, $langcode) {
  $term->content['my_additional_field'] = array(
    '#markup' => $additional_field,
    '#weight' => 10,
    '#theme' => 'mymodule_my_additional_field',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_view()".

- [taxonomy_test_taxonomy_term_view()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_taxonomy_term_view.md) — `modules/simpletest/tests/taxonomy_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
