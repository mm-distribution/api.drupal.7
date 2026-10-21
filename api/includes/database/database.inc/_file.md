# includes/database/database.inc

- **Source:** [local](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · 3176 lines

## File documentation

```text
@file
Core systems for the database layer.

Classes required for basic functioning of the database system should be
placed in this file.  All utility functions should also be placed in this
file only, as they cannot auto-load the way classes can.
```

## Functions (derived index)

- [db_query()](db_query.md) — Executes an arbitrary query string against the active database.
- [db_query_range()](db_query_range.md) — Executes a query against the active database, restricted to a range.
- [db_query_temporary()](db_query_temporary.md) — Executes a SELECT query string and saves the result set to a temporary table.
- [db_insert()](db_insert.md) — Returns a new InsertQuery object for the active database.
- [db_merge()](db_merge.md) — Returns a new MergeQuery object for the active database.
- [db_update()](db_update.md) — Returns a new UpdateQuery object for the active database.
- [db_delete()](db_delete.md) — Returns a new DeleteQuery object for the active database.
- [db_truncate()](db_truncate.md) — Returns a new TruncateQuery object for the active database.
- [db_select()](db_select.md) — Returns a new SelectQuery object for the active database.
- [db_transaction()](db_transaction.md) — Returns a new transaction object for the active database.
- [db_set_active()](db_set_active.md) — Sets a new active database.
- [db_escape_table()](db_escape_table.md) — Restricts a dynamic table name to safe characters.
- [db_escape_field()](db_escape_field.md) — Restricts a dynamic column or constraint name to safe characters.
- [db_like()](db_like.md) — Escapes characters that work as wildcard characters in a LIKE pattern.
- [db_driver()](db_driver.md) — Retrieves the name of the currently active database driver.
- [db_close()](db_close.md) — Closes the active database connection.
- [db_next_id()](db_next_id.md) — Retrieves a unique id.
- [db_or()](db_or.md) — Returns a new DatabaseCondition, set to "OR" all conditions together.
- [db_and()](db_and.md) — Returns a new DatabaseCondition, set to "AND" all conditions together.
- [db_xor()](db_xor.md) — Returns a new DatabaseCondition, set to "XOR" all conditions together.
- [db_condition()](db_condition.md) — Returns a new DatabaseCondition, set to the specified conjunction.
- [db_create_table()](db_create_table.md) — Creates a new table from a Drupal table definition.
- [db_field_names()](db_field_names.md) — Returns an array of field names from an array of key/index column specifiers.
- [db_index_exists()](db_index_exists.md) — Checks if an index exists in the given table.
- [db_table_exists()](db_table_exists.md) — Checks if a table exists.
- [db_field_exists()](db_field_exists.md) — Checks if a column exists in the given table.
- [db_find_tables()](db_find_tables.md) — Finds all tables that are like the specified base table name.
- [db_find_tables_d8()](db_find_tables_d8.md) — Finds all tables that are like the specified base table name. This is a backport of the change made to db_find_tables in Drupal 8 to work with virtual, un-prefixed table names. The original function is retained for Backwards Compatibility.
- [_db_create_keys_sql()](_db_create_keys_sql.md)
- [db_rename_table()](db_rename_table.md) — Renames a table.
- [db_drop_table()](db_drop_table.md) — Drops a table.
- [db_add_field()](db_add_field.md) — Adds a new field to a table.
- [db_drop_field()](db_drop_field.md) — Drops a field.
- [db_field_set_default()](db_field_set_default.md) — Sets the default value for a field.
- [db_field_set_no_default()](db_field_set_no_default.md) — Sets a field to have no default value.
- [db_add_primary_key()](db_add_primary_key.md) — Adds a primary key to a database table.
- [db_drop_primary_key()](db_drop_primary_key.md) — Drops the primary key of a database table.
- [db_add_unique_key()](db_add_unique_key.md) — Adds a unique key.
- [db_drop_unique_key()](db_drop_unique_key.md) — Drops a unique key.
- [db_add_index()](db_add_index.md) — Adds an index.
- [db_drop_index()](db_drop_index.md) — Drops an index.
- [db_change_field()](db_change_field.md) — Changes a field definition.
- [db_ignore_slave()](db_ignore_slave.md) — Sets a session variable specifying the lag time for ignoring a slave server.

## Classes and interfaces (derived index)

- [DatabaseConnection](DatabaseConnection.md) — Base Database API class.
- [Database](Database.md) — Primary front-controller for the database system.
- [DatabaseTransactionNoActiveException](DatabaseTransactionNoActiveException.md) — Exception for when popTransaction() is called with no active transaction.
- [DatabaseTransactionNameNonUniqueException](DatabaseTransactionNameNonUniqueException.md) — Exception thrown when a savepoint or transaction name occurs twice.
- [DatabaseTransactionCommitFailedException](DatabaseTransactionCommitFailedException.md) — Exception thrown when a commit() function fails.
- [DatabaseTransactionExplicitCommitNotAllowedException](DatabaseTransactionExplicitCommitNotAllowedException.md) — Exception to deny attempts to explicitly manage transactions.
- [DatabaseTransactionOutOfOrderException](DatabaseTransactionOutOfOrderException.md) — Exception thrown when a rollback() resulted in other active transactions being rolled-back.
- [InvalidMergeQueryException](InvalidMergeQueryException.md) — Exception thrown for merge queries that do not make semantic sense.
- [InvalidQueryConditionOperatorException](InvalidQueryConditionOperatorException.md) — Exception thrown if an invalid query condition is specified.
- [FieldsOverlapException](FieldsOverlapException.md) — Exception thrown if an insert query specifies a field twice.
- [NoFieldsException](NoFieldsException.md) — Exception thrown if an insert query doesn't specify insert or default fields.
- [DatabaseConnectionNotDefinedException](DatabaseConnectionNotDefinedException.md) — Exception thrown if an undefined database connection is requested.
- [DatabaseDriverNotSpecifiedException](DatabaseDriverNotSpecifiedException.md) — Exception thrown if no driver is specified for a database connection.
- [DatabaseTransaction](DatabaseTransaction.md) — A wrapper class for creating and managing database transactions.
- [DatabaseStatementInterface](DatabaseStatementInterface.md) — Represents a prepared statement.
- [DatabaseStatementBase](DatabaseStatementBase.md) — Default implementation of DatabaseStatementInterface.
- [DatabaseStatementEmpty](DatabaseStatementEmpty.md) — Empty implementation of a database statement.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
