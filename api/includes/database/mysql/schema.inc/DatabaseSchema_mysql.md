# DatabaseSchema_mysql

- **Type:** Class
- **File:** [`includes/database/mysql/schema.inc`](_file.md), lines 14–545 · [local source](../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L14-L545)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
class DatabaseSchema_mysql extends DatabaseSchema
```

## Documentation

```text
@addtogroup schemaapi
@{
```

## Constants

### COMMENT_MAX_TABLE

```php
const COMMENT_MAX_TABLE = 60;
```

```text
Maximum length of a table comment in MySQL.
```

### COMMENT_MAX_COLUMN

```php
const COMMENT_MAX_COLUMN = 255;
```

```text
Maximum length of a column comment in MySQL.
```

## Methods (derived index)

- [getPrefixInfo()](DatabaseSchema_mysql/getPrefixInfo.md) — Get information about the table and database name from the prefix.
- [buildTableNameCondition()](DatabaseSchema_mysql/buildTableNameCondition.md) — Build a condition to match a table name against a standard information_schema.
- [createTableSql()](DatabaseSchema_mysql/createTableSql.md) — Generate SQL to create a new table from a Drupal schema definition.
- [createFieldSql()](DatabaseSchema_mysql/createFieldSql.md) — Create an SQL string for a field to be used in table creation or alteration.
- [processField()](DatabaseSchema_mysql/processField.md) — Set database-engine specific properties for a field.
- [getFieldTypeMap()](DatabaseSchema_mysql/getFieldTypeMap.md)
- [createKeysSql()](DatabaseSchema_mysql/createKeysSql.md)
- [createKeySql()](DatabaseSchema_mysql/createKeySql.md)
- [createKeysSqlHelper()](DatabaseSchema_mysql/createKeysSqlHelper.md)
- [renameTable()](DatabaseSchema_mysql/renameTable.md)
- [dropTable()](DatabaseSchema_mysql/dropTable.md)
- [addField()](DatabaseSchema_mysql/addField.md)
- [dropField()](DatabaseSchema_mysql/dropField.md)
- [fieldSetDefault()](DatabaseSchema_mysql/fieldSetDefault.md)
- [fieldSetNoDefault()](DatabaseSchema_mysql/fieldSetNoDefault.md)
- [indexExists()](DatabaseSchema_mysql/indexExists.md)
- [addPrimaryKey()](DatabaseSchema_mysql/addPrimaryKey.md)
- [dropPrimaryKey()](DatabaseSchema_mysql/dropPrimaryKey.md)
- [addUniqueKey()](DatabaseSchema_mysql/addUniqueKey.md)
- [dropUniqueKey()](DatabaseSchema_mysql/dropUniqueKey.md)
- [addIndex()](DatabaseSchema_mysql/addIndex.md)
- [dropIndex()](DatabaseSchema_mysql/dropIndex.md)
- [changeField()](DatabaseSchema_mysql/changeField.md)
- [prepareComment()](DatabaseSchema_mysql/prepareComment.md)
- [getComment()](DatabaseSchema_mysql/getComment.md) — Retrieve a table or column comment.
- [tableExists()](DatabaseSchema_mysql/tableExists.md)
- [fieldExists()](DatabaseSchema_mysql/fieldExists.md)

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
