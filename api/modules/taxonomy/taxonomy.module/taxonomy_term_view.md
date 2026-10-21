# taxonomy_term_view()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 880–906 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L880-L906)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_view($term, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Generate an array for rendering the given term.

@param $term
  A term object.
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
function taxonomy_term_view($term, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Populate $term->content with a render() array.
  taxonomy_term_build_content($term, $view_mode, $langcode);
  $build = $term->content;

  // We don't need duplicate rendering info in $term->content.
  unset($term->content);

  $build += array(
    '#theme' => 'taxonomy_term',
    '#term' => $term,
    '#view_mode' => $view_mode,
    '#language' => $langcode,
  );

  $build['#attached']['css'][] = drupal_get_path('module', 'taxonomy') . '/taxonomy.css';

  // Allow modules to modify the structured taxonomy term.
  $type = 'taxonomy_term';
  drupal_alter(array('taxonomy_term_view', 'entity_view'), $build, $type);

  return $build;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
