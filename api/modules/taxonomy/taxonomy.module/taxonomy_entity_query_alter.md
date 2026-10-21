# taxonomy_entity_query_alter()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 2042–2063 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L2042-L2063)
- **Module/theme:** taxonomy
- **Implements:** [hook_entity_query_alter()](../../system/system.api.php/hook_entity_query_alter.md)

## Signature

```php
function taxonomy_entity_query_alter($query)
```

## Documentation

```text
Implements hook_entity_query_alter().

Converts EntityFieldQuery instances on taxonomy terms that have an entity
condition on term bundles (vocabulary machine names). Since the vocabulary
machine name is not present in the {taxonomy_term_data} table itself, we have
to convert the bundle condition into a property condition of vocabulary IDs
to match against {taxonomy_term_data}.vid.
```

## Code

```php
function taxonomy_entity_query_alter($query) {
  $conditions = &$query->entityConditions;

  // Alter only taxonomy term queries with bundle conditions.
  if (isset($conditions['entity_type']) && $conditions['entity_type']['value'] == 'taxonomy_term' && isset($conditions['bundle'])) {
    // Convert vocabulary machine names to vocabulary IDs.
    $vocabulary_data = taxonomy_vocabulary_get_names();
    $vids = array();
    if (is_array($conditions['bundle']['value'])) {
      foreach ($conditions['bundle']['value'] as $vocabulary_machine_name) {
        $vids[] = $vocabulary_data[$vocabulary_machine_name]->vid;
      }
    }
    else {
      $vocabulary_machine_name = $conditions['bundle']['value'];
      $vids = $vocabulary_data[$vocabulary_machine_name]->vid;
    }

    $query->propertyCondition('vid', $vids, $conditions['bundle']['operator']);
    unset($conditions['bundle']);
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
