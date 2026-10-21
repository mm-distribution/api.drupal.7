# InsertQuery

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 441–728 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L441-L728)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class InsertQuery extends Query
```

## Documentation

```text
General class for an abstracted INSERT query.
```

## Properties

### $table

```php
protected $table;
```

```text
The table on which to insert.

@var string
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
An array of fields that should be set to their database-defined defaults.

@var array
```

### $insertValues

```php
protected $insertValues = array();
```

```text
A nested array of values to insert.

$insertValues is an array of arrays. Each sub-array is either an
associative array whose keys are field names and whose values are field
values to insert, or a non-associative array of values in the same order
as $insertFields.

Whether multiple insert sets will be run in a single query or multiple
queries is left to individual drivers to implement in whatever manner is
most appropriate. The order of values in each sub-array must match the
order of fields in $insertFields.

@var array
```

### $fromQuery

```php
protected $fromQuery;
```

```text
A SelectQuery object to fetch the rows that should be inserted.

@var SelectQueryInterface
```

## Methods (derived index)

- [__construct()](InsertQuery/__construct.md) — Constructs an InsertQuery object.
- [fields()](InsertQuery/fields.md) — Adds a set of field->value pairs to be inserted.
- [values()](InsertQuery/values.md) — Adds another set of values to the query to be inserted.
- [useDefaults()](InsertQuery/useDefaults.md) — Specifies fields for which the database defaults should be used.
- [from()](InsertQuery/from.md) — Sets the fromQuery on this InsertQuery object.
- [execute()](InsertQuery/execute.md) — Executes the insert query.
- [__toString()](InsertQuery/__toString.md) — Implements PHP magic __toString method to convert the query to a string.
- [preExecute()](InsertQuery/preExecute.md) — Preprocesses and validates the query.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
