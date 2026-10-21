# taxonomy_term_view_multiple()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 780–802 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L780-L802)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_view_multiple($terms, $view_mode = 'teaser', $weight = 0, $langcode = NULL)
```

## Documentation

```text
Constructs a drupal_render() style array from an array of loaded terms.

@param $terms
  An array of taxonomy terms as returned by taxonomy_term_load_multiple().
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $weight
  An integer representing the weight of the first taxonomy term in the list.
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.

@return
  An array in the format expected by drupal_render().
```

## Code

```php
function taxonomy_term_view_multiple($terms, $view_mode = 'teaser', $weight = 0, $langcode = NULL) {
  $build = array();
  $entities_by_view_mode = entity_view_mode_prepare('taxonomy_term', $terms, $view_mode, $langcode);
  foreach ($entities_by_view_mode as $entity_view_mode => $entities) {
    field_attach_prepare_view('taxonomy_term', $entities, $entity_view_mode, $langcode);
    entity_prepare_view('taxonomy_term', $entities, $langcode);

    foreach ($entities as $entity) {
      $build['taxonomy_terms'][$entity->tid] = taxonomy_term_view($entity, $entity_view_mode, $langcode);
    }
  }

  foreach ($terms as $term) {
    $build['taxonomy_terms'][$term->tid]['#weight'] = $weight;
    $weight++;
  }
  // Sort here, to preserve the input order of the entities that were passed to
  // this function.
  uasort($build['taxonomy_terms'], 'element_sort');
  $build['taxonomy_terms']['#sorted'] = TRUE;

  return $build;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
