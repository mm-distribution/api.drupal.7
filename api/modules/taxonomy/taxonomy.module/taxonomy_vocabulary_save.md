# taxonomy_vocabulary_save()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 415–459 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L415-L459)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_save($vocabulary)
```

## Documentation

```text
Saves a vocabulary.

@param $vocabulary
  A vocabulary object with the following properties:
  - vid: (optional) The ID of the vocabulary (omit if creating a new
    vocabulary; only use to update an existing vocabulary).
  - name: The human-readable name of the vocabulary.
  - machine_name: The machine name of the vocabulary.
  - description: (optional) The vocabulary's description.
  - hierarchy: The hierarchy level of the vocabulary.
  - module: (optional) The module altering the vocabulary.
  - weight: (optional) The weight of this vocabulary in relation to other
    vocabularies.
  - original: (optional) The original vocabulary object before any changes
    are applied.
  - old_machine_name: (optional) The original machine name of the
    vocabulary.

@return
  Status constant indicating whether the vocabulary was inserted (SAVED_NEW)
  or updated (SAVED_UPDATED).
```

## Code

```php
function taxonomy_vocabulary_save($vocabulary) {
  // Prevent leading and trailing spaces in vocabulary names.
  if (!empty($vocabulary->name)) {
    $vocabulary->name = trim($vocabulary->name);
  }
  // Load the stored entity, if any.
  if (!empty($vocabulary->vid)) {
    if (!isset($vocabulary->original)) {
      $vocabulary->original = entity_load_unchanged('taxonomy_vocabulary', $vocabulary->vid);
    }
    // Make sure machine name changes are easily detected.
    // @todo: Remove in Drupal 8, as it is deprecated by directly reading from
    // $vocabulary->original.
    $vocabulary->old_machine_name = $vocabulary->original->machine_name;
  }

  if (!isset($vocabulary->module)) {
    $vocabulary->module = 'taxonomy';
  }

  module_invoke_all('taxonomy_vocabulary_presave', $vocabulary);
  module_invoke_all('entity_presave', $vocabulary, 'taxonomy_vocabulary');

  if (!empty($vocabulary->vid) && !empty($vocabulary->name)) {
    $status = drupal_write_record('taxonomy_vocabulary', $vocabulary, 'vid');
    taxonomy_vocabulary_static_reset(array($vocabulary->vid));
    if ($vocabulary->old_machine_name != $vocabulary->machine_name) {
      field_attach_rename_bundle('taxonomy_term', $vocabulary->old_machine_name, $vocabulary->machine_name);
    }
    module_invoke_all('taxonomy_vocabulary_update', $vocabulary);
    module_invoke_all('entity_update', $vocabulary, 'taxonomy_vocabulary');
  }
  elseif (empty($vocabulary->vid)) {
    $status = drupal_write_record('taxonomy_vocabulary', $vocabulary);
    taxonomy_vocabulary_static_reset();
    field_attach_create_bundle('taxonomy_term', $vocabulary->machine_name);
    module_invoke_all('taxonomy_vocabulary_insert', $vocabulary);
    module_invoke_all('entity_insert', $vocabulary, 'taxonomy_vocabulary');
  }

  unset($vocabulary->original);
  cache_clear_all();

  return $status;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
