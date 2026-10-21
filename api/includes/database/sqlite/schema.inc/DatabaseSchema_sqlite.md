# DatabaseSchema_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/schema.inc`](_file.md), lines 14–714 · [local source](../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L14-L714)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
class DatabaseSchema_sqlite extends DatabaseSchema
```

## Documentation

```text
@ingroup schemaapi
@{
```

## Properties

### $defaultSchema

```php
protected $defaultSchema = 'main';
```

```text
Override DatabaseSchema::$defaultSchema
```

## Methods (derived index)

- [tableExists()](DatabaseSchema_sqlite/tableExists.md)
- [fieldExists()](DatabaseSchema_sqlite/fieldExists.md)
- [createTableSql()](DatabaseSchema_sqlite/createTableSql.md) — Generate SQL to create a new table from a Drupal schema definition.
- [createIndexSql()](DatabaseSchema_sqlite/createIndexSql.md) — Build the SQL expression for indexes.
- [createColumsSql()](DatabaseSchema_sqlite/createColumsSql.md) — Build the SQL expression for creating columns.
- [createKeySql()](DatabaseSchema_sqlite/createKeySql.md) — Build the SQL expression for keys.
- [processField()](DatabaseSchema_sqlite/processField.md) — Set database-engine specific properties for a field.
- [createFieldSql()](DatabaseSchema_sqlite/createFieldSql.md) — Create an SQL string for a field to be used in table creation or alteration.
- [getFieldTypeMap()](DatabaseSchema_sqlite/getFieldTypeMap.md) — This maps a generic data type in combination with its data size to the engine-specific data type.
- [renameTable()](DatabaseSchema_sqlite/renameTable.md)
- [dropTable()](DatabaseSchema_sqlite/dropTable.md)
- [addField()](DatabaseSchema_sqlite/addField.md)
- [alterTable()](DatabaseSchema_sqlite/alterTable.md) — Create a table with a new schema containing the old content.
- [introspectSchema()](DatabaseSchema_sqlite/introspectSchema.md) — Find out the schema of a table.
- [dropField()](DatabaseSchema_sqlite/dropField.md)
- [changeField()](DatabaseSchema_sqlite/changeField.md)
- [mapKeyDefinition()](DatabaseSchema_sqlite/mapKeyDefinition.md) — Utility method: rename columns in an index definition according to a new mapping.
- [addIndex()](DatabaseSchema_sqlite/addIndex.md)
- [indexExists()](DatabaseSchema_sqlite/indexExists.md)
- [dropIndex()](DatabaseSchema_sqlite/dropIndex.md)
- [addUniqueKey()](DatabaseSchema_sqlite/addUniqueKey.md)
- [dropUniqueKey()](DatabaseSchema_sqlite/dropUniqueKey.md)
- [addPrimaryKey()](DatabaseSchema_sqlite/addPrimaryKey.md)
- [dropPrimaryKey()](DatabaseSchema_sqlite/dropPrimaryKey.md)
- [fieldSetDefault()](DatabaseSchema_sqlite/fieldSetDefault.md)
- [fieldSetNoDefault()](DatabaseSchema_sqlite/fieldSetNoDefault.md)
- [findTables()](DatabaseSchema_sqlite/findTables.md) — {@inheritdoc}
- [findTablesD8()](DatabaseSchema_sqlite/findTablesD8.md) — {@inheritdoc}

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
