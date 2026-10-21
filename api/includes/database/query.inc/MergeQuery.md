# MergeQuery

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 1276–1678 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1276-L1678)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class MergeQuery extends Query implements QueryConditionInterface
```

## Documentation

```text
General class for an abstracted MERGE query operation.

An ANSI SQL:2003 compatible database would run the following query:

@code
MERGE INTO table_name_1 USING table_name_2 ON (condition)
  WHEN MATCHED THEN
  UPDATE SET column1 = value1 [, column2 = value2 ...]
  WHEN NOT MATCHED THEN
  INSERT (column1 [, column2 ...]) VALUES (value1 [, value2 ...
@endcode

Other databases (most notably MySQL, PostgreSQL and SQLite) will emulate
this statement by running a SELECT and then INSERT or UPDATE.

By default, the two table names are identical and they are passed into the
the constructor. table_name_2 can be specified by the
MergeQuery::conditionTable() method. It can be either a string or a
subquery.

The condition is built exactly like SelectQuery or UpdateQuery conditions,
the UPDATE query part is built similarly like an UpdateQuery and finally the
INSERT query part is built similarly like an InsertQuery. However, both
UpdateQuery and InsertQuery has a fields method so
MergeQuery::updateFields() and MergeQuery::insertFields() needs to be called
instead. MergeQuery::fields() can also be called which calls both of these
methods as the common case is to use the same column-value pairs for both
INSERT and UPDATE. However, this is not mandatory. Another convenient
wrapper is MergeQuery::key() which adds the same column-value pairs to the
condition and the INSERT query part.

Several methods (key(), fields(), insertFields()) can be called to set a
key-value pair for the INSERT query part. Subsequent calls for the same
fields override the earlier ones. The same is true for UPDATE and key(),
fields() and updateFields().
```

## Constants

### STATUS_INSERT

```php
const STATUS_INSERT = 1;
```

```text
Returned by execute() if an INSERT query has been executed.
```

### STATUS_UPDATE

```php
const STATUS_UPDATE = 2;
```

```text
Returned by execute() if an UPDATE query has been executed.
```

## Properties

### $table

```php
protected $table;
```

```text
The table to be used for INSERT and UPDATE.

@var string
```

### $conditionTable

```php
protected $conditionTable;
```

```text
The table or subquery to be used for the condition.
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

### $insertFields

```php
protected $insertFields = array();
```

```text
An array of fields on which to insert.

@var array
```

### $defaultFields

```php
protected $defaultFields = array();
```

```text
An array of fields which should be set to their database-defined defaults.

Used on INSERT.

@var array
```

### $insertValues

```php
protected $insertValues = array();
```

```text
An array of values to be inserted.

@var string
```

### $updateFields

```php
protected $updateFields = array();
```

```text
An array of fields that will be updated.

@var array
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

### $needsUpdate

```php
protected $needsUpdate = FALSE;
```

```text
Flag indicating whether an UPDATE is necessary.

@var boolean
```

## Methods (derived index)

- [__construct()](MergeQuery/__construct.md) — Constructs a MergeQuery object.
- [conditionTable()](MergeQuery/conditionTable.md) — Sets the table or subquery to be used for the condition.
- [updateFields()](MergeQuery/updateFields.md) — Adds a set of field->value pairs to be updated.
- [expression()](MergeQuery/expression.md) — Specifies fields to be updated as an expression.
- [insertFields()](MergeQuery/insertFields.md) — Adds a set of field->value pairs to be inserted.
- [useDefaults()](MergeQuery/useDefaults.md) — Specifies fields for which the database-defaults should be used.
- [fields()](MergeQuery/fields.md) — Sets common field-value pairs in the INSERT and UPDATE query parts.
- [key()](MergeQuery/key.md) — Sets the key field(s) to be used as conditions for this query.
- [condition()](MergeQuery/condition.md) — Implements QueryConditionInterface::condition().
- [isNull()](MergeQuery/isNull.md) — Implements QueryConditionInterface::isNull().
- [isNotNull()](MergeQuery/isNotNull.md) — Implements QueryConditionInterface::isNotNull().
- [exists()](MergeQuery/exists.md) — Implements QueryConditionInterface::exists().
- [notExists()](MergeQuery/notExists.md) — Implements QueryConditionInterface::notExists().
- [conditions()](MergeQuery/conditions.md) — Implements QueryConditionInterface::conditions().
- [arguments()](MergeQuery/arguments.md) — Implements QueryConditionInterface::arguments().
- [where()](MergeQuery/where.md) — Implements QueryConditionInterface::where().
- [compile()](MergeQuery/compile.md) — Implements QueryConditionInterface::compile().
- [compiled()](MergeQuery/compiled.md) — Implements QueryConditionInterface::compiled().
- [__toString()](MergeQuery/__toString.md) — Implements PHP magic __toString method to convert the query to a string.
- [execute()](MergeQuery/execute.md)

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
