# DeleteQuery

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 733–887 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L733-L887)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DeleteQuery extends Query implements QueryConditionInterface
```

## Documentation

```text
General class for an abstracted DELETE operation.
```

## Properties

### $table

```php
protected $table;
```

```text
The table from which to delete.

@var string
```

### $condition

```php
protected $condition;
```

```text
The condition object for this query.

Condition handling is handled via composition.

@var DatabaseCondition
```

## Methods (derived index)

- [__construct()](DeleteQuery/__construct.md) — Constructs a DeleteQuery object.
- [condition()](DeleteQuery/condition.md) — Implements QueryConditionInterface::condition().
- [isNull()](DeleteQuery/isNull.md) — Implements QueryConditionInterface::isNull().
- [isNotNull()](DeleteQuery/isNotNull.md) — Implements QueryConditionInterface::isNotNull().
- [exists()](DeleteQuery/exists.md) — Implements QueryConditionInterface::exists().
- [notExists()](DeleteQuery/notExists.md) — Implements QueryConditionInterface::notExists().
- [conditions()](DeleteQuery/conditions.md) — Implements QueryConditionInterface::conditions().
- [arguments()](DeleteQuery/arguments.md) — Implements QueryConditionInterface::arguments().
- [where()](DeleteQuery/where.md) — Implements QueryConditionInterface::where().
- [compile()](DeleteQuery/compile.md) — Implements QueryConditionInterface::compile().
- [compiled()](DeleteQuery/compiled.md) — Implements QueryConditionInterface::compiled().
- [execute()](DeleteQuery/execute.md) — Executes the DELETE query.
- [__toString()](DeleteQuery/__toString.md) — Implements PHP magic __toString method to convert the query to a string.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
