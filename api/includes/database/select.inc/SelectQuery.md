# SelectQuery

- **Type:** Class
- **File:** [`includes/database/select.inc`](_file.md), lines 860–1675 · [local source](../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L860-L1675)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class SelectQuery extends Query implements SelectQueryInterface
```

## Documentation

```text
Query builder for SELECT statements.
```

## Properties

### $fields

```php
protected $fields = array();
```

```text
The fields to SELECT.

@var array
```

### $expressions

```php
protected $expressions = array();
```

```text
The expressions to SELECT as virtual fields.

@var array
```

### $tables

```php
protected $tables = array();
```

```text
The tables against which to JOIN.

This property is a nested array. Each entry is an array representing
a single table against which to join. The structure of each entry is:

array(
  'type' => $join_type (one of INNER, LEFT OUTER, RIGHT OUTER),
  'table' => $table,
  'alias' => $alias_of_the_table,
  'condition' => $join_condition (string or Condition object),
  'arguments' => $array_of_arguments_for_placeholders_in_the condition.
  'all_fields' => TRUE to SELECT $alias.*, FALSE or NULL otherwise.
)

If $table is a string, it is taken as the name of a table. If it is
a SelectQuery object, it is taken as a subquery.

If $join_condition is a Condition object, any arguments should be
incorporated into the object; a separate array of arguments does not need
to be provided.

@var array
```

### $order

```php
protected $order = array();
```

```text
The fields by which to order this query.

This is an associative array. The keys are the fields to order, and the value
is the direction to order, either ASC or DESC.

@var array
```

### $group

```php
protected $group = array();
```

```text
The fields by which to group.

@var array
```

### $where

```php
protected $where;
```

```text
The conditional object for the WHERE clause.

@var DatabaseCondition
```

### $having

```php
protected $having;
```

```text
The conditional object for the HAVING clause.

@var DatabaseCondition
```

### $distinct

```php
protected $distinct = FALSE;
```

```text
Whether or not this query should be DISTINCT

@var boolean
```

### $range

```php
protected $range;
```

```text
The range limiters for this query.

@var array
```

### $alterMetaData

```php
public $alterMetaData;
```

```text
The query metadata for alter purposes.

@var array
```

### $alterTags

```php
public $alterTags;
```

```text
The query tags.

@var array
```

### $union

```php
protected $union = array();
```

```text
An array whose elements specify a query to UNION, and the UNION type. The
'type' key may be '', 'ALL', or 'DISTINCT' to represent a 'UNION',
'UNION ALL', or 'UNION DISTINCT' statement, respectively.

All entries in this array will be applied from front to back, with the
first query to union on the right of the original query, the second union
to the right of the first, etc.

@var array
```

### $prepared

```php
protected $prepared = FALSE;
```

```text
Indicates if preExecute() has already been called.
@var boolean
```

### $forUpdate

```php
protected $forUpdate = FALSE;
```

```text
The FOR UPDATE status
```

## Methods (derived index)

- [__construct()](SelectQuery/__construct.md)
- [addTag()](SelectQuery/addTag.md)
- [hasTag()](SelectQuery/hasTag.md)
- [hasAllTags()](SelectQuery/hasAllTags.md)
- [hasAnyTag()](SelectQuery/hasAnyTag.md)
- [addMetaData()](SelectQuery/addMetaData.md)
- [getMetaData()](SelectQuery/getMetaData.md)
- [condition()](SelectQuery/condition.md)
- [conditions()](SelectQuery/conditions.md)
- [arguments()](SelectQuery/arguments.md)
- [where()](SelectQuery/where.md)
- [isNull()](SelectQuery/isNull.md)
- [isNotNull()](SelectQuery/isNotNull.md)
- [exists()](SelectQuery/exists.md)
- [notExists()](SelectQuery/notExists.md)
- [compile()](SelectQuery/compile.md)
- [compiled()](SelectQuery/compiled.md)
- [havingCondition()](SelectQuery/havingCondition.md)
- [havingConditions()](SelectQuery/havingConditions.md)
- [havingArguments()](SelectQuery/havingArguments.md)
- [having()](SelectQuery/having.md)
- [havingCompile()](SelectQuery/havingCompile.md)
- [extend()](SelectQuery/extend.md)
- [havingIsNull()](SelectQuery/havingIsNull.md)
- [havingIsNotNull()](SelectQuery/havingIsNotNull.md)
- [havingExists()](SelectQuery/havingExists.md)
- [havingNotExists()](SelectQuery/havingNotExists.md)
- [forUpdate()](SelectQuery/forUpdate.md)
- [getFields()](SelectQuery/getFields.md)
- [getExpressions()](SelectQuery/getExpressions.md)
- [getOrderBy()](SelectQuery/getOrderBy.md)
- [getGroupBy()](SelectQuery/getGroupBy.md)
- [getTables()](SelectQuery/getTables.md)
- [getUnion()](SelectQuery/getUnion.md)
- [getArguments()](SelectQuery/getArguments.md)
- [isPrepared()](SelectQuery/isPrepared.md) — Indicates if preExecute() has already been called on that object.
- [preExecute()](SelectQuery/preExecute.md) — Generic preparation and validation for a SELECT query.
- [execute()](SelectQuery/execute.md)
- [distinct()](SelectQuery/distinct.md)
- [addField()](SelectQuery/addField.md)
- [fields()](SelectQuery/fields.md)
- [addExpression()](SelectQuery/addExpression.md)
- [join()](SelectQuery/join.md)
- [innerJoin()](SelectQuery/innerJoin.md)
- [leftJoin()](SelectQuery/leftJoin.md)
- [rightJoin()](SelectQuery/rightJoin.md)
- [addJoin()](SelectQuery/addJoin.md)
- [orderBy()](SelectQuery/orderBy.md)
- [orderRandom()](SelectQuery/orderRandom.md)
- [range()](SelectQuery/range.md)
- [union()](SelectQuery/union.md)
- [groupBy()](SelectQuery/groupBy.md)
- [countQuery()](SelectQuery/countQuery.md)
- [__toString()](SelectQuery/__toString.md)
- [__clone()](SelectQuery/__clone.md)

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
