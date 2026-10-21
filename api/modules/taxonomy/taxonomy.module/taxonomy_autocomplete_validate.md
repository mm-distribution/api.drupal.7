# taxonomy_autocomplete_validate()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1757–1793 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1757-L1793)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_autocomplete_validate($element, &$form_state)
```

## Documentation

```text
Form element validate handler for taxonomy term autocomplete element.
```

## Code

```php
function taxonomy_autocomplete_validate($element, &$form_state) {
  // Autocomplete widgets do not send their tids in the form, so we must detect
  // them here and process them independently.
  $value = array();
  if ($tags = $element['#value']) {
    // Collect candidate vocabularies.
    $field = field_widget_field($element, $form_state);
    $vocabularies = array();
    foreach ($field['settings']['allowed_values'] as $tree) {
      if ($vocabulary = taxonomy_vocabulary_machine_name_load($tree['vocabulary'])) {
        $vocabularies[$vocabulary->vid] = $vocabulary;
      }
    }

    // Translate term names into actual terms.
    $typed_terms = drupal_explode_tags($tags);
    foreach ($typed_terms as $typed_term) {
      // See if the term exists in the chosen vocabulary and return the tid;
      // otherwise, create a new 'autocreate' term for insert/update.
      if ($possibilities = taxonomy_term_load_multiple(array(), array('name' => trim($typed_term), 'vid' => array_keys($vocabularies)))) {
        $term = array_pop($possibilities);
      }
      else {
        $vocabulary = reset($vocabularies);
        $term = array(
          'tid' => 'autocreate',
          'vid' => $vocabulary->vid,
          'name' => $typed_term,
          'vocabulary_machine_name' => $vocabulary->machine_name,
        );
      }
      $value[] = (array)$term;
    }
  }

  form_set_value($element, $value, $form_state);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
