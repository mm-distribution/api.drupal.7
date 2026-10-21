# UpdateQuery

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 969–1237 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L969-L1237)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class UpdateQuery extends Query implements QueryConditionInterface
```

## Documentation

```text
General class for an abstracted UPDATE operation.
```

## Properties

### $table

```php
protected $table;
```

```text
The table to update.

@var string
```

### $fields

```php
protected $fields = array();
```

```text
An array of fields that will be updated.

@var array
```

### $arguments

```php
protected $arguments = array();
```

```text
An array of values to update to.

@var array
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

### $expressionFields

```php
protected $expressionFields = array();
```

```text
Array of fields to update to an expression in case of a duplicate record.

This variable is a nested array in the following format:
@code
<some field> => array(
 'condition' => <condition to execute, as a string>,
 'arguments' => <array of arguments for condition, or NULL for none>,
);
@endcode

@var array
```

## Methods (derived index)

- [__construct()](UpdateQuery/__construct.md) — Constructs an UpdateQuery object.
- [condition()](UpdateQuery/condition.md) — Implements QueryConditionInterface::condition().
- [isNull()](UpdateQuery/isNull.md) — Implements QueryConditionInterface::isNull().
- [isNotNull()](UpdateQuery/isNotNull.md) — Implements QueryConditionInterface::isNotNull().
- [exists()](UpdateQuery/exists.md) — Implements QueryConditionInterface::exists().
- [notExists()](UpdateQuery/notExists.md) — Implements QueryConditionInterface::notExists().
- [conditions()](UpdateQuery/conditions.md) — Implements QueryConditionInterface::conditions().
- [arguments()](UpdateQuery/arguments.md) — Implements QueryConditionInterface::arguments().
- [where()](UpdateQuery/where.md) — Implements QueryConditionInterface::where().
- [compile()](UpdateQuery/compile.md) — Implements QueryConditionInterface::compile().
- [compiled()](UpdateQuery/compiled.md) — Implements QueryConditionInterface::compiled().
- [fields()](UpdateQuery/fields.md) — Adds a set of field->value pairs to be updated.
- [expression()](UpdateQuery/expression.md) — Specifies fields to be updated as an expression.
- [execute()](UpdateQuery/execute.md) — Executes the UPDATE query.
- [__toString()](UpdateQuery/__toString.md) — Implements PHP magic __toString method to convert the query to a string.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
