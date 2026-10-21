# SelectQueryInterface

- **Type:** Interface
- **File:** [`includes/database/select.inc`](_file.md), lines 39–531 · [local source](../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L39-L531)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
interface SelectQueryInterface extends QueryConditionInterface, QueryAlterableInterface, QueryExtendableInterface, QueryPlaceholderInterface
```

## Documentation

```text
Interface definition for a Select Query object.
```

## Methods (derived index)

- [getFields()](SelectQueryInterface/getFields.md) — Returns a reference to the fields array for this query.
- [getExpressions()](SelectQueryInterface/getExpressions.md) — Returns a reference to the expressions array for this query.
- [getOrderBy()](SelectQueryInterface/getOrderBy.md) — Returns a reference to the order by array for this query.
- [getGroupBy()](SelectQueryInterface/getGroupBy.md) — Returns a reference to the group-by array for this query.
- [getTables()](SelectQueryInterface/getTables.md) — Returns a reference to the tables array for this query.
- [getUnion()](SelectQueryInterface/getUnion.md) — Returns a reference to the union queries for this query. This include queries for UNION, UNION ALL, and UNION DISTINCT.
- [getArguments()](SelectQueryInterface/getArguments.md) — Compiles and returns an associative array of the arguments for this prepared statement.
- [distinct()](SelectQueryInterface/distinct.md) — Sets this query to be DISTINCT.
- [addField()](SelectQueryInterface/addField.md) — Adds a field to the list to be SELECTed.
- [fields()](SelectQueryInterface/fields.md) — Add multiple fields from the same table to be SELECTed.
- [addExpression()](SelectQueryInterface/addExpression.md) — Adds an expression to the list of "fields" to be SELECTed.
- [join()](SelectQueryInterface/join.md) — Default Join against another table in the database.
- [innerJoin()](SelectQueryInterface/innerJoin.md) — Inner Join against another table in the database.
- [leftJoin()](SelectQueryInterface/leftJoin.md) — Left Outer Join against another table in the database.
- [rightJoin()](SelectQueryInterface/rightJoin.md) — Right Outer Join against another table in the database.
- [addJoin()](SelectQueryInterface/addJoin.md) — Join against another table in the database.
- [orderBy()](SelectQueryInterface/orderBy.md) — Orders the result set by a given field.
- [orderRandom()](SelectQueryInterface/orderRandom.md) — Orders the result set by a random value.
- [range()](SelectQueryInterface/range.md) — Restricts a query to a given range in the result set.
- [union()](SelectQueryInterface/union.md) — Add another Select query to UNION to this one.
- [groupBy()](SelectQueryInterface/groupBy.md) — Groups the result set by the specified field.
- [countQuery()](SelectQueryInterface/countQuery.md) — Get the equivalent COUNT query of this query as a new query object.
- [isPrepared()](SelectQueryInterface/isPrepared.md) — Indicates if preExecute() has already been called on that object.
- [preExecute()](SelectQueryInterface/preExecute.md) — Generic preparation and validation for a SELECT query.
- [havingCondition()](SelectQueryInterface/havingCondition.md) — Helper function to build most common HAVING conditional clauses.
- [__clone()](SelectQueryInterface/__clone.md) — Clone magic method.
- [forUpdate()](SelectQueryInterface/forUpdate.md) — Add FOR UPDATE to the query.

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
