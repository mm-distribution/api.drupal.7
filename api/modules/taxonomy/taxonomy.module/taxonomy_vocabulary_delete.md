# taxonomy_vocabulary_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 474–526 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L474-L526)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_delete($vid)
```

## Documentation

```text
Deletes a vocabulary.

This will update all Taxonomy fields so that they don't reference the
deleted vocabulary. It also will delete fields that have no remaining
vocabulary references. All taxonomy terms of the deleted vocabulary
will be deleted as well.

@param $vid
  A vocabulary ID.
@return
  Constant indicating items were deleted.
```

## Code

```php
function taxonomy_vocabulary_delete($vid) {
  $vocabulary = taxonomy_vocabulary_load($vid);

  $transaction = db_transaction();
  try {
    // Only load terms without a parent, child terms will get deleted too.
    $result = db_query('SELECT t.tid FROM {taxonomy_term_data} t INNER JOIN {taxonomy_term_hierarchy} th ON th.tid = t.tid WHERE t.vid = :vid AND th.parent = 0', array(':vid' => $vid))->fetchCol();
    foreach ($result as $tid) {
      taxonomy_term_delete($tid);
    }
    db_delete('taxonomy_vocabulary')
      ->condition('vid', $vid)
      ->execute();

    field_attach_delete_bundle('taxonomy_term', $vocabulary->machine_name);
    module_invoke_all('taxonomy_vocabulary_delete', $vocabulary);
    module_invoke_all('entity_delete', $vocabulary, 'taxonomy_vocabulary');

    // Load all Taxonomy module fields and delete those which use only this
    // vocabulary.
    $taxonomy_fields = field_read_fields(array('module' => 'taxonomy'));
    foreach ($taxonomy_fields as $field_name => $taxonomy_field) {
      $modified_field = FALSE;
      // Term reference fields may reference terms from more than one
      // vocabulary.
      foreach ($taxonomy_field['settings']['allowed_values'] as $key => $allowed_value) {
        if ($allowed_value['vocabulary'] == $vocabulary->machine_name) {
          unset($taxonomy_field['settings']['allowed_values'][$key]);
          $modified_field = TRUE;
        }
      }
      if ($modified_field) {
        if (empty($taxonomy_field['settings']['allowed_values'])) {
          field_delete_field($field_name);
        }
        else {
          // Update the field definition with the new allowed values.
          field_update_field($taxonomy_field);
        }
      }
    }

    cache_clear_all();
    taxonomy_vocabulary_static_reset();

    return SAVED_DELETED;
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('taxonomy', $e);
    throw $e;
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
