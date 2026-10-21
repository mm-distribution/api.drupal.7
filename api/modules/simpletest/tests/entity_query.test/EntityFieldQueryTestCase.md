# EntityFieldQueryTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/entity_query.test`](_file.md), lines 12–1685 · [local source](../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L12-L1685)
- **Module/theme:** batch_test

## Signature

```php
class EntityFieldQueryTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests EntityFieldQuery.
```

## Properties

### $fields

```php
protected $fields;
```

### $field_names

```php
protected $field_names;
```

### $instances

```php
protected $instances;
```

## Methods (derived index)

- [getInfo()](EntityFieldQueryTestCase/getInfo.md)
- [setUp()](EntityFieldQueryTestCase/setUp.md)
- [testEntityFieldQuery()](EntityFieldQueryTestCase/testEntityFieldQuery.md) — Tests EntityFieldQuery.
- [testEntityFieldQueryTranslatable()](EntityFieldQueryTestCase/testEntityFieldQueryTranslatable.md) — Tests querying translatable fields.
- [testEntityFieldQueryMetaConditions()](EntityFieldQueryTestCase/testEntityFieldQueryMetaConditions.md) — Tests field meta conditions.
- [testEntityFieldQueryRouting()](EntityFieldQueryTestCase/testEntityFieldQueryRouting.md) — Tests the routing feature of EntityFieldQuery.
- [testEntityFieldQueryPager()](EntityFieldQueryTestCase/testEntityFieldQueryPager.md) — Tests the pager integration of EntityFieldQuery.
- [testEntityFieldQueryDisablePager()](EntityFieldQueryTestCase/testEntityFieldQueryDisablePager.md) — Tests disabling the pager in EntityFieldQuery.
- [testEntityFieldQueryTableSort()](EntityFieldQueryTestCase/testEntityFieldQueryTableSort.md) — Tests the TableSort integration of EntityFieldQuery.
- [testEntityFieldQueryAccess()](EntityFieldQueryTestCase/testEntityFieldQueryAccess.md) — Tests EntityFieldQuery access on non-node entities.
- [assertEntityFieldQuery()](EntityFieldQueryTestCase/assertEntityFieldQuery.md) — Fetches the results of an EntityFieldQuery and compares.
- [testTablePrefixing()](EntityFieldQueryTestCase/testTablePrefixing.md) — Tests EFQ table prefixing with multiple conditions and an altered join.

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
