# hook_entity_query_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 403–405 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L403-L405)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_query_alter($query)
```

## Documentation

```text
Alter or execute an EntityFieldQuery.

@param EntityFieldQuery $query
  An EntityFieldQuery. One of the most important properties to be changed is
  EntityFieldQuery::executeCallback. If this is set to an existing function,
  this function will get the query as its single argument and its result
  will be the returned as the result of EntityFieldQuery::execute(). This can
  be used to change the behavior of EntityFieldQuery entirely. For example,
  the default implementation can only deal with one field storage engine, but
  it is possible to write a module that can query across field storage
  engines. Also, the default implementation presumes entities are stored in
  SQL, but the execute callback could instead query any other entity storage,
  local or remote.

  Note the $query->altered attribute which is TRUE in case the query has
  already been altered once. This happens with cloned queries.
  If there is a pager, then such a cloned query will be executed to count
  all elements. This query can be detected by checking for
  ($query->pager && $query->count), allowing the driver to return 0 from
  the count query and disable the pager.
```

## Code

```php
function hook_entity_query_alter($query) {
  $query->executeCallback = 'my_module_query_callback';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_query_alter()".

- [field_test_entity_query_alter()](../../field/tests/field_test.module/field_test_entity_query_alter.md) — `modules/field/tests/field_test.module`
- [taxonomy_entity_query_alter()](../../taxonomy/taxonomy.module/taxonomy_entity_query_alter.md) — `modules/taxonomy/taxonomy.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
