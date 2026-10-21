# entity_query_access_test_sample_query()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_query_access_test.module`](_file.md), lines 26–54 · [local source](../../../../../source/modules/simpletest/tests/entity_query_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query_access_test.module#L26-L54)
- **Module/theme:** batch_test

## Signature

```php
function entity_query_access_test_sample_query($field_name)
```

## Documentation

```text
Returns the results from an example EntityFieldQuery.
```

## Code

```php
function entity_query_access_test_sample_query($field_name) {
  global $user;

  // Simulate user does not have access to view all nodes.
  $access = &drupal_static('node_access_view_all_nodes');
  $access[$user->uid] = FALSE;

  $query = new EntityFieldQuery();
  $query
    ->entityCondition('entity_type', 'test_entity_bundle_key')
    ->fieldCondition($field_name, 'value', 0, '>')
    ->entityOrderBy('entity_id', 'ASC');
  $results = array(
    'items' => array(),
    'title' => t('EntityFieldQuery results'),
  );
  foreach ($query->execute() as $entity_type => $entity_ids) {
    foreach ($entity_ids as $entity_id => $entity_stub) {
      $results['items'][] = format_string('Found entity of type @entity_type with id @entity_id', array('@entity_type' => $entity_type, '@entity_id' => $entity_id));
    }
  }
  if (count($results['items']) > 0) {
    $output = theme('item_list', $results);
  }
  else {
    $output = 'No results found with EntityFieldQuery.';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
