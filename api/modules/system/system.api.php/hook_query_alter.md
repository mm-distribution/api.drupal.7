# hook_query_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3318–3322 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3318-L3322)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_query_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Perform alterations to a structured query.

Structured (aka dynamic) queries that have tags associated may be altered by any module
before the query is executed.

@param $query
  A Query object describing the composite parts of a SQL query.

@see hook_query_TAG_alter()
@see node_query_node_access_alter()
@see QueryAlterableInterface
@see SelectQueryInterface
```

## Code

```php
function hook_query_alter(QueryAlterableInterface $query) {
  if ($query->hasTag('micro_limit')) {
    $query->range(0, 2);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_query_alter()".

- [database_test_query_alter()](../../simpletest/tests/database_test.module/database_test_query_alter.md) — `modules/simpletest/tests/database_test.module`
- [taxonomy_test_query_alter()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_query_alter.md) — `modules/simpletest/tests/taxonomy_test.module`
- [search_node_tags_query_alter()](../../search/tests/search_node_tags.module/search_node_tags_query_alter.md) — `modules/search/tests/search_node_tags.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
