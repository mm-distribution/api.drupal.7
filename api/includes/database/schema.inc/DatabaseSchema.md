# DatabaseSchema

- **Type:** Class
- **File:** [`includes/database/schema.inc`](_file.md), lines 170–778 · [local source](../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L170-L778)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
abstract class DatabaseSchema implements QueryPlaceholderInterface
```

## Documentation

```text
Base class for database schema definitions.
```

## Properties

### $connection

```php
protected $connection;
```

```text
The database connection.

@var DatabaseConnection
```

### $placeholder

```php
protected $placeholder = 0;
```

```text
The placeholder counter.
```

### $defaultSchema

```php
protected $defaultSchema = 'public';
```

```text
Definition of prefixInfo array structure.

Rather than redefining DatabaseSchema::getPrefixInfo() for each driver,
by defining the defaultSchema variable only MySQL has to re-write the
method.

@see DatabaseSchema::getPrefixInfo()
```

### $uniqueIdentifier

```php
protected $uniqueIdentifier;
```

```text
A unique identifier for this query object.
```

## Methods (derived index)

- [__construct()](DatabaseSchema/__construct.md)
- [__clone()](DatabaseSchema/__clone.md) — Implements the magic __clone function.
- [uniqueIdentifier()](DatabaseSchema/uniqueIdentifier.md) — Implements QueryPlaceHolderInterface::uniqueIdentifier().
- [nextPlaceholder()](DatabaseSchema/nextPlaceholder.md) — Implements QueryPlaceHolderInterface::nextPlaceholder().
- [getPrefixInfo()](DatabaseSchema/getPrefixInfo.md) — Get information about the table name and schema from the prefix.
- [prefixNonTable()](DatabaseSchema/prefixNonTable.md) — Create names for indexes, primary keys and constraints.
- [buildTableNameCondition()](DatabaseSchema/buildTableNameCondition.md) — Build a condition to match a table name against a standard information_schema.
- [tableExists()](DatabaseSchema/tableExists.md) — Check if a table exists.
- [findTables()](DatabaseSchema/findTables.md) — Find all tables that are like the specified base table name.
- [findTablesD8()](DatabaseSchema/findTablesD8.md) — Finds all tables that are like the specified base table name. This is a backport of the change made to findTables in Drupal 8 to work with virtual, un-prefixed table names. The original function is retained for Backwards Compatibility.
- [fieldExists()](DatabaseSchema/fieldExists.md) — Check if a column exists in the given table.
- [getFieldTypeMap()](DatabaseSchema/getFieldTypeMap.md) — Returns a mapping of Drupal schema field names to DB-native field types.
- [renameTable()](DatabaseSchema/renameTable.md) — Rename a table.
- [dropTable()](DatabaseSchema/dropTable.md) — Drop a table.
- [addField()](DatabaseSchema/addField.md) — Add a new field to a table.
- [dropField()](DatabaseSchema/dropField.md) — Drop a field.
- [fieldSetDefault()](DatabaseSchema/fieldSetDefault.md) — Set the default value for a field.
- [fieldSetNoDefault()](DatabaseSchema/fieldSetNoDefault.md) — Set a field to have no default value.
- [indexExists()](DatabaseSchema/indexExists.md) — Checks if an index exists in the given table.
- [addPrimaryKey()](DatabaseSchema/addPrimaryKey.md) — Add a primary key.
- [dropPrimaryKey()](DatabaseSchema/dropPrimaryKey.md) — Drop the primary key.
- [addUniqueKey()](DatabaseSchema/addUniqueKey.md) — Add a unique key.
- [dropUniqueKey()](DatabaseSchema/dropUniqueKey.md) — Drop a unique key.
- [addIndex()](DatabaseSchema/addIndex.md) — Add an index.
- [dropIndex()](DatabaseSchema/dropIndex.md) — Drop an index.
- [changeField()](DatabaseSchema/changeField.md) — Change a field definition.
- [createTable()](DatabaseSchema/createTable.md) — Create a new table from a Drupal table definition.
- [fieldNames()](DatabaseSchema/fieldNames.md) — Return an array of field names from an array of key/index column specifiers.
- [prepareComment()](DatabaseSchema/prepareComment.md) — Prepare a table or column comment for database query.

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
