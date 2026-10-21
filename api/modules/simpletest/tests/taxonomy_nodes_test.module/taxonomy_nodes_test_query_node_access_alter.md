# taxonomy_nodes_test_query_node_access_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_nodes_test.module`](_file.md), lines 11–26 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_nodes_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_nodes_test.module#L11-L26)
- **Module/theme:** batch_test
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function taxonomy_nodes_test_query_node_access_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_TAG_alter().
```

## Code

```php
function taxonomy_nodes_test_query_node_access_alter(QueryAlterableInterface $query) {
  if (variable_get('taxonomy_nodes_test_query_node_access_alter', FALSE)) {
    $taxonomy_index = FALSE;
    foreach ($query->getTables() as $alias => $table) {
      if ($table['table'] == 'taxonomy_index') {
        $taxonomy_index = TRUE;
      }
    }

    if ($taxonomy_index) {
      // Verify that additional data can be added to the default
      // taxonomy_select_nodes() query by altering it.
      $query->leftJoin('taxonomy_term_data', 'ttd', 'ttd.tid = t.tid');
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_nodes_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_nodes_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
