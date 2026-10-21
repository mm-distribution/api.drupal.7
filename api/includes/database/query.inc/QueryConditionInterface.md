# QueryConditionInterface

- **Type:** Interface
- **File:** [`includes/database/query.inc`](_file.md), lines 16–160 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L16-L160)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
interface QueryConditionInterface
```

## Documentation

```text
Interface for a conditional clause in a query.
```

## Methods (derived index)

- [condition()](QueryConditionInterface/condition.md) — Helper function: builds the most common conditional clauses.
- [where()](QueryConditionInterface/where.md) — Adds an arbitrary WHERE clause to the query.
- [isNull()](QueryConditionInterface/isNull.md) — Sets a condition that the specified field be NULL.
- [isNotNull()](QueryConditionInterface/isNotNull.md) — Sets a condition that the specified field be NOT NULL.
- [exists()](QueryConditionInterface/exists.md) — Sets a condition that the specified subquery returns values.
- [notExists()](QueryConditionInterface/notExists.md) — Sets a condition that the specified subquery returns no values.
- [conditions()](QueryConditionInterface/conditions.md) — Gets a complete list of all conditions in this conditional clause.
- [arguments()](QueryConditionInterface/arguments.md) — Gets a complete list of all values to insert into the prepared statement.
- [compile()](QueryConditionInterface/compile.md) — Compiles the saved conditions for later retrieval.
- [compiled()](QueryConditionInterface/compiled.md) — Check whether a condition has been previously compiled.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
