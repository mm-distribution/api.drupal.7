# taxonomy_term_save()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 628–698 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L628-L698)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_save($term)
```

## Documentation

```text
Saves a term object to the database.

@param $term
  The taxonomy term object with the following properties:
  - vid: The ID of the vocabulary the term is assigned to.
  - name: The name of the term.
  - tid: (optional) The unique ID for the term being saved. If $term->tid is
    empty or omitted, a new term will be inserted.
  - description: (optional) The term's description.
  - format: (optional) The text format for the term's description.
  - weight: (optional) The weight of this term in relation to other terms
    within the same vocabulary.
  - parent: (optional) The parent term(s) for this term. This can be a single
    term ID or an array of term IDs. A value of 0 means this term does not
    have any parents. When omitting this variable during an update, the
    existing hierarchy for the term remains unchanged.
  - vocabulary_machine_name: (optional) The machine name of the vocabulary
    the term is assigned to. If not given, this value will be set
    automatically by loading the vocabulary based on $term->vid.
  - original: (optional) The original taxonomy term object before any changes
    were applied. When omitted, the unchanged taxonomy term object is
    loaded from the database and stored in this property.
  Since a taxonomy term is an entity, any fields contained in the term object
  are saved alongside the term object.

@return
  Status constant indicating whether term was inserted (SAVED_NEW) or updated
  (SAVED_UPDATED). When inserting a new term, $term->tid will contain the
  term ID of the newly created term.
```

## Code

```php
function taxonomy_term_save($term) {
  // Prevent leading and trailing spaces in term names.
  $term->name = trim($term->name);
  if (!isset($term->vocabulary_machine_name)) {
    $vocabulary = taxonomy_vocabulary_load($term->vid);
    $term->vocabulary_machine_name = $vocabulary->machine_name;
  }

  // Load the stored entity, if any.
  if (!empty($term->tid) && !isset($term->original)) {
    $term->original = entity_load_unchanged('taxonomy_term', $term->tid);
  }

  field_attach_presave('taxonomy_term', $term);
  module_invoke_all('taxonomy_term_presave', $term);
  module_invoke_all('entity_presave', $term, 'taxonomy_term');

  if (empty($term->tid)) {
    $op = 'insert';
    $status = drupal_write_record('taxonomy_term_data', $term);
    field_attach_insert('taxonomy_term', $term);
    if (!isset($term->parent)) {
      $term->parent = array(0);
    }
  }
  else {
    $op = 'update';
    $status = drupal_write_record('taxonomy_term_data', $term, 'tid');
    field_attach_update('taxonomy_term', $term);
    if (isset($term->parent)) {
      db_delete('taxonomy_term_hierarchy')
        ->condition('tid', $term->tid)
        ->execute();
    }
  }

  if (isset($term->parent)) {
    if (!is_array($term->parent)) {
      $term->parent = array($term->parent);
    }
    $query = db_insert('taxonomy_term_hierarchy')
      ->fields(array('tid', 'parent'));
    foreach ($term->parent as $parent) {
      if (is_array($parent)) {
        foreach ($parent as $tid) {
          $query->values(array(
            'tid' => $term->tid,
            'parent' => $tid
          ));
        }
      }
      else {
        $query->values(array(
          'tid' => $term->tid,
          'parent' => $parent
        ));
      }
    }
    $query->execute();
  }

  // Reset the taxonomy term static variables.
  taxonomy_terms_static_reset();

  // Invoke the taxonomy hooks.
  module_invoke_all("taxonomy_term_$op", $term);
  module_invoke_all("entity_$op", $term, 'taxonomy_term');
  unset($term->original);

  return $status;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
