# SelectQueryExtender

- **Type:** Class
- **File:** [`includes/database/select.inc`](_file.md), lines 536–855 · [local source](../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L536-L855)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class SelectQueryExtender implements SelectQueryInterface
```

## Documentation

```text
The base extender class for Select queries.
```

## Properties

### $query

```php
protected $query;
```

```text
The SelectQuery object we are extending/decorating.

@var SelectQueryInterface
```

### $connection

```php
protected $connection;
```

```text
The connection object on which to run this query.

@var DatabaseConnection
```

### $uniqueIdentifier

```php
protected $uniqueIdentifier;
```

```text
A unique identifier for this query object.
```

### $placeholder

```php
protected $placeholder = 0;
```

```text
The placeholder counter.
```

## Methods (derived index)

- [__construct()](SelectQueryExtender/__construct.md)
- [uniqueIdentifier()](SelectQueryExtender/uniqueIdentifier.md) — Implements QueryPlaceholderInterface::uniqueIdentifier().
- [nextPlaceholder()](SelectQueryExtender/nextPlaceholder.md) — Implements QueryPlaceholderInterface::nextPlaceholder().
- [addTag()](SelectQueryExtender/addTag.md)
- [hasTag()](SelectQueryExtender/hasTag.md)
- [hasAllTags()](SelectQueryExtender/hasAllTags.md)
- [hasAnyTag()](SelectQueryExtender/hasAnyTag.md)
- [addMetaData()](SelectQueryExtender/addMetaData.md)
- [getMetaData()](SelectQueryExtender/getMetaData.md)
- [condition()](SelectQueryExtender/condition.md)
- [conditions()](SelectQueryExtender/conditions.md)
- [arguments()](SelectQueryExtender/arguments.md)
- [where()](SelectQueryExtender/where.md)
- [compile()](SelectQueryExtender/compile.md)
- [compiled()](SelectQueryExtender/compiled.md)
- [havingCondition()](SelectQueryExtender/havingCondition.md)
- [havingConditions()](SelectQueryExtender/havingConditions.md)
- [havingArguments()](SelectQueryExtender/havingArguments.md)
- [having()](SelectQueryExtender/having.md)
- [havingCompile()](SelectQueryExtender/havingCompile.md)
- [extend()](SelectQueryExtender/extend.md)
- [getFields()](SelectQueryExtender/getFields.md)
- [getExpressions()](SelectQueryExtender/getExpressions.md)
- [getOrderBy()](SelectQueryExtender/getOrderBy.md)
- [getGroupBy()](SelectQueryExtender/getGroupBy.md)
- [getTables()](SelectQueryExtender/getTables.md)
- [getUnion()](SelectQueryExtender/getUnion.md)
- [getArguments()](SelectQueryExtender/getArguments.md)
- [isPrepared()](SelectQueryExtender/isPrepared.md)
- [preExecute()](SelectQueryExtender/preExecute.md)
- [execute()](SelectQueryExtender/execute.md)
- [distinct()](SelectQueryExtender/distinct.md)
- [addField()](SelectQueryExtender/addField.md)
- [fields()](SelectQueryExtender/fields.md)
- [addExpression()](SelectQueryExtender/addExpression.md)
- [join()](SelectQueryExtender/join.md)
- [innerJoin()](SelectQueryExtender/innerJoin.md)
- [leftJoin()](SelectQueryExtender/leftJoin.md)
- [rightJoin()](SelectQueryExtender/rightJoin.md)
- [addJoin()](SelectQueryExtender/addJoin.md)
- [orderBy()](SelectQueryExtender/orderBy.md)
- [orderRandom()](SelectQueryExtender/orderRandom.md)
- [range()](SelectQueryExtender/range.md)
- [union()](SelectQueryExtender/union.md)
- [groupBy()](SelectQueryExtender/groupBy.md)
- [forUpdate()](SelectQueryExtender/forUpdate.md)
- [countQuery()](SelectQueryExtender/countQuery.md)
- [isNull()](SelectQueryExtender/isNull.md)
- [isNotNull()](SelectQueryExtender/isNotNull.md)
- [exists()](SelectQueryExtender/exists.md)
- [notExists()](SelectQueryExtender/notExists.md)
- [__toString()](SelectQueryExtender/__toString.md)
- [__clone()](SelectQueryExtender/__clone.md)
- [__call()](SelectQueryExtender/__call.md) — Magic override for undefined methods.

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
