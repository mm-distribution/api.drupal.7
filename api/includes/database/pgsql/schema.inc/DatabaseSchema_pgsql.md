# DatabaseSchema_pgsql

- **Type:** Class
- **File:** [`includes/database/pgsql/schema.inc`](_file.md), lines 13–856 · [local source](../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L13-L856)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
class DatabaseSchema_pgsql extends DatabaseSchema
```

## Documentation

```text
@ingroup schemaapi
@{
```

## Properties

### $tempNamespaceName

```php
protected $tempNamespaceName;
```

```text
PostgreSQL's temporary namespace name.

@var string
```

### $tableInformation

```php
protected $tableInformation = array();
```

```text
A cache of information about blob columns and sequences of tables.

This is collected by DatabaseConnection_pgsql->queryTableInformation(),
by introspecting the database.

@see DatabaseConnection_pgsql->queryTableInformation()
@var array
```

### $maxIdentifierLength

```php
protected $maxIdentifierLength;
```

```text
The maximum allowed length for index, primary key and constraint names.

Value will usually be set to a 63 chars limit but PostgreSQL allows
to higher this value before compiling, so we need to check for that.

@var int
```

## Methods (derived index)

- [ensureIdentifiersLength()](DatabaseSchema_pgsql/ensureIdentifiersLength.md) — Make sure to limit identifiers according to PostgreSQL compiled in length.
- [queryTableInformation()](DatabaseSchema_pgsql/queryTableInformation.md) — Fetch the list of blobs and sequences used on a table.
- [getTempNamespaceName()](DatabaseSchema_pgsql/getTempNamespaceName.md) — Gets PostgreSQL's temporary namespace name.
- [queryFieldInformation()](DatabaseSchema_pgsql/queryFieldInformation.md) — Fetch the list of CHECK constraints used on a field.
- [createTableSql()](DatabaseSchema_pgsql/createTableSql.md) — Generate SQL to create a new table from a Drupal schema definition.
- [createFieldSql()](DatabaseSchema_pgsql/createFieldSql.md) — Create an SQL string for a field to be used in table creation or alteration.
- [processField()](DatabaseSchema_pgsql/processField.md) — Set database-engine specific properties for a field.
- [getFieldTypeMap()](DatabaseSchema_pgsql/getFieldTypeMap.md) — This maps a generic data type in combination with its data size to the engine-specific data type.
- [_createKeySql()](DatabaseSchema_pgsql/_createKeySql.md)
- [tableExists()](DatabaseSchema_pgsql/tableExists.md) — {@inheritdoc}
- [findTables()](DatabaseSchema_pgsql/findTables.md) — {@inheritdoc}
- [renameTable()](DatabaseSchema_pgsql/renameTable.md)
- [dropTable()](DatabaseSchema_pgsql/dropTable.md)
- [addField()](DatabaseSchema_pgsql/addField.md)
- [dropField()](DatabaseSchema_pgsql/dropField.md)
- [fieldSetDefault()](DatabaseSchema_pgsql/fieldSetDefault.md)
- [fieldSetNoDefault()](DatabaseSchema_pgsql/fieldSetNoDefault.md)
- [fieldExists()](DatabaseSchema_pgsql/fieldExists.md) — {@inheritdoc}
- [indexExists()](DatabaseSchema_pgsql/indexExists.md)
- [constraintExists()](DatabaseSchema_pgsql/constraintExists.md) — Helper function: check if a constraint (PK, FK, UK) exists.
- [addPrimaryKey()](DatabaseSchema_pgsql/addPrimaryKey.md)
- [dropPrimaryKey()](DatabaseSchema_pgsql/dropPrimaryKey.md)
- [addUniqueKey()](DatabaseSchema_pgsql/addUniqueKey.md)
- [dropUniqueKey()](DatabaseSchema_pgsql/dropUniqueKey.md)
- [addIndex()](DatabaseSchema_pgsql/addIndex.md)
- [dropIndex()](DatabaseSchema_pgsql/dropIndex.md)
- [changeField()](DatabaseSchema_pgsql/changeField.md)
- [_createIndexSql()](DatabaseSchema_pgsql/_createIndexSql.md)
- [_createKeys()](DatabaseSchema_pgsql/_createKeys.md)
- [getComment()](DatabaseSchema_pgsql/getComment.md) — Retrieve a table or column comment.
- [hashBase64()](DatabaseSchema_pgsql/hashBase64.md) — Calculates a base-64 encoded, PostgreSQL-safe sha-256 hash per PostgreSQL documentation: 4.1. Lexical Structure.
- [buildTableNameCondition()](DatabaseSchema_pgsql/buildTableNameCondition.md) — Build a condition to match a table name against a standard information_schema.

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
