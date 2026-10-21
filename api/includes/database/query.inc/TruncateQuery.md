# TruncateQuery

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 893–964 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L893-L964)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class TruncateQuery extends Query
```

## Documentation

```text
General class for an abstracted TRUNCATE operation.
```

## Properties

### $table

```php
protected $table;
```

```text
The table to truncate.

@var string
```

## Methods (derived index)

- [__construct()](TruncateQuery/__construct.md) — Constructs a TruncateQuery object.
- [compile()](TruncateQuery/compile.md) — Implements QueryConditionInterface::compile().
- [compiled()](TruncateQuery/compiled.md) — Implements QueryConditionInterface::compiled().
- [execute()](TruncateQuery/execute.md) — Executes the TRUNCATE query.
- [__toString()](TruncateQuery/__toString.md) — Implements PHP magic __toString method to convert the query to a string.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
