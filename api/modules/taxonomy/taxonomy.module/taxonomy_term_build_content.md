# taxonomy_term_build_content()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 824–864 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L824-L864)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_build_content($term, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Builds a structured array representing the term's content.

The content built for the taxonomy term (field values, file attachments or
other term components) will vary depending on the $view_mode parameter.

Drupal core defines the following view modes for terms, with the following
default use cases:
  - full (default): term is displayed on its own page (taxonomy/term/123)
Contributed modules might define additional view modes, or use existing
view modes in additional contexts.

@param $term
  A taxonomy term object.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.
```

## Code

```php
function taxonomy_term_build_content($term, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Remove previously built content, if exists.
  $term->content = array();

  // Allow modules to change the view mode.
  $view_mode = key(entity_view_mode_prepare('taxonomy_term', array($term->tid => $term), $view_mode, $langcode));

  // Add the term description if the term has one and it is visible.
  $type = 'taxonomy_term';
  $entity_ids = entity_extract_ids($type, $term);
  $settings = field_view_mode_settings($type, $entity_ids[2]);
  $fields = field_extra_fields_get_display($type, $entity_ids[2], $view_mode);
  if (!empty($term->description) && isset($fields['description']) && $fields['description']['visible']) {
    $term->content['description'] = array(
      '#markup' => check_markup($term->description, $term->format, '', TRUE),
      '#weight' => $fields['description']['weight'],
      '#prefix' => '<div class="taxonomy-term-description">',
      '#suffix' => '</div>',
    );
  }

  // Build fields content.
  // In case of a multiple view, taxonomy_term_view_multiple() already ran the
  // 'prepare_view' step. An internal flag prevents the operation from running
  // twice.
  field_attach_prepare_view('taxonomy_term', array($term->tid => $term), $view_mode, $langcode);
  entity_prepare_view('taxonomy_term', array($term->tid => $term), $langcode);
  $term->content += field_attach_view('taxonomy_term', $term, $view_mode, $langcode);

  // Allow modules to make their own additions to the taxonomy term.
  module_invoke_all('taxonomy_term_view', $term, $view_mode, $langcode);
  module_invoke_all('entity_view', $term, 'taxonomy_term', $view_mode, $langcode);

  // Make sure the current view mode is stored if no module has already
  // populated the related key.
  $term->content += array('#view_mode' => $view_mode);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
