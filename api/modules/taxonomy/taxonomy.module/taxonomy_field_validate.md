# taxonomy_field_validate()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1512–1558 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1512-L1558)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_validate()](../../field/field.api.php/hook_field_validate.md)

## Signature

```php
function taxonomy_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Implements hook_field_validate().

Taxonomy field settings allow for either a single vocabulary ID, multiple
vocabulary IDs, or sub-trees of a vocabulary to be specified as allowed
values, although only the first of these is supported via the field UI.
Confirm that terms entered as values meet at least one of these conditions.

Possible error codes:
- 'taxonomy_term_illegal_value': The value is not part of the list of allowed values.
```

## Code

```php
function taxonomy_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  // Build an array of existing term IDs so they can be loaded with
  // taxonomy_term_load_multiple();
  foreach ($items as $delta => $item) {
    if (!empty($item['tid']) && $item['tid'] !== 'autocreate') {
      $tids[] = $item['tid'];
    }
  }
  if (!empty($tids)) {
    $terms = taxonomy_term_load_multiple($tids);

    // Check each existing item to ensure it can be found in the
    // allowed values for this field.
    foreach ($items as $delta => $item) {
      $validate = TRUE;
      if (!empty($item['tid']) && $item['tid'] !== 'autocreate') {
        $validate = FALSE;
        foreach ($field['settings']['allowed_values'] as $settings) {
          // If no parent is specified, check if the term is in the vocabulary.
          if (isset($settings['vocabulary']) && empty($settings['parent'])) {
            if ($settings['vocabulary'] == $terms[$item['tid']]->vocabulary_machine_name) {
              $validate = TRUE;
              break;
            }
          }
          // If a parent is specified, then to validate it must appear in the
          // array returned by taxonomy_get_parents_all().
          elseif (!empty($settings['parent'])) {
            $ancestors = taxonomy_get_parents_all($item['tid']);
            foreach ($ancestors as $ancestor) {
              if ($ancestor->tid == $settings['parent']) {
                $validate = TRUE;
                break 2;
              }
            }
          }
        }
      }
      if (!$validate) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'taxonomy_term_reference_illegal_value',
          'message' => t('%name: illegal value.', array('%name' => $instance['label'])),
        );
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
