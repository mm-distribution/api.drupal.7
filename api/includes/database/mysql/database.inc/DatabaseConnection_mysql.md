# DatabaseConnection_mysql

- **Type:** Class
- **File:** [`includes/database/mysql/database.inc`](_file.md), lines 18–661 · [local source](../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L18-L661)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class DatabaseConnection_mysql extends DatabaseConnection
```

## Documentation

```text
@addtogroup database
@{
```

## Properties

### $needsCleanup

```php
protected $needsCleanup = FALSE;
```

```text
Flag to indicate if the cleanup function in __destruct() should run.

@var boolean
```

### $reservedKeyWords

```php
private $reservedKeyWords = array(
    'accessible',
    'add',
    'admin',
    'all',
    'alter',
    'analyze',
    'and',
    'as',
    'asc',
    'asensitive',
    'before',
    'between',
    'bigint',
    'binary',
    'blob',
    'both',
    'by',
    'call',
    'cascade',
    'case',
    'change',
    'char',
    'character',
    'check',
    'collate',
    'column',
    'condition',
    'constraint',
    'continue',
    'convert',
    'create',
    'cross',
    'cube',
    'cume_dist',
    'current_date',
    'current_time',
    'current_timestamp',
    'current_user',
    'cursor',
    'database',
    'databases',
    'day_hour',
    'day_microsecond',
    'day_minute',
    'day_second',
    'dec',
    'decimal',
    'declare',
    'default',
    'delayed',
    'delete',
    'dense_rank',
    'desc',
    'describe',
    'deterministic',
    'distinct',
    'distinctrow',
    'div',
    'double',
    'drop',
    'dual',
    'each',
    'else',
    'elseif',
    'empty',
    'enclosed',
    'escaped',
    'except',
    'exists',
    'exit',
    'explain',
    'false',
    'fetch',
    'first_value',
    'float',
    'float4',
    'float8',
    'for',
    'force',
    'foreign',
    'from',
    'fulltext',
    'function',
    'generated',
    'get',
    'grant',
    'group',
    'grouping',
    'groups',
    'having',
    'high_priority',
    'hour_microsecond',
    'hour_minute',
    'hour_second',
    'if',
    'ignore',
    'in',
    'index',
    'infile',
    'inner',
    'inout',
    'insensitive',
    'insert',
    'int',
    'int1',
    'int2',
    'int3',
    'int4',
    'int8',
    'integer',
    'intersect',
    'interval',
    'into',
    'io_after_gtids',
    'io_before_gtids',
    'is',
    'iterate',
    'join',
    'json_table',
    'key',
    'keys',
    'kill',
    'lag',
    'last_value',
    'lateral',
    'lead',
    'leading',
    'leave',
    'left',
    'like',
    'limit',
    'linear',
    'lines',
    'load',
    'localtime',
    'localtimestamp',
    'lock',
    'long',
    'longblob',
    'longtext',
    'loop',
    'low_priority',
    'master_bind',
    'master_ssl_verify_server_cert',
    'match',
    'maxvalue',
    'mediumblob',
    'mediumint',
    'mediumtext',
    'middleint',
    'minute_microsecond',
    'minute_second',
    'mod',
    'modifies',
    'natural',
    'not',
    'no_write_to_binlog',
    'nth_value',
    'ntile',
    'null',
    'numeric',
    'of',
    'on',
    'optimize',
    'optimizer_costs',
    'option',
    'optionally',
    'or',
    'order',
    'out',
    'outer',
    'outfile',
    'over',
    'partition',
    'percent_rank',
    'persist',
    'persist_only',
    'precision',
    'primary',
    'procedure',
    'purge',
    'range',
    'rank',
    'read',
    'reads',
    'read_write',
    'real',
    'recursive',
    'references',
    'regexp',
    'release',
    'rename',
    'repeat',
    'replace',
    'require',
    'resignal',
    'restrict',
    'return',
    'revoke',
    'right',
    'rlike',
    'row',
    'rows',
    'row_number',
    'schema',
    'schemas',
    'second_microsecond',
    'select',
    'sensitive',
    'separator',
    'set',
    'show',
    'signal',
    'smallint',
    'spatial',
    'specific',
    'sql',
    'sqlexception',
    'sqlstate',
    'sqlwarning',
    'sql_big_result',
    'sql_calc_found_rows',
    'sql_small_result',
    'ssl',
    'starting',
    'stored',
    'straight_join',
    'system',
    'table',
    'terminated',
    'then',
    'tinyblob',
    'tinyint',
    'tinytext',
    'to',
    'trailing',
    'trigger',
    'true',
    'undo',
    'union',
    'unique',
    'unlock',
    'unsigned',
    'update',
    'usage',
    'use',
    'using',
    'utc_date',
    'utc_time',
    'utc_timestamp',
    'values',
    'varbinary',
    'varchar',
    'varcharacter',
    'varying',
    'virtual',
    'when',
    'where',
    'while',
    'window',
    'with',
    'write',
    'xor',
    'year_month',
    'zerofill',
  );
```

```text
The list of MySQL reserved key words.

@link https://dev.mysql.com/doc/refman/8.0/en/keywords.html
```

## Methods (derived index)

- [__construct()](DatabaseConnection_mysql/__construct.md)
- [setPrefix()](DatabaseConnection_mysql/setPrefix.md) — {@inheritdoc}}
- [escapeField()](DatabaseConnection_mysql/escapeField.md) — {@inheritdoc}
- [escapeFields()](DatabaseConnection_mysql/escapeFields.md)
- [escapeAlias()](DatabaseConnection_mysql/escapeAlias.md) — {@inheritdoc}
- [quoteIdentifier()](DatabaseConnection_mysql/quoteIdentifier.md) — Quotes an identifier if it matches a MySQL reserved keyword.
- [__destruct()](DatabaseConnection_mysql/__destruct.md)
- [queryRange()](DatabaseConnection_mysql/queryRange.md)
- [queryTemporary()](DatabaseConnection_mysql/queryTemporary.md)
- [driver()](DatabaseConnection_mysql/driver.md)
- [databaseType()](DatabaseConnection_mysql/databaseType.md)
- [mapConditionOperator()](DatabaseConnection_mysql/mapConditionOperator.md)
- [nextId()](DatabaseConnection_mysql/nextId.md)
- [nextIdDelete()](DatabaseConnection_mysql/nextIdDelete.md)
- [popCommittableTransactions()](DatabaseConnection_mysql/popCommittableTransactions.md) — Overridden to work around issues to MySQL not supporting transactional DDL.
- [doCommit()](DatabaseConnection_mysql/doCommit.md) — Do the actual commit, including a workaround for PHP 8 behaviour changes.
- [rollback()](DatabaseConnection_mysql/rollback.md) — {@inheritdoc}
- [utf8mb4IsConfigurable()](DatabaseConnection_mysql/utf8mb4IsConfigurable.md)
- [utf8mb4IsActive()](DatabaseConnection_mysql/utf8mb4IsActive.md)
- [utf8mb4IsSupported()](DatabaseConnection_mysql/utf8mb4IsSupported.md)

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
