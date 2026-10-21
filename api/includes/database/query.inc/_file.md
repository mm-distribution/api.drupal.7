# includes/database/query.inc

- **Source:** [local](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · 2011 lines

## File documentation

```text
@file
Non-specific Database query code. Used by all engines.
```

## Classes and interfaces (derived index)

- [QueryConditionInterface](QueryConditionInterface.md) — Interface for a conditional clause in a query.
- [QueryAlterableInterface](QueryAlterableInterface.md) — Interface for a query that can be manipulated via an alter hook.
- [QueryPlaceholderInterface](QueryPlaceholderInterface.md) — Interface for a query that accepts placeholders.
- [Query](Query.md) — Base class for query builders.
- [InsertQuery](InsertQuery.md) — General class for an abstracted INSERT query.
- [DeleteQuery](DeleteQuery.md) — General class for an abstracted DELETE operation.
- [TruncateQuery](TruncateQuery.md) — General class for an abstracted TRUNCATE operation.
- [UpdateQuery](UpdateQuery.md) — General class for an abstracted UPDATE operation.
- [MergeQuery](MergeQuery.md) — General class for an abstracted MERGE query operation.
- [DatabaseCondition](DatabaseCondition.md) — Generic class for a series of conditions in a query.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
