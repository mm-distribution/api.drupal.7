# taxonomy_form_term_submit_build_taxonomy_term()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 856–865 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L856-L865)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_form_term_submit_build_taxonomy_term($form, &$form_state)
```

## Documentation

```text
Updates the form state's term entity by processing this submission's values.
```

## Code

```php
function taxonomy_form_term_submit_build_taxonomy_term($form, &$form_state) {
  $term = $form_state['term'];
  entity_form_submit_build_entity('taxonomy_term', $term, $form, $form_state);

  // Convert text_format field into values expected by taxonomy_term_save().
  $description = $form_state['values']['description'];
  $term->description = $description['value'];
  $term->format = $description['format'];
  return $term;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
