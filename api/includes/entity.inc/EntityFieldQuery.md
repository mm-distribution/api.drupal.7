# EntityFieldQuery

- **Type:** Class
- **File:** [`includes/entity.inc`](_file.md), lines 475–1434 · [local source](../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L475-L1434)

## Signature

```php
class EntityFieldQuery
```

## Documentation

```text
Retrieves entities matching a given set of conditions.

This class allows finding entities based on entity properties (for example,
node->changed), field values, and generic entity meta data (bundle,
entity type, entity ID, and revision ID). It is not possible to query across
multiple entity types. For example, there is no facility to find published
nodes written by users created in the last hour, as this would require
querying both node->status and user->created.

Normally we would not want to have public properties on the object, as that
allows the object's state to become inconsistent too easily. However, this
class's standard use case involves primarily code that does need to have
direct access to the collected properties in order to handle alternate
execution routines. We therefore use public properties for simplicity. Note
that code that is simply creating and running a field query should still use
the appropriate methods to add conditions on the query.

Storage engines are not required to support every type of query. By default,
an EntityFieldQueryException will be raised if an unsupported condition is
specified or if the query has field conditions or sorts that are stored in
different field storage engines. However, this logic can be overridden in
hook_entity_query_alter().

Also note that this query does not automatically respect entity access
restrictions. Node access control is performed by the SQL storage engine but
other storage engines might not do this.
```

## Constants

### RETURN_ALL

```php
const RETURN_ALL = NULL;
```

```text
Indicates that both deleted and non-deleted fields should be returned.

@see EntityFieldQuery::deleted()
```

## Properties

### $altered

```php
public $altered = FALSE;
```

```text
TRUE if the query has already been altered, FALSE if it hasn't.

Used in alter hooks to check for cloned queries that have already been
altered prior to the clone (for example, the pager count query).

@var boolean
```

### $entityConditions

```php
public $entityConditions = array();
```

```text
Associative array of entity-generic metadata conditions.

@var array

@see EntityFieldQuery::entityCondition()
```

### $fieldConditions

```php
public $fieldConditions = array();
```

```text
List of field conditions.

@var array

@see EntityFieldQuery::fieldCondition()
```

### $fieldMetaConditions

```php
public $fieldMetaConditions = array();
```

```text
List of field meta conditions (language and delta).

Field conditions operate on columns specified by hook_field_schema(),
the meta conditions operate on columns added by the system: delta
and language. These can not be mixed with the field conditions because
field columns can have any name including delta and language.

@var array

@see EntityFieldQuery::fieldLanguageCondition()
@see EntityFieldQuery::fieldDeltaCondition()
```

### $propertyConditions

```php
public $propertyConditions = array();
```

```text
List of property conditions.

@var array

@see EntityFieldQuery::propertyCondition()
```

### $order

```php
public $order = array();
```

```text
List of order clauses.

@var array
```

### $range

```php
public $range = array();
```

```text
The query range.

@var array

@see EntityFieldQuery::range()
```

### $pager

```php
public $pager = array();
```

```text
The query pager data.

@var array

@see EntityFieldQuery::pager()
```

### $deleted

```php
public $deleted = FALSE;
```

```text
Query behavior for deleted data.

TRUE to return only deleted data, FALSE to return only non-deleted data,
EntityFieldQuery::RETURN_ALL to return everything.

@see EntityFieldQuery::deleted()
```

### $fields

```php
public $fields = array();
```

```text
A list of field arrays used.

Field names passed to EntityFieldQuery::fieldCondition() and
EntityFieldQuery::fieldOrderBy() are run through field_info_field() before
stored in this array. This way, the elements of this array are field
arrays.

@var array
```

### $count

```php
public $count = FALSE;
```

```text
TRUE if this is a count query, FALSE if it isn't.

@var boolean
```

### $age

```php
public $age = FIELD_LOAD_CURRENT;
```

```text
Flag indicating whether this is querying current or all revisions.

@var int

@see EntityFieldQuery::age()
```

### $tags

```php
public $tags = array();
```

```text
A list of the tags added to this query.

@var array

@see EntityFieldQuery::addTag()
```

### $metaData

```php
public $metaData = array();
```

```text
A list of metadata added to this query.

@var array

@see EntityFieldQuery::addMetaData()
```

### $ordered_results

```php
public $ordered_results = array();
```

```text
The ordered results.

@var array

@see EntityFieldQuery::execute().
```

### $executeCallback

```php
public $executeCallback = '';
```

```text
The method executing the query, if it is overriding the default.

@var string

@see EntityFieldQuery::execute().
```

## Methods (derived index)

- [entityCondition()](EntityFieldQuery/entityCondition.md) — Adds a condition on entity-generic metadata.
- [fieldCondition()](EntityFieldQuery/fieldCondition.md) — Adds a condition on field values.
- [fieldLanguageCondition()](EntityFieldQuery/fieldLanguageCondition.md) — Adds a condition on the field language column.
- [fieldDeltaCondition()](EntityFieldQuery/fieldDeltaCondition.md) — Adds a condition on the field delta column.
- [addFieldCondition()](EntityFieldQuery/addFieldCondition.md) — Adds the given condition to the proper condition array.
- [propertyCondition()](EntityFieldQuery/propertyCondition.md) — Adds a condition on an entity-specific property.
- [entityOrderBy()](EntityFieldQuery/entityOrderBy.md) — Orders the result set by entity-generic metadata.
- [fieldOrderBy()](EntityFieldQuery/fieldOrderBy.md) — Orders the result set by a given field column.
- [propertyOrderBy()](EntityFieldQuery/propertyOrderBy.md) — Orders the result set by an entity-specific property.
- [count()](EntityFieldQuery/count.md) — Sets the query to be a count query only.
- [range()](EntityFieldQuery/range.md) — Restricts a query to a given range in the result set.
- [pager()](EntityFieldQuery/pager.md) — Enables a pager for the query.
- [tableSort()](EntityFieldQuery/tableSort.md) — Enables sortable tables for this query.
- [deleted()](EntityFieldQuery/deleted.md) — Filters on the data being deleted.
- [age()](EntityFieldQuery/age.md) — Queries the current or every revision.
- [addTag()](EntityFieldQuery/addTag.md) — Adds a tag to the query.
- [addMetaData()](EntityFieldQuery/addMetaData.md) — Adds additional metadata to the query.
- [execute()](EntityFieldQuery/execute.md) — Executes the query.
- [queryCallback()](EntityFieldQuery/queryCallback.md) — Determines the query callback to use for this entity query.
- [propertyQuery()](EntityFieldQuery/propertyQuery.md) — Queries entity tables in SQL for property conditions and sorts.
- [initializePager()](EntityFieldQuery/initializePager.md) — Gets the total number of results and initializes a pager for the query.
- [finishQuery()](EntityFieldQuery/finishQuery.md) — Finishes the query.
- [addCondition()](EntityFieldQuery/addCondition.md) — Adds a condition to an already built SelectQuery (internal function).

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
