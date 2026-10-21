# database_test_query_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 6–32 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L6-L32)
- **Module/theme:** batch_test
- **Implements:** [hook_query_alter()](../../../system/system.api.php/hook_query_alter.md)

## Signature

```php
function database_test_query_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_alter().
```

## Code

```php
function database_test_query_alter(QueryAlterableInterface $query) {

  if ($query->hasTag('database_test_alter_add_range')) {
    $query->range(0, 2);
  }

  if ($query->hasTag('database_test_alter_add_join')) {
    $people_alias = $query->join('test', 'people', "test_task.pid = %alias.id");
    $name_field = $query->addField($people_alias, 'name', 'name');
    $query->condition($people_alias . '.id', 2);
  }

  if ($query->hasTag('database_test_alter_change_conditional')) {
    $conditions =& $query->conditions();
    $conditions[0]['value'] = 2;
  }

  if ($query->hasTag('database_test_alter_change_fields')) {
    $fields =& $query->getFields();
    unset($fields['age']);
  }

  if ($query->hasTag('database_test_alter_change_expressions')) {
    $expressions =& $query->getExpressions();
    $expressions['double_age']['expression'] = 'age*3';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
