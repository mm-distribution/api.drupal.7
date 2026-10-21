# Database abstraction layer

- **Topic id:** `database`
- **Defined in:** [`includes/database/database.inc`](../includes/database/database.inc/_file.md), line 12 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L12)

## Documentation

```text
@defgroup database Database abstraction layer
@{
Allow the use of different database servers using the same code base.

Drupal provides a database abstraction layer to provide developers with
the ability to support multiple database servers easily. The intent of
this layer is to preserve the syntax and power of SQL as much as possible,
but also allow developers a way to leverage more complex functionality in
a unified way. It also provides a structured interface for dynamically
constructing queries when appropriate, and enforcing security checks and
similar good practices.

The system is built atop PHP's PDO (PHP Data Objects) database API and
inherits much of its syntax and semantics.

Most Drupal database SELECT queries are performed by a call to db_query() or
db_query_range(). Module authors should also consider using the PagerDefault
Extender for queries that return results that need to be presented on
multiple pages (see https://drupal.org/node/508796), and the TableSort
Extender for generating appropriate queries for sortable tables
(see https://drupal.org/node/1848372).

For example, one might wish to return a list of the most recent 10 nodes
authored by a given user. Instead of directly issuing the SQL query
@code
SELECT n.nid, n.title, n.created FROM node n WHERE n.uid = $uid
  ORDER BY n.created DESC LIMIT 0, 10;
@endcode
one would instead call the Drupal functions:
@code
$result = db_query_range('SELECT n.nid, n.title, n.created
  FROM {node} n WHERE n.uid = :uid
  ORDER BY n.created DESC', 0, 10, array(':uid' => $uid));
foreach ($result as $record) {
  // Perform operations on $record->title, etc. here.
}
@endcode
Curly braces are used around "node" to provide table prefixing via
DatabaseConnection::prefixTables(). The explicit use of a user ID is pulled
out into an argument passed to db_query() so that SQL injection attacks
from user input can be caught and nullified. The LIMIT syntax varies between
database servers, so that is abstracted into db_query_range() arguments.
Finally, note the PDO-based ability to iterate over the result set using
foreach ().

All queries are passed as a prepared statement string. A
prepared statement is a "template" of a query that omits literal or variable
values in favor of placeholders. The values to place into those
placeholders are passed separately, and the database driver handles
inserting the values into the query in a secure fashion. That means you
should never quote or string-escape a value to be inserted into the query.

There are two formats for placeholders: named and unnamed. Named placeholders
are strongly preferred in all cases as they are more flexible and
self-documenting. Named placeholders should start with a colon ":" and can be
followed by one or more letters, numbers or underscores.

Named placeholders begin with a colon followed by a unique string. Example:
@code
SELECT nid, title FROM {node} WHERE uid=:uid;
@endcode

":uid" is a placeholder that will be replaced with a literal value when
the query is executed. A given placeholder label cannot be repeated in a
given query, even if the value should be the same. When using named
placeholders, the array of arguments to the query must be an associative
array where keys are a placeholder label (e.g., :uid) and the value is the
corresponding value to use. The array may be in any order.

Unnamed placeholders are simply a question mark. Example:
@code
SELECT nid, title FROM {node} WHERE uid=?;
@endcode

In this case, the array of arguments must be an indexed array of values to
use in the exact same order as the placeholders in the query.

Note that placeholders should be a "complete" value. For example, when
running a LIKE query the SQL wildcard character, %, should be part of the
value, not the query itself. Thus, the following is incorrect:
@code
SELECT nid, title FROM {node} WHERE title LIKE :title%;
@endcode
It should instead read:
@code
SELECT nid, title FROM {node} WHERE title LIKE :title;
@endcode
and the value for :title should include a % as appropriate. Again, note the
lack of quotation marks around :title. Because the value is not inserted
into the query as one big string but as an explicitly separate value, the
database server knows where the query ends and a value begins. That is
considerably more secure against SQL injection than trying to remember
which values need quotation marks and string escaping and which don't.

INSERT, UPDATE, and DELETE queries need special care in order to behave
consistently across all different databases. Therefore, they use a special
object-oriented API for defining a query structurally. For example, rather
than:
@code
INSERT INTO node (nid, title, body) VALUES (1, 'my title', 'my body');
@endcode
one would instead write:
@code
$fields = array('nid' => 1, 'title' => 'my title', 'body' => 'my body');
db_insert('node')->fields($fields)->execute();
@endcode
This method allows databases that need special data type handling to do so,
while also allowing optimizations such as multi-insert queries. UPDATE and
DELETE queries have a similar pattern.

Drupal also supports transactions, including a transparent fallback for
databases that do not support transactions. To start a new transaction,
simply call $txn = db_transaction(); in your own code. The transaction will
remain open for as long as the variable $txn remains in scope.  When $txn is
destroyed, the transaction will be committed.  If your transaction is nested
inside of another then Drupal will track each transaction and only commit
the outer-most transaction when the last transaction object goes out out of
scope, that is, all relevant queries completed successfully.

Example:
@code
function my_transaction_function() {
  // The transaction opens here.
  $txn = db_transaction();

  try {
    $id = db_insert('example')
      ->fields(array(
        'field1' => 'mystring',
        'field2' => 5,
      ))
      ->execute();

    my_other_function($id);

    return $id;
  }
  catch (Exception $e) {
    // Something went wrong somewhere, so roll back now.
    $txn->rollback();
    // Log the exception to watchdog.
    watchdog_exception('type', $e);
  }

  // $txn goes out of scope here.  Unless the transaction was rolled back, it
  // gets automatically committed here.
}

function my_other_function($id) {
  // The transaction is still open here.

  if ($id % 2 == 0) {
    db_update('example')
      ->condition('id', $id)
      ->fields(array('field2' => 10))
      ->execute();
  }
}
@endcode

@see http://drupal.org/developing/api/database
```

## Members (derived, 501)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [db_and()](../includes/database/database.inc/db_and.md) (function) — Returns a new DatabaseCondition, set to "AND" all conditions together.
- [db_close()](../includes/database/database.inc/db_close.md) (function) — Closes the active database connection.
- [db_condition()](../includes/database/database.inc/db_condition.md) (function) — Returns a new DatabaseCondition, set to the specified conjunction.
- [db_delete()](../includes/database/database.inc/db_delete.md) (function) — Returns a new DeleteQuery object for the active database.
- [db_driver()](../includes/database/database.inc/db_driver.md) (function) — Retrieves the name of the currently active database driver.
- [db_escape_field()](../includes/database/database.inc/db_escape_field.md) (function) — Restricts a dynamic column or constraint name to safe characters.
- [db_escape_table()](../includes/database/database.inc/db_escape_table.md) (function) — Restricts a dynamic table name to safe characters.
- [db_insert()](../includes/database/database.inc/db_insert.md) (function) — Returns a new InsertQuery object for the active database.
- [db_like()](../includes/database/database.inc/db_like.md) (function) — Escapes characters that work as wildcard characters in a LIKE pattern.
- [db_merge()](../includes/database/database.inc/db_merge.md) (function) — Returns a new MergeQuery object for the active database.
- [db_next_id()](../includes/database/database.inc/db_next_id.md) (function) — Retrieves a unique id.
- [db_or()](../includes/database/database.inc/db_or.md) (function) — Returns a new DatabaseCondition, set to "OR" all conditions together.
- [db_query()](../includes/database/database.inc/db_query.md) (function) — Executes an arbitrary query string against the active database.
- [db_query_range()](../includes/database/database.inc/db_query_range.md) (function) — Executes a query against the active database, restricted to a range.
- [db_query_temporary()](../includes/database/database.inc/db_query_temporary.md) (function) — Executes a SELECT query string and saves the result set to a temporary table.
- [db_select()](../includes/database/database.inc/db_select.md) (function) — Returns a new SelectQuery object for the active database.
- [db_set_active()](../includes/database/database.inc/db_set_active.md) (function) — Sets a new active database.
- [db_transaction()](../includes/database/database.inc/db_transaction.md) (function) — Returns a new transaction object for the active database.
- [db_truncate()](../includes/database/database.inc/db_truncate.md) (function) — Returns a new TruncateQuery object for the active database.
- [db_update()](../includes/database/database.inc/db_update.md) (function) — Returns a new UpdateQuery object for the active database.
- [db_xor()](../includes/database/database.inc/db_xor.md) (function) — Returns a new DatabaseCondition, set to "XOR" all conditions together.
- [POSTGRESQL_NEXTID_LOCK](../includes/database/pgsql/database.inc/_file.md#postgresql_nextid_lock) (constant) — The name by which to obtain a lock for retrieving the next insert id.
- [Database](../includes/database/database.inc/Database.md) (class) — Primary front-controller for the database system.
- [DatabaseCondition](../includes/database/query.inc/DatabaseCondition.md) (class) — Generic class for a series of conditions in a query.
- [DatabaseConnection](../includes/database/database.inc/DatabaseConnection.md) (class) — Base Database API class.
- [DatabaseConnectionNotDefinedException](../includes/database/database.inc/DatabaseConnectionNotDefinedException.md) (class) — Exception thrown if an undefined database connection is requested.
- [DatabaseConnection_mysql](../includes/database/mysql/database.inc/DatabaseConnection_mysql.md) (class)
- [DatabaseConnection_pgsql](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql.md) (class)
- [DatabaseConnection_sqlite](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite.md) (class) — Specific SQLite implementation of DatabaseConnection.
- [DatabaseDriverNotSpecifiedException](../includes/database/database.inc/DatabaseDriverNotSpecifiedException.md) (class) — Exception thrown if no driver is specified for a database connection.
- [DatabaseStatementBase](../includes/database/database.inc/DatabaseStatementBase.md) (class) — Default implementation of DatabaseStatementInterface.
- [DatabaseStatementEmpty](../includes/database/database.inc/DatabaseStatementEmpty.md) (class) — Empty implementation of a database statement.
- [DatabaseStatementInterface](../includes/database/database.inc/DatabaseStatementInterface.md) (interface) — Represents a prepared statement.
- [DatabaseStatementPrefetch](../includes/database/prefetch.inc/DatabaseStatementPrefetch.md) (class) — An implementation of DatabaseStatementInterface that prefetches all data.
- [DatabaseStatement_sqlite](../includes/database/sqlite/database.inc/DatabaseStatement_sqlite.md) (class) — Specific SQLite implementation of DatabaseConnection.
- [DatabaseTransaction](../includes/database/database.inc/DatabaseTransaction.md) (class) — A wrapper class for creating and managing database transactions.
- [DatabaseTransactionCommitFailedException](../includes/database/database.inc/DatabaseTransactionCommitFailedException.md) (class) — Exception thrown when a commit() function fails.
- [DatabaseTransactionExplicitCommitNotAllowedException](../includes/database/database.inc/DatabaseTransactionExplicitCommitNotAllowedException.md) (class) — Exception to deny attempts to explicitly manage transactions.
- [DatabaseTransactionNameNonUniqueException](../includes/database/database.inc/DatabaseTransactionNameNonUniqueException.md) (class) — Exception thrown when a savepoint or transaction name occurs twice.
- [DatabaseTransactionNoActiveException](../includes/database/database.inc/DatabaseTransactionNoActiveException.md) (class) — Exception for when popTransaction() is called with no active transaction.
- [DatabaseTransactionOutOfOrderException](../includes/database/database.inc/DatabaseTransactionOutOfOrderException.md) (class) — Exception thrown when a rollback() resulted in other active transactions being rolled-back.
- [DeleteQuery](../includes/database/query.inc/DeleteQuery.md) (class) — General class for an abstracted DELETE operation.
- [DeleteQuery_sqlite](../includes/database/sqlite/query.inc/DeleteQuery_sqlite.md) (class) — SQLite specific implementation of DeleteQuery.
- [FieldsOverlapException](../includes/database/database.inc/FieldsOverlapException.md) (class) — Exception thrown if an insert query specifies a field twice.
- [InsertQuery](../includes/database/query.inc/InsertQuery.md) (class) — General class for an abstracted INSERT query.
- [InsertQuery_mysql](../includes/database/mysql/query.inc/InsertQuery_mysql.md) (class)
- [InsertQuery_sqlite](../includes/database/sqlite/query.inc/InsertQuery_sqlite.md) (class) — SQLite specific implementation of InsertQuery.
- [InvalidMergeQueryException](../includes/database/database.inc/InvalidMergeQueryException.md) (class) — Exception thrown for merge queries that do not make semantic sense.
- [InvalidQueryConditionOperatorException](../includes/database/database.inc/InvalidQueryConditionOperatorException.md) (class) — Exception thrown if an invalid query condition is specified.
- [MergeQuery](../includes/database/query.inc/MergeQuery.md) (class) — General class for an abstracted MERGE query operation.
- [NoFieldsException](../includes/database/database.inc/NoFieldsException.md) (class) — Exception thrown if an insert query doesn't specify insert or default fields.
- [Query](../includes/database/query.inc/Query.md) (class) — Base class for query builders.
- [QueryAlterableInterface](../includes/database/query.inc/QueryAlterableInterface.md) (interface) — Interface for a query that can be manipulated via an alter hook.
- [QueryConditionInterface](../includes/database/query.inc/QueryConditionInterface.md) (interface) — Interface for a conditional clause in a query.
- [QueryExtendableInterface](../includes/database/select.inc/QueryExtendableInterface.md) (interface) — Interface for extendable query objects.
- [QueryPlaceholderInterface](../includes/database/query.inc/QueryPlaceholderInterface.md) (interface) — Interface for a query that accepts placeholders.
- [SelectQuery](../includes/database/select.inc/SelectQuery.md) (class) — Query builder for SELECT statements.
- [SelectQueryExtender](../includes/database/select.inc/SelectQueryExtender.md) (class) — The base extender class for Select queries.
- [SelectQueryInterface](../includes/database/select.inc/SelectQueryInterface.md) (interface) — Interface definition for a Select Query object.
- [SelectQuery_pgsql](../includes/database/pgsql/select.inc/SelectQuery_pgsql.md) (class)
- [SelectQuery_sqlite](../includes/database/sqlite/select.inc/SelectQuery_sqlite.md) (class) — SQLite specific query builder for SELECT statements.
- [TruncateQuery](../includes/database/query.inc/TruncateQuery.md) (class) — General class for an abstracted TRUNCATE operation.
- [TruncateQuery_mysql](../includes/database/mysql/query.inc/TruncateQuery_mysql.md) (class)
- [TruncateQuery_sqlite](../includes/database/sqlite/query.inc/TruncateQuery_sqlite.md) (class) — SQLite specific implementation of TruncateQuery.
- [UpdateQuery](../includes/database/query.inc/UpdateQuery.md) (class) — General class for an abstracted UPDATE operation.
- [UpdateQuery_mysql](../includes/database/mysql/query.inc/UpdateQuery_mysql.md) (class)
- [UpdateQuery_sqlite](../includes/database/sqlite/query.inc/UpdateQuery_sqlite.md) (class) — SQLite specific implementation of UpdateQuery.
- [Database::addConnectionInfo()](../includes/database/database.inc/Database/addConnectionInfo.md) (method) — Adds database connection information for a given key/target.
- [Database::closeConnection()](../includes/database/database.inc/Database/closeConnection.md) (method) — Closes a connection to the server specified by the given key and target.
- [Database::getConnection()](../includes/database/database.inc/Database/getConnection.md) (method) — Gets the connection object for the specified database key and target.
- [Database::getConnectionInfo()](../includes/database/database.inc/Database/getConnectionInfo.md) (method) — Gets information on the specified database connection.
- [Database::getLog()](../includes/database/database.inc/Database/getLog.md) (method) — Retrieves the queries logged on for given logging key.
- [Database::ignoreTarget()](../includes/database/database.inc/Database/ignoreTarget.md) (method) — Instructs the system to temporarily ignore a given key/target.
- [Database::isActiveConnection()](../includes/database/database.inc/Database/isActiveConnection.md) (method) — Determines if there is an active connection.
- [Database::loadDriverFile()](../includes/database/database.inc/Database/loadDriverFile.md) (method) — Load a file for the database that might hold a class.
- [Database::openConnection()](../includes/database/database.inc/Database/openConnection.md) (method) — Opens a connection to the server specified by the given key and target.
- [Database::parseConnectionInfo()](../includes/database/database.inc/Database/parseConnectionInfo.md) (method) — Process the configuration file for database information.
- [Database::removeConnection()](../includes/database/database.inc/Database/removeConnection.md) (method) — Remove a connection and its corresponding connection information.
- [Database::renameConnection()](../includes/database/database.inc/Database/renameConnection.md) (method) — Rename a connection and its corresponding connection information.
- [Database::setActiveConnection()](../includes/database/database.inc/Database/setActiveConnection.md) (method) — Sets the active connection to the specified key.
- [Database::startLog()](../includes/database/database.inc/Database/startLog.md) (method) — Starts logging a given logging key on the specified connection.
- [DatabaseCondition::__clone()](../includes/database/query.inc/DatabaseCondition/__clone.md) (method) — PHP magic __clone() method.
- [DatabaseCondition::__construct()](../includes/database/query.inc/DatabaseCondition/__construct.md) (method) — Constructs a DataBaseCondition object.
- [DatabaseCondition::__toString()](../includes/database/query.inc/DatabaseCondition/__toString.md) (method) — Implements PHP magic __toString method to convert the conditions to string.
- [DatabaseCondition::arguments()](../includes/database/query.inc/DatabaseCondition/arguments.md) (method) — Implements QueryConditionInterface::arguments().
- [DatabaseCondition::compile()](../includes/database/query.inc/DatabaseCondition/compile.md) (method) — Implements QueryConditionInterface::compile().
- [DatabaseCondition::compiled()](../includes/database/query.inc/DatabaseCondition/compiled.md) (method) — Implements QueryConditionInterface::compiled().
- [DatabaseCondition::condition()](../includes/database/query.inc/DatabaseCondition/condition.md) (method) — Implements QueryConditionInterface::condition().
- [DatabaseCondition::conditions()](../includes/database/query.inc/DatabaseCondition/conditions.md) (method) — Implements QueryConditionInterface::conditions().
- [DatabaseCondition::count()](../includes/database/query.inc/DatabaseCondition/count.md) (method)
- [DatabaseCondition::exists()](../includes/database/query.inc/DatabaseCondition/exists.md) (method) — Implements QueryConditionInterface::exists().
- [DatabaseCondition::isNotNull()](../includes/database/query.inc/DatabaseCondition/isNotNull.md) (method) — Implements QueryConditionInterface::isNotNull().
- [DatabaseCondition::isNull()](../includes/database/query.inc/DatabaseCondition/isNull.md) (method) — Implements QueryConditionInterface::isNull().
- [DatabaseCondition::mapConditionOperator()](../includes/database/query.inc/DatabaseCondition/mapConditionOperator.md) (method) — Gets any special processing requirements for the condition operator.
- [DatabaseCondition::notExists()](../includes/database/query.inc/DatabaseCondition/notExists.md) (method) — Implements QueryConditionInterface::notExists().
- [DatabaseCondition::where()](../includes/database/query.inc/DatabaseCondition/where.md) (method) — Implements QueryConditionInterface::where().
- [DatabaseConnection::__call()](../includes/database/database.inc/DatabaseConnection/__call.md) (method) — Proxy possible direct calls to the \PDO methods.
- [DatabaseConnection::__construct()](../includes/database/database.inc/DatabaseConnection/__construct.md) (method)
- [DatabaseConnection::commit()](../includes/database/database.inc/DatabaseConnection/commit.md) (method) — Throws an exception to deny direct access to transaction commits.
- [DatabaseConnection::databaseType()](../includes/database/database.inc/DatabaseConnection/databaseType.md) (method) — Returns the name of the PDO driver for this connection.
- [DatabaseConnection::defaultOptions()](../includes/database/database.inc/DatabaseConnection/defaultOptions.md) (method) — Returns the default query options for any given query.
- [DatabaseConnection::delete()](../includes/database/database.inc/DatabaseConnection/delete.md) (method) — Prepares and returns a DELETE query object.
- [DatabaseConnection::destroy()](../includes/database/database.inc/DatabaseConnection/destroy.md) (method) — Destroys this Connection object.
- [DatabaseConnection::driver()](../includes/database/database.inc/DatabaseConnection/driver.md) (method) — Returns the type of database driver.
- [DatabaseConnection::escapeAlias()](../includes/database/database.inc/DatabaseConnection/escapeAlias.md) (method) — Escapes an alias name string.
- [DatabaseConnection::escapeField()](../includes/database/database.inc/DatabaseConnection/escapeField.md) (method) — Escapes a field name string.
- [DatabaseConnection::escapeLike()](../includes/database/database.inc/DatabaseConnection/escapeLike.md) (method) — Escapes characters that work as wildcard characters in a LIKE pattern.
- [DatabaseConnection::escapeTable()](../includes/database/database.inc/DatabaseConnection/escapeTable.md) (method) — Escapes a table name string.
- [DatabaseConnection::expandArguments()](../includes/database/database.inc/DatabaseConnection/expandArguments.md) (method) — Expands out shorthand placeholders.
- [DatabaseConnection::filterComment()](../includes/database/database.inc/DatabaseConnection/filterComment.md) (method) — Sanitize a query comment string.
- [DatabaseConnection::generateTemporaryTableName()](../includes/database/database.inc/DatabaseConnection/generateTemporaryTableName.md) (method) — Generates a temporary table name.
- [DatabaseConnection::getConnectionOptions()](../includes/database/database.inc/DatabaseConnection/getConnectionOptions.md) (method) — Returns the connection information for this connection object.
- [DatabaseConnection::getDriverClass()](../includes/database/database.inc/DatabaseConnection/getDriverClass.md) (method) — Gets the driver-specific override class if any for the specified class.
- [DatabaseConnection::getKey()](../includes/database/database.inc/DatabaseConnection/getKey.md) (method) — Returns the key this connection is associated with.
- [DatabaseConnection::getLogger()](../includes/database/database.inc/DatabaseConnection/getLogger.md) (method) — Gets the current logging object for this connection.
- [DatabaseConnection::getTarget()](../includes/database/database.inc/DatabaseConnection/getTarget.md) (method) — Returns the target this connection is associated with.
- [DatabaseConnection::getUnprefixedTablesMap()](../includes/database/database.inc/DatabaseConnection/getUnprefixedTablesMap.md) (method) — Gets a list of individually prefixed table names.
- [DatabaseConnection::inTransaction()](../includes/database/database.inc/DatabaseConnection/inTransaction.md) (method) — Determines if there is an active transaction open.
- [DatabaseConnection::insert()](../includes/database/database.inc/DatabaseConnection/insert.md) (method) — Prepares and returns an INSERT query object.
- [DatabaseConnection::makeComment()](../includes/database/database.inc/DatabaseConnection/makeComment.md) (method) — Flatten an array of query comments into a single comment string.
- [DatabaseConnection::makeSequenceName()](../includes/database/database.inc/DatabaseConnection/makeSequenceName.md) (method) — Creates the appropriate sequence name for a given table and serial field.
- [DatabaseConnection::mapConditionOperator()](../includes/database/database.inc/DatabaseConnection/mapConditionOperator.md) (method) — Gets any special processing requirements for the condition operator.
- [DatabaseConnection::merge()](../includes/database/database.inc/DatabaseConnection/merge.md) (method) — Prepares and returns a MERGE query object.
- [DatabaseConnection::nextId()](../includes/database/database.inc/DatabaseConnection/nextId.md) (method) — Retrieves an unique id from a given sequence.
- [DatabaseConnection::popCommittableTransactions()](../includes/database/database.inc/DatabaseConnection/popCommittableTransactions.md) (method) — Internal function: commit all the transaction layers that can commit.
- [DatabaseConnection::popTransaction()](../includes/database/database.inc/DatabaseConnection/popTransaction.md) (method) — Decreases the depth of transaction nesting.
- [DatabaseConnection::prefixTables()](../includes/database/database.inc/DatabaseConnection/prefixTables.md) (method) — Appends a database prefix to all tables in a query.
- [DatabaseConnection::prepareQuery()](../includes/database/database.inc/DatabaseConnection/prepareQuery.md) (method) — Prepares a query string and returns the prepared statement.
- [DatabaseConnection::pushTransaction()](../includes/database/database.inc/DatabaseConnection/pushTransaction.md) (method) — Increases the depth of transaction nesting.
- [DatabaseConnection::query()](../includes/database/database.inc/DatabaseConnection/query.md) (method) — Executes a query string against the database.
- [DatabaseConnection::queryRange()](../includes/database/database.inc/DatabaseConnection/queryRange.md) (method) — Runs a limited-range query on this database object.
- [DatabaseConnection::queryTemporary()](../includes/database/database.inc/DatabaseConnection/queryTemporary.md) (method) — Runs a SELECT query and stores its results in a temporary table.
- [DatabaseConnection::rollback()](../includes/database/database.inc/DatabaseConnection/rollback.md) (method) — Rolls back the transaction entirely or to a named savepoint.
- [DatabaseConnection::schema()](../includes/database/database.inc/DatabaseConnection/schema.md) (method) — Returns a DatabaseSchema object for manipulating the schema.
- [DatabaseConnection::select()](../includes/database/database.inc/DatabaseConnection/select.md) (method) — Prepares and returns a SELECT query object.
- [DatabaseConnection::setKey()](../includes/database/database.inc/DatabaseConnection/setKey.md) (method) — Tells this connection object what its key is.
- [DatabaseConnection::setLogger()](../includes/database/database.inc/DatabaseConnection/setLogger.md) (method) — Associates a logging object with this connection.
- [DatabaseConnection::setPrefix()](../includes/database/database.inc/DatabaseConnection/setPrefix.md) (method) — Set the list of prefixes used by this database connection.
- [DatabaseConnection::setTarget()](../includes/database/database.inc/DatabaseConnection/setTarget.md) (method) — Tells this connection object what its target value is.
- [DatabaseConnection::startTransaction()](../includes/database/database.inc/DatabaseConnection/startTransaction.md) (method) — Returns a new DatabaseTransaction object on this connection.
- [DatabaseConnection::supportsTransactionalDDL()](../includes/database/database.inc/DatabaseConnection/supportsTransactionalDDL.md) (method) — Determines if this driver supports transactional DDL.
- [DatabaseConnection::supportsTransactions()](../includes/database/database.inc/DatabaseConnection/supportsTransactions.md) (method) — Determines if this driver supports transactions.
- [DatabaseConnection::tablePrefix()](../includes/database/database.inc/DatabaseConnection/tablePrefix.md) (method) — Find the prefix for a table.
- [DatabaseConnection::transactionDepth()](../includes/database/database.inc/DatabaseConnection/transactionDepth.md) (method) — Determines current transaction depth.
- [DatabaseConnection::truncate()](../includes/database/database.inc/DatabaseConnection/truncate.md) (method) — Prepares and returns a TRUNCATE query object.
- [DatabaseConnection::update()](../includes/database/database.inc/DatabaseConnection/update.md) (method) — Prepares and returns an UPDATE query object.
- [DatabaseConnection::utf8mb4IsActive()](../includes/database/database.inc/DatabaseConnection/utf8mb4IsActive.md) (method) — Checks whether utf8mb4 support is currently active.
- [DatabaseConnection::utf8mb4IsConfigurable()](../includes/database/database.inc/DatabaseConnection/utf8mb4IsConfigurable.md) (method) — Checks whether utf8mb4 support is configurable in settings.php.
- [DatabaseConnection::utf8mb4IsSupported()](../includes/database/database.inc/DatabaseConnection/utf8mb4IsSupported.md) (method) — Checks whether utf8mb4 support is available on the current database system.
- [DatabaseConnection::version()](../includes/database/database.inc/DatabaseConnection/version.md) (method) — Returns the version of the database server.
- [DatabaseConnection_mysql::__construct()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/__construct.md) (method)
- [DatabaseConnection_mysql::__destruct()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/__destruct.md) (method)
- [DatabaseConnection_mysql::databaseType()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/databaseType.md) (method)
- [DatabaseConnection_mysql::doCommit()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/doCommit.md) (method) — Do the actual commit, including a workaround for PHP 8 behaviour changes.
- [DatabaseConnection_mysql::driver()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/driver.md) (method)
- [DatabaseConnection_mysql::escapeAlias()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/escapeAlias.md) (method) — {@inheritdoc}
- [DatabaseConnection_mysql::escapeField()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/escapeField.md) (method) — {@inheritdoc}
- [DatabaseConnection_mysql::escapeFields()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/escapeFields.md) (method)
- [DatabaseConnection_mysql::mapConditionOperator()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/mapConditionOperator.md) (method)
- [DatabaseConnection_mysql::nextId()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/nextId.md) (method)
- [DatabaseConnection_mysql::nextIdDelete()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/nextIdDelete.md) (method)
- [DatabaseConnection_mysql::popCommittableTransactions()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/popCommittableTransactions.md) (method) — Overridden to work around issues to MySQL not supporting transactional DDL.
- [DatabaseConnection_mysql::queryRange()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/queryRange.md) (method)
- [DatabaseConnection_mysql::queryTemporary()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/queryTemporary.md) (method)
- [DatabaseConnection_mysql::quoteIdentifier()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/quoteIdentifier.md) (method) — Quotes an identifier if it matches a MySQL reserved keyword.
- [DatabaseConnection_mysql::rollback()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/rollback.md) (method) — {@inheritdoc}
- [DatabaseConnection_mysql::setPrefix()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/setPrefix.md) (method) — {@inheritdoc}}
- [DatabaseConnection_mysql::utf8mb4IsActive()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/utf8mb4IsActive.md) (method)
- [DatabaseConnection_mysql::utf8mb4IsConfigurable()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/utf8mb4IsConfigurable.md) (method)
- [DatabaseConnection_mysql::utf8mb4IsSupported()](../includes/database/mysql/database.inc/DatabaseConnection_mysql/utf8mb4IsSupported.md) (method)
- [DatabaseConnection_pgsql::__construct()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/__construct.md) (method)
- [DatabaseConnection_pgsql::databaseType()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/databaseType.md) (method)
- [DatabaseConnection_pgsql::driver()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/driver.md) (method)
- [DatabaseConnection_pgsql::mapConditionOperator()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/mapConditionOperator.md) (method)
- [DatabaseConnection_pgsql::nextId()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/nextId.md) (method) — Retrieve the next id in a sequence.
- [DatabaseConnection_pgsql::prepareQuery()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/prepareQuery.md) (method)
- [DatabaseConnection_pgsql::query()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/query.md) (method)
- [DatabaseConnection_pgsql::queryRange()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/queryRange.md) (method)
- [DatabaseConnection_pgsql::queryTemporary()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/queryTemporary.md) (method)
- [DatabaseConnection_pgsql::utf8mb4IsActive()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/utf8mb4IsActive.md) (method)
- [DatabaseConnection_pgsql::utf8mb4IsSupported()](../includes/database/pgsql/database.inc/DatabaseConnection_pgsql/utf8mb4IsSupported.md) (method)
- [DatabaseConnection_sqlite::PDOPrepare()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/PDOPrepare.md) (method) — NEVER CALL THIS FUNCTION: YOU MIGHT DEADLOCK YOUR PHP PROCESS.
- [DatabaseConnection_sqlite::__construct()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/__construct.md) (method)
- [DatabaseConnection_sqlite::__destruct()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/__destruct.md) (method) — Destructor for the SQLite connection.
- [DatabaseConnection_sqlite::databaseType()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/databaseType.md) (method)
- [DatabaseConnection_sqlite::driver()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/driver.md) (method)
- [DatabaseConnection_sqlite::getAttachedDatabases()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/getAttachedDatabases.md) (method) — Gets all the attached databases.
- [DatabaseConnection_sqlite::mapConditionOperator()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/mapConditionOperator.md) (method)
- [DatabaseConnection_sqlite::nextId()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/nextId.md) (method)
- [DatabaseConnection_sqlite::popTransaction()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/popTransaction.md) (method)
- [DatabaseConnection_sqlite::prepare()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/prepare.md) (method) — SQLite-specific implementation of DatabaseConnection::prepare().
- [DatabaseConnection_sqlite::prepareQuery()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/prepareQuery.md) (method)
- [DatabaseConnection_sqlite::pushTransaction()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/pushTransaction.md) (method)
- [DatabaseConnection_sqlite::queryRange()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/queryRange.md) (method)
- [DatabaseConnection_sqlite::queryTemporary()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/queryTemporary.md) (method)
- [DatabaseConnection_sqlite::rollback()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/rollback.md) (method)
- [DatabaseConnection_sqlite::sqlFunctionConcat()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionConcat.md) (method) — SQLite compatibility implementation for the CONCAT() SQL function.
- [DatabaseConnection_sqlite::sqlFunctionGreatest()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionGreatest.md) (method) — SQLite compatibility implementation for the GREATEST() SQL function.
- [DatabaseConnection_sqlite::sqlFunctionIf()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionIf.md) (method) — SQLite compatibility implementation for the IF() SQL function.
- [DatabaseConnection_sqlite::sqlFunctionRand()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionRand.md) (method) — SQLite compatibility implementation for the RAND() SQL function.
- [DatabaseConnection_sqlite::sqlFunctionSubstring()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionSubstring.md) (method) — SQLite compatibility implementation for the SUBSTRING() SQL function.
- [DatabaseConnection_sqlite::sqlFunctionSubstringIndex()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/sqlFunctionSubstringIndex.md) (method) — SQLite compatibility implementation for the SUBSTRING_INDEX() SQL function.
- [DatabaseConnection_sqlite::utf8mb4IsActive()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/utf8mb4IsActive.md) (method)
- [DatabaseConnection_sqlite::utf8mb4IsSupported()](../includes/database/sqlite/database.inc/DatabaseConnection_sqlite/utf8mb4IsSupported.md) (method)
- [DatabaseStatementBase::__construct()](../includes/database/database.inc/DatabaseStatementBase/__construct.md) (method)
- [DatabaseStatementBase::execute()](../includes/database/database.inc/DatabaseStatementBase/execute.md) (method)
- [DatabaseStatementBase::fetchAllAssoc()](../includes/database/database.inc/DatabaseStatementBase/fetchAllAssoc.md) (method)
- [DatabaseStatementBase::fetchAllKeyed()](../includes/database/database.inc/DatabaseStatementBase/fetchAllKeyed.md) (method)
- [DatabaseStatementBase::fetchAssoc()](../includes/database/database.inc/DatabaseStatementBase/fetchAssoc.md) (method)
- [DatabaseStatementBase::fetchCol()](../includes/database/database.inc/DatabaseStatementBase/fetchCol.md) (method)
- [DatabaseStatementBase::fetchField()](../includes/database/database.inc/DatabaseStatementBase/fetchField.md) (method)
- [DatabaseStatementBase::getQueryString()](../includes/database/database.inc/DatabaseStatementBase/getQueryString.md) (method)
- [DatabaseStatementEmpty::current()](../includes/database/database.inc/DatabaseStatementEmpty/current.md) (method)
- [DatabaseStatementEmpty::execute()](../includes/database/database.inc/DatabaseStatementEmpty/execute.md) (method)
- [DatabaseStatementEmpty::fetch()](../includes/database/database.inc/DatabaseStatementEmpty/fetch.md) (method)
- [DatabaseStatementEmpty::fetchAll()](../includes/database/database.inc/DatabaseStatementEmpty/fetchAll.md) (method)
- [DatabaseStatementEmpty::fetchAllAssoc()](../includes/database/database.inc/DatabaseStatementEmpty/fetchAllAssoc.md) (method)
- [DatabaseStatementEmpty::fetchAllKeyed()](../includes/database/database.inc/DatabaseStatementEmpty/fetchAllKeyed.md) (method)
- [DatabaseStatementEmpty::fetchAssoc()](../includes/database/database.inc/DatabaseStatementEmpty/fetchAssoc.md) (method)
- [DatabaseStatementEmpty::fetchCol()](../includes/database/database.inc/DatabaseStatementEmpty/fetchCol.md) (method)
- [DatabaseStatementEmpty::fetchField()](../includes/database/database.inc/DatabaseStatementEmpty/fetchField.md) (method)
- [DatabaseStatementEmpty::fetchObject()](../includes/database/database.inc/DatabaseStatementEmpty/fetchObject.md) (method)
- [DatabaseStatementEmpty::getQueryString()](../includes/database/database.inc/DatabaseStatementEmpty/getQueryString.md) (method)
- [DatabaseStatementEmpty::key()](../includes/database/database.inc/DatabaseStatementEmpty/key.md) (method)
- [DatabaseStatementEmpty::next()](../includes/database/database.inc/DatabaseStatementEmpty/next.md) (method)
- [DatabaseStatementEmpty::rewind()](../includes/database/database.inc/DatabaseStatementEmpty/rewind.md) (method)
- [DatabaseStatementEmpty::rowCount()](../includes/database/database.inc/DatabaseStatementEmpty/rowCount.md) (method)
- [DatabaseStatementEmpty::setFetchMode()](../includes/database/database.inc/DatabaseStatementEmpty/setFetchMode.md) (method)
- [DatabaseStatementEmpty::valid()](../includes/database/database.inc/DatabaseStatementEmpty/valid.md) (method)
- [DatabaseStatementInterface::execute()](../includes/database/database.inc/DatabaseStatementInterface/execute.md) (method) — Executes a prepared statement
- [DatabaseStatementInterface::fetchAllAssoc()](../includes/database/database.inc/DatabaseStatementInterface/fetchAllAssoc.md) (method) — Returns the result set as an associative array keyed by the given field.
- [DatabaseStatementInterface::fetchAllKeyed()](../includes/database/database.inc/DatabaseStatementInterface/fetchAllKeyed.md) (method) — Returns the entire result set as a single associative array.
- [DatabaseStatementInterface::fetchAssoc()](../includes/database/database.inc/DatabaseStatementInterface/fetchAssoc.md) (method) — Fetches the next row and returns it as an associative array.
- [DatabaseStatementInterface::fetchCol()](../includes/database/database.inc/DatabaseStatementInterface/fetchCol.md) (method) — Returns an entire single column of a result set as an indexed array.
- [DatabaseStatementInterface::fetchField()](../includes/database/database.inc/DatabaseStatementInterface/fetchField.md) (method) — Returns a single field from the next record of a result set.
- [DatabaseStatementInterface::getQueryString()](../includes/database/database.inc/DatabaseStatementInterface/getQueryString.md) (method) — Gets the query string of this statement.
- [DatabaseStatementInterface::rowCount()](../includes/database/database.inc/DatabaseStatementInterface/rowCount.md) (method) — Returns the number of rows affected by the last SQL statement.
- [DatabaseStatementPrefetch::__construct()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/__construct.md) (method)
- [DatabaseStatementPrefetch::current()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/current.md) (method)
- [DatabaseStatementPrefetch::execute()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/execute.md) (method) — Executes a prepared statement.
- [DatabaseStatementPrefetch::fetch()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetch.md) (method)
- [DatabaseStatementPrefetch::fetchAll()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchAll.md) (method)
- [DatabaseStatementPrefetch::fetchAllAssoc()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchAllAssoc.md) (method)
- [DatabaseStatementPrefetch::fetchAllKeyed()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchAllKeyed.md) (method)
- [DatabaseStatementPrefetch::fetchAssoc()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchAssoc.md) (method)
- [DatabaseStatementPrefetch::fetchCol()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchCol.md) (method)
- [DatabaseStatementPrefetch::fetchColumn()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchColumn.md) (method)
- [DatabaseStatementPrefetch::fetchField()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchField.md) (method)
- [DatabaseStatementPrefetch::fetchObject()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/fetchObject.md) (method)
- [DatabaseStatementPrefetch::getQueryString()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/getQueryString.md) (method) — Return the object's SQL query string.
- [DatabaseStatementPrefetch::getStatement()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/getStatement.md) (method) — Grab a PDOStatement object from a given query and its arguments.
- [DatabaseStatementPrefetch::key()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/key.md) (method)
- [DatabaseStatementPrefetch::next()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/next.md) (method)
- [DatabaseStatementPrefetch::rewind()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/rewind.md) (method)
- [DatabaseStatementPrefetch::rowCount()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/rowCount.md) (method)
- [DatabaseStatementPrefetch::setFetchMode()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/setFetchMode.md) (method)
- [DatabaseStatementPrefetch::throwPDOException()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/throwPDOException.md) (method) — Throw a PDO Exception based on the last PDO error.
- [DatabaseStatementPrefetch::valid()](../includes/database/prefetch.inc/DatabaseStatementPrefetch/valid.md) (method)
- [DatabaseStatement_sqlite::execute()](../includes/database/sqlite/database.inc/DatabaseStatement_sqlite/execute.md) (method)
- [DatabaseStatement_sqlite::getStatement()](../includes/database/sqlite/database.inc/DatabaseStatement_sqlite/getStatement.md) (method) — SQLite specific implementation of getStatement().
- [DatabaseTransaction::__construct()](../includes/database/database.inc/DatabaseTransaction/__construct.md) (method)
- [DatabaseTransaction::__destruct()](../includes/database/database.inc/DatabaseTransaction/__destruct.md) (method)
- [DatabaseTransaction::name()](../includes/database/database.inc/DatabaseTransaction/name.md) (method) — Retrieves the name of the transaction or savepoint.
- [DatabaseTransaction::rollback()](../includes/database/database.inc/DatabaseTransaction/rollback.md) (method) — Rolls back the current transaction.
- [DeleteQuery::__construct()](../includes/database/query.inc/DeleteQuery/__construct.md) (method) — Constructs a DeleteQuery object.
- [DeleteQuery::__toString()](../includes/database/query.inc/DeleteQuery/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [DeleteQuery::arguments()](../includes/database/query.inc/DeleteQuery/arguments.md) (method) — Implements QueryConditionInterface::arguments().
- [DeleteQuery::compile()](../includes/database/query.inc/DeleteQuery/compile.md) (method) — Implements QueryConditionInterface::compile().
- [DeleteQuery::compiled()](../includes/database/query.inc/DeleteQuery/compiled.md) (method) — Implements QueryConditionInterface::compiled().
- [DeleteQuery::condition()](../includes/database/query.inc/DeleteQuery/condition.md) (method) — Implements QueryConditionInterface::condition().
- [DeleteQuery::conditions()](../includes/database/query.inc/DeleteQuery/conditions.md) (method) — Implements QueryConditionInterface::conditions().
- [DeleteQuery::execute()](../includes/database/query.inc/DeleteQuery/execute.md) (method) — Executes the DELETE query.
- [DeleteQuery::exists()](../includes/database/query.inc/DeleteQuery/exists.md) (method) — Implements QueryConditionInterface::exists().
- [DeleteQuery::isNotNull()](../includes/database/query.inc/DeleteQuery/isNotNull.md) (method) — Implements QueryConditionInterface::isNotNull().
- [DeleteQuery::isNull()](../includes/database/query.inc/DeleteQuery/isNull.md) (method) — Implements QueryConditionInterface::isNull().
- [DeleteQuery::notExists()](../includes/database/query.inc/DeleteQuery/notExists.md) (method) — Implements QueryConditionInterface::notExists().
- [DeleteQuery::where()](../includes/database/query.inc/DeleteQuery/where.md) (method) — Implements QueryConditionInterface::where().
- [DeleteQuery_sqlite::execute()](../includes/database/sqlite/query.inc/DeleteQuery_sqlite/execute.md) (method)
- [InsertQuery::__construct()](../includes/database/query.inc/InsertQuery/__construct.md) (method) — Constructs an InsertQuery object.
- [InsertQuery::__toString()](../includes/database/query.inc/InsertQuery/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [InsertQuery::execute()](../includes/database/query.inc/InsertQuery/execute.md) (method) — Executes the insert query.
- [InsertQuery::fields()](../includes/database/query.inc/InsertQuery/fields.md) (method) — Adds a set of field->value pairs to be inserted.
- [InsertQuery::from()](../includes/database/query.inc/InsertQuery/from.md) (method) — Sets the fromQuery on this InsertQuery object.
- [InsertQuery::preExecute()](../includes/database/query.inc/InsertQuery/preExecute.md) (method) — Preprocesses and validates the query.
- [InsertQuery::useDefaults()](../includes/database/query.inc/InsertQuery/useDefaults.md) (method) — Specifies fields for which the database defaults should be used.
- [InsertQuery::values()](../includes/database/query.inc/InsertQuery/values.md) (method) — Adds another set of values to the query to be inserted.
- [InsertQuery_mysql::__toString()](../includes/database/mysql/query.inc/InsertQuery_mysql/__toString.md) (method)
- [InsertQuery_mysql::execute()](../includes/database/mysql/query.inc/InsertQuery_mysql/execute.md) (method)
- [InsertQuery_sqlite::__toString()](../includes/database/sqlite/query.inc/InsertQuery_sqlite/__toString.md) (method)
- [InsertQuery_sqlite::execute()](../includes/database/sqlite/query.inc/InsertQuery_sqlite/execute.md) (method)
- [MergeQuery::__construct()](../includes/database/query.inc/MergeQuery/__construct.md) (method) — Constructs a MergeQuery object.
- [MergeQuery::__toString()](../includes/database/query.inc/MergeQuery/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [MergeQuery::arguments()](../includes/database/query.inc/MergeQuery/arguments.md) (method) — Implements QueryConditionInterface::arguments().
- [MergeQuery::compile()](../includes/database/query.inc/MergeQuery/compile.md) (method) — Implements QueryConditionInterface::compile().
- [MergeQuery::compiled()](../includes/database/query.inc/MergeQuery/compiled.md) (method) — Implements QueryConditionInterface::compiled().
- [MergeQuery::condition()](../includes/database/query.inc/MergeQuery/condition.md) (method) — Implements QueryConditionInterface::condition().
- [MergeQuery::conditionTable()](../includes/database/query.inc/MergeQuery/conditionTable.md) (method) — Sets the table or subquery to be used for the condition.
- [MergeQuery::conditions()](../includes/database/query.inc/MergeQuery/conditions.md) (method) — Implements QueryConditionInterface::conditions().
- [MergeQuery::execute()](../includes/database/query.inc/MergeQuery/execute.md) (method)
- [MergeQuery::exists()](../includes/database/query.inc/MergeQuery/exists.md) (method) — Implements QueryConditionInterface::exists().
- [MergeQuery::expression()](../includes/database/query.inc/MergeQuery/expression.md) (method) — Specifies fields to be updated as an expression.
- [MergeQuery::fields()](../includes/database/query.inc/MergeQuery/fields.md) (method) — Sets common field-value pairs in the INSERT and UPDATE query parts.
- [MergeQuery::insertFields()](../includes/database/query.inc/MergeQuery/insertFields.md) (method) — Adds a set of field->value pairs to be inserted.
- [MergeQuery::isNotNull()](../includes/database/query.inc/MergeQuery/isNotNull.md) (method) — Implements QueryConditionInterface::isNotNull().
- [MergeQuery::isNull()](../includes/database/query.inc/MergeQuery/isNull.md) (method) — Implements QueryConditionInterface::isNull().
- [MergeQuery::key()](../includes/database/query.inc/MergeQuery/key.md) (method) — Sets the key field(s) to be used as conditions for this query.
- [MergeQuery::notExists()](../includes/database/query.inc/MergeQuery/notExists.md) (method) — Implements QueryConditionInterface::notExists().
- [MergeQuery::updateFields()](../includes/database/query.inc/MergeQuery/updateFields.md) (method) — Adds a set of field->value pairs to be updated.
- [MergeQuery::useDefaults()](../includes/database/query.inc/MergeQuery/useDefaults.md) (method) — Specifies fields for which the database-defaults should be used.
- [MergeQuery::where()](../includes/database/query.inc/MergeQuery/where.md) (method) — Implements QueryConditionInterface::where().
- [Query::__clone()](../includes/database/query.inc/Query/__clone.md) (method) — Implements the magic __clone function.
- [Query::__construct()](../includes/database/query.inc/Query/__construct.md) (method) — Constructs a Query object.
- [Query::__sleep()](../includes/database/query.inc/Query/__sleep.md) (method) — Implements the magic __sleep function to disconnect from the database.
- [Query::__toString()](../includes/database/query.inc/Query/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [Query::__wakeup()](../includes/database/query.inc/Query/__wakeup.md) (method) — Implements the magic __wakeup function to reconnect to the database.
- [Query::comment()](../includes/database/query.inc/Query/comment.md) (method) — Adds a comment to the query.
- [Query::execute()](../includes/database/query.inc/Query/execute.md) (method) — Runs the query against the database.
- [Query::getComments()](../includes/database/query.inc/Query/getComments.md) (method) — Returns a reference to the comments array for the query.
- [Query::nextPlaceholder()](../includes/database/query.inc/Query/nextPlaceholder.md) (method) — Gets the next placeholder value for this query object.
- [Query::uniqueIdentifier()](../includes/database/query.inc/Query/uniqueIdentifier.md) (method) — Returns a unique identifier for this object.
- [QueryAlterableInterface::addMetaData()](../includes/database/query.inc/QueryAlterableInterface/addMetaData.md) (method) — Adds additional metadata to the query.
- [QueryAlterableInterface::addTag()](../includes/database/query.inc/QueryAlterableInterface/addTag.md) (method) — Adds a tag to a query.
- [QueryAlterableInterface::getMetaData()](../includes/database/query.inc/QueryAlterableInterface/getMetaData.md) (method) — Retrieves a given piece of metadata.
- [QueryAlterableInterface::hasAllTags()](../includes/database/query.inc/QueryAlterableInterface/hasAllTags.md) (method) — Determines if a given query has all specified tags.
- [QueryAlterableInterface::hasAnyTag()](../includes/database/query.inc/QueryAlterableInterface/hasAnyTag.md) (method) — Determines if a given query has any specified tag.
- [QueryAlterableInterface::hasTag()](../includes/database/query.inc/QueryAlterableInterface/hasTag.md) (method) — Determines if a given query has a given tag.
- [QueryConditionInterface::arguments()](../includes/database/query.inc/QueryConditionInterface/arguments.md) (method) — Gets a complete list of all values to insert into the prepared statement.
- [QueryConditionInterface::compile()](../includes/database/query.inc/QueryConditionInterface/compile.md) (method) — Compiles the saved conditions for later retrieval.
- [QueryConditionInterface::compiled()](../includes/database/query.inc/QueryConditionInterface/compiled.md) (method) — Check whether a condition has been previously compiled.
- [QueryConditionInterface::condition()](../includes/database/query.inc/QueryConditionInterface/condition.md) (method) — Helper function: builds the most common conditional clauses.
- [QueryConditionInterface::conditions()](../includes/database/query.inc/QueryConditionInterface/conditions.md) (method) — Gets a complete list of all conditions in this conditional clause.
- [QueryConditionInterface::exists()](../includes/database/query.inc/QueryConditionInterface/exists.md) (method) — Sets a condition that the specified subquery returns values.
- [QueryConditionInterface::isNotNull()](../includes/database/query.inc/QueryConditionInterface/isNotNull.md) (method) — Sets a condition that the specified field be NOT NULL.
- [QueryConditionInterface::isNull()](../includes/database/query.inc/QueryConditionInterface/isNull.md) (method) — Sets a condition that the specified field be NULL.
- [QueryConditionInterface::notExists()](../includes/database/query.inc/QueryConditionInterface/notExists.md) (method) — Sets a condition that the specified subquery returns no values.
- [QueryConditionInterface::where()](../includes/database/query.inc/QueryConditionInterface/where.md) (method) — Adds an arbitrary WHERE clause to the query.
- [QueryExtendableInterface::extend()](../includes/database/select.inc/QueryExtendableInterface/extend.md) (method) — Enhance this object by wrapping it in an extender object.
- [QueryPlaceholderInterface::nextPlaceholder()](../includes/database/query.inc/QueryPlaceholderInterface/nextPlaceholder.md) (method) — Returns the next placeholder ID for the query.
- [QueryPlaceholderInterface::uniqueIdentifier()](../includes/database/query.inc/QueryPlaceholderInterface/uniqueIdentifier.md) (method) — Returns a unique identifier for this object.
- [SelectQuery::__clone()](../includes/database/select.inc/SelectQuery/__clone.md) (method)
- [SelectQuery::__construct()](../includes/database/select.inc/SelectQuery/__construct.md) (method)
- [SelectQuery::__toString()](../includes/database/select.inc/SelectQuery/__toString.md) (method)
- [SelectQuery::addExpression()](../includes/database/select.inc/SelectQuery/addExpression.md) (method)
- [SelectQuery::addField()](../includes/database/select.inc/SelectQuery/addField.md) (method)
- [SelectQuery::addJoin()](../includes/database/select.inc/SelectQuery/addJoin.md) (method)
- [SelectQuery::addMetaData()](../includes/database/select.inc/SelectQuery/addMetaData.md) (method)
- [SelectQuery::addTag()](../includes/database/select.inc/SelectQuery/addTag.md) (method)
- [SelectQuery::arguments()](../includes/database/select.inc/SelectQuery/arguments.md) (method)
- [SelectQuery::compile()](../includes/database/select.inc/SelectQuery/compile.md) (method)
- [SelectQuery::compiled()](../includes/database/select.inc/SelectQuery/compiled.md) (method)
- [SelectQuery::condition()](../includes/database/select.inc/SelectQuery/condition.md) (method)
- [SelectQuery::conditions()](../includes/database/select.inc/SelectQuery/conditions.md) (method)
- [SelectQuery::countQuery()](../includes/database/select.inc/SelectQuery/countQuery.md) (method)
- [SelectQuery::distinct()](../includes/database/select.inc/SelectQuery/distinct.md) (method)
- [SelectQuery::execute()](../includes/database/select.inc/SelectQuery/execute.md) (method)
- [SelectQuery::exists()](../includes/database/select.inc/SelectQuery/exists.md) (method)
- [SelectQuery::extend()](../includes/database/select.inc/SelectQuery/extend.md) (method)
- [SelectQuery::fields()](../includes/database/select.inc/SelectQuery/fields.md) (method)
- [SelectQuery::forUpdate()](../includes/database/select.inc/SelectQuery/forUpdate.md) (method)
- [SelectQuery::getArguments()](../includes/database/select.inc/SelectQuery/getArguments.md) (method)
- [SelectQuery::getExpressions()](../includes/database/select.inc/SelectQuery/getExpressions.md) (method)
- [SelectQuery::getFields()](../includes/database/select.inc/SelectQuery/getFields.md) (method)
- [SelectQuery::getGroupBy()](../includes/database/select.inc/SelectQuery/getGroupBy.md) (method)
- [SelectQuery::getMetaData()](../includes/database/select.inc/SelectQuery/getMetaData.md) (method)
- [SelectQuery::getOrderBy()](../includes/database/select.inc/SelectQuery/getOrderBy.md) (method)
- [SelectQuery::getTables()](../includes/database/select.inc/SelectQuery/getTables.md) (method)
- [SelectQuery::getUnion()](../includes/database/select.inc/SelectQuery/getUnion.md) (method)
- [SelectQuery::groupBy()](../includes/database/select.inc/SelectQuery/groupBy.md) (method)
- [SelectQuery::hasAllTags()](../includes/database/select.inc/SelectQuery/hasAllTags.md) (method)
- [SelectQuery::hasAnyTag()](../includes/database/select.inc/SelectQuery/hasAnyTag.md) (method)
- [SelectQuery::hasTag()](../includes/database/select.inc/SelectQuery/hasTag.md) (method)
- [SelectQuery::having()](../includes/database/select.inc/SelectQuery/having.md) (method)
- [SelectQuery::havingArguments()](../includes/database/select.inc/SelectQuery/havingArguments.md) (method)
- [SelectQuery::havingCompile()](../includes/database/select.inc/SelectQuery/havingCompile.md) (method)
- [SelectQuery::havingCondition()](../includes/database/select.inc/SelectQuery/havingCondition.md) (method)
- [SelectQuery::havingConditions()](../includes/database/select.inc/SelectQuery/havingConditions.md) (method)
- [SelectQuery::havingExists()](../includes/database/select.inc/SelectQuery/havingExists.md) (method)
- [SelectQuery::havingIsNotNull()](../includes/database/select.inc/SelectQuery/havingIsNotNull.md) (method)
- [SelectQuery::havingIsNull()](../includes/database/select.inc/SelectQuery/havingIsNull.md) (method)
- [SelectQuery::havingNotExists()](../includes/database/select.inc/SelectQuery/havingNotExists.md) (method)
- [SelectQuery::innerJoin()](../includes/database/select.inc/SelectQuery/innerJoin.md) (method)
- [SelectQuery::isNotNull()](../includes/database/select.inc/SelectQuery/isNotNull.md) (method)
- [SelectQuery::isNull()](../includes/database/select.inc/SelectQuery/isNull.md) (method)
- [SelectQuery::isPrepared()](../includes/database/select.inc/SelectQuery/isPrepared.md) (method) — Indicates if preExecute() has already been called on that object.
- [SelectQuery::join()](../includes/database/select.inc/SelectQuery/join.md) (method)
- [SelectQuery::leftJoin()](../includes/database/select.inc/SelectQuery/leftJoin.md) (method)
- [SelectQuery::notExists()](../includes/database/select.inc/SelectQuery/notExists.md) (method)
- [SelectQuery::orderBy()](../includes/database/select.inc/SelectQuery/orderBy.md) (method)
- [SelectQuery::orderRandom()](../includes/database/select.inc/SelectQuery/orderRandom.md) (method)
- [SelectQuery::preExecute()](../includes/database/select.inc/SelectQuery/preExecute.md) (method) — Generic preparation and validation for a SELECT query.
- [SelectQuery::range()](../includes/database/select.inc/SelectQuery/range.md) (method)
- [SelectQuery::rightJoin()](../includes/database/select.inc/SelectQuery/rightJoin.md) (method)
- [SelectQuery::union()](../includes/database/select.inc/SelectQuery/union.md) (method)
- [SelectQuery::where()](../includes/database/select.inc/SelectQuery/where.md) (method)
- [SelectQueryExtender::__call()](../includes/database/select.inc/SelectQueryExtender/__call.md) (method) — Magic override for undefined methods.
- [SelectQueryExtender::__clone()](../includes/database/select.inc/SelectQueryExtender/__clone.md) (method)
- [SelectQueryExtender::__construct()](../includes/database/select.inc/SelectQueryExtender/__construct.md) (method)
- [SelectQueryExtender::__toString()](../includes/database/select.inc/SelectQueryExtender/__toString.md) (method)
- [SelectQueryExtender::addExpression()](../includes/database/select.inc/SelectQueryExtender/addExpression.md) (method)
- [SelectQueryExtender::addField()](../includes/database/select.inc/SelectQueryExtender/addField.md) (method)
- [SelectQueryExtender::addJoin()](../includes/database/select.inc/SelectQueryExtender/addJoin.md) (method)
- [SelectQueryExtender::addMetaData()](../includes/database/select.inc/SelectQueryExtender/addMetaData.md) (method)
- [SelectQueryExtender::addTag()](../includes/database/select.inc/SelectQueryExtender/addTag.md) (method)
- [SelectQueryExtender::arguments()](../includes/database/select.inc/SelectQueryExtender/arguments.md) (method)
- [SelectQueryExtender::compile()](../includes/database/select.inc/SelectQueryExtender/compile.md) (method)
- [SelectQueryExtender::compiled()](../includes/database/select.inc/SelectQueryExtender/compiled.md) (method)
- [SelectQueryExtender::condition()](../includes/database/select.inc/SelectQueryExtender/condition.md) (method)
- [SelectQueryExtender::conditions()](../includes/database/select.inc/SelectQueryExtender/conditions.md) (method)
- [SelectQueryExtender::countQuery()](../includes/database/select.inc/SelectQueryExtender/countQuery.md) (method)
- [SelectQueryExtender::distinct()](../includes/database/select.inc/SelectQueryExtender/distinct.md) (method)
- [SelectQueryExtender::execute()](../includes/database/select.inc/SelectQueryExtender/execute.md) (method)
- [SelectQueryExtender::exists()](../includes/database/select.inc/SelectQueryExtender/exists.md) (method)
- [SelectQueryExtender::extend()](../includes/database/select.inc/SelectQueryExtender/extend.md) (method)
- [SelectQueryExtender::fields()](../includes/database/select.inc/SelectQueryExtender/fields.md) (method)
- [SelectQueryExtender::forUpdate()](../includes/database/select.inc/SelectQueryExtender/forUpdate.md) (method)
- [SelectQueryExtender::getArguments()](../includes/database/select.inc/SelectQueryExtender/getArguments.md) (method)
- [SelectQueryExtender::getExpressions()](../includes/database/select.inc/SelectQueryExtender/getExpressions.md) (method)
- [SelectQueryExtender::getFields()](../includes/database/select.inc/SelectQueryExtender/getFields.md) (method)
- [SelectQueryExtender::getGroupBy()](../includes/database/select.inc/SelectQueryExtender/getGroupBy.md) (method)
- [SelectQueryExtender::getMetaData()](../includes/database/select.inc/SelectQueryExtender/getMetaData.md) (method)
- [SelectQueryExtender::getOrderBy()](../includes/database/select.inc/SelectQueryExtender/getOrderBy.md) (method)
- [SelectQueryExtender::getTables()](../includes/database/select.inc/SelectQueryExtender/getTables.md) (method)
- [SelectQueryExtender::getUnion()](../includes/database/select.inc/SelectQueryExtender/getUnion.md) (method)
- [SelectQueryExtender::groupBy()](../includes/database/select.inc/SelectQueryExtender/groupBy.md) (method)
- [SelectQueryExtender::hasAllTags()](../includes/database/select.inc/SelectQueryExtender/hasAllTags.md) (method)
- [SelectQueryExtender::hasAnyTag()](../includes/database/select.inc/SelectQueryExtender/hasAnyTag.md) (method)
- [SelectQueryExtender::hasTag()](../includes/database/select.inc/SelectQueryExtender/hasTag.md) (method)
- [SelectQueryExtender::having()](../includes/database/select.inc/SelectQueryExtender/having.md) (method)
- [SelectQueryExtender::havingArguments()](../includes/database/select.inc/SelectQueryExtender/havingArguments.md) (method)
- [SelectQueryExtender::havingCompile()](../includes/database/select.inc/SelectQueryExtender/havingCompile.md) (method)
- [SelectQueryExtender::havingCondition()](../includes/database/select.inc/SelectQueryExtender/havingCondition.md) (method)
- [SelectQueryExtender::havingConditions()](../includes/database/select.inc/SelectQueryExtender/havingConditions.md) (method)
- [SelectQueryExtender::innerJoin()](../includes/database/select.inc/SelectQueryExtender/innerJoin.md) (method)
- [SelectQueryExtender::isNotNull()](../includes/database/select.inc/SelectQueryExtender/isNotNull.md) (method)
- [SelectQueryExtender::isNull()](../includes/database/select.inc/SelectQueryExtender/isNull.md) (method)
- [SelectQueryExtender::isPrepared()](../includes/database/select.inc/SelectQueryExtender/isPrepared.md) (method)
- [SelectQueryExtender::join()](../includes/database/select.inc/SelectQueryExtender/join.md) (method)
- [SelectQueryExtender::leftJoin()](../includes/database/select.inc/SelectQueryExtender/leftJoin.md) (method)
- [SelectQueryExtender::nextPlaceholder()](../includes/database/select.inc/SelectQueryExtender/nextPlaceholder.md) (method) — Implements QueryPlaceholderInterface::nextPlaceholder().
- [SelectQueryExtender::notExists()](../includes/database/select.inc/SelectQueryExtender/notExists.md) (method)
- [SelectQueryExtender::orderBy()](../includes/database/select.inc/SelectQueryExtender/orderBy.md) (method)
- [SelectQueryExtender::orderRandom()](../includes/database/select.inc/SelectQueryExtender/orderRandom.md) (method)
- [SelectQueryExtender::preExecute()](../includes/database/select.inc/SelectQueryExtender/preExecute.md) (method)
- [SelectQueryExtender::range()](../includes/database/select.inc/SelectQueryExtender/range.md) (method)
- [SelectQueryExtender::rightJoin()](../includes/database/select.inc/SelectQueryExtender/rightJoin.md) (method)
- [SelectQueryExtender::union()](../includes/database/select.inc/SelectQueryExtender/union.md) (method)
- [SelectQueryExtender::uniqueIdentifier()](../includes/database/select.inc/SelectQueryExtender/uniqueIdentifier.md) (method) — Implements QueryPlaceholderInterface::uniqueIdentifier().
- [SelectQueryExtender::where()](../includes/database/select.inc/SelectQueryExtender/where.md) (method)
- [SelectQueryInterface::__clone()](../includes/database/select.inc/SelectQueryInterface/__clone.md) (method) — Clone magic method.
- [SelectQueryInterface::addExpression()](../includes/database/select.inc/SelectQueryInterface/addExpression.md) (method) — Adds an expression to the list of "fields" to be SELECTed.
- [SelectQueryInterface::addField()](../includes/database/select.inc/SelectQueryInterface/addField.md) (method) — Adds a field to the list to be SELECTed.
- [SelectQueryInterface::addJoin()](../includes/database/select.inc/SelectQueryInterface/addJoin.md) (method) — Join against another table in the database.
- [SelectQueryInterface::countQuery()](../includes/database/select.inc/SelectQueryInterface/countQuery.md) (method) — Get the equivalent COUNT query of this query as a new query object.
- [SelectQueryInterface::distinct()](../includes/database/select.inc/SelectQueryInterface/distinct.md) (method) — Sets this query to be DISTINCT.
- [SelectQueryInterface::fields()](../includes/database/select.inc/SelectQueryInterface/fields.md) (method) — Add multiple fields from the same table to be SELECTed.
- [SelectQueryInterface::forUpdate()](../includes/database/select.inc/SelectQueryInterface/forUpdate.md) (method) — Add FOR UPDATE to the query.
- [SelectQueryInterface::getArguments()](../includes/database/select.inc/SelectQueryInterface/getArguments.md) (method) — Compiles and returns an associative array of the arguments for this prepared statement.
- [SelectQueryInterface::getExpressions()](../includes/database/select.inc/SelectQueryInterface/getExpressions.md) (method) — Returns a reference to the expressions array for this query.
- [SelectQueryInterface::getFields()](../includes/database/select.inc/SelectQueryInterface/getFields.md) (method) — Returns a reference to the fields array for this query.
- [SelectQueryInterface::getGroupBy()](../includes/database/select.inc/SelectQueryInterface/getGroupBy.md) (method) — Returns a reference to the group-by array for this query.
- [SelectQueryInterface::getOrderBy()](../includes/database/select.inc/SelectQueryInterface/getOrderBy.md) (method) — Returns a reference to the order by array for this query.
- [SelectQueryInterface::getTables()](../includes/database/select.inc/SelectQueryInterface/getTables.md) (method) — Returns a reference to the tables array for this query.
- [SelectQueryInterface::getUnion()](../includes/database/select.inc/SelectQueryInterface/getUnion.md) (method) — Returns a reference to the union queries for this query. This include queries for UNION, UNION ALL, and UNION DISTINCT.
- [SelectQueryInterface::groupBy()](../includes/database/select.inc/SelectQueryInterface/groupBy.md) (method) — Groups the result set by the specified field.
- [SelectQueryInterface::havingCondition()](../includes/database/select.inc/SelectQueryInterface/havingCondition.md) (method) — Helper function to build most common HAVING conditional clauses.
- [SelectQueryInterface::innerJoin()](../includes/database/select.inc/SelectQueryInterface/innerJoin.md) (method) — Inner Join against another table in the database.
- [SelectQueryInterface::isPrepared()](../includes/database/select.inc/SelectQueryInterface/isPrepared.md) (method) — Indicates if preExecute() has already been called on that object.
- [SelectQueryInterface::join()](../includes/database/select.inc/SelectQueryInterface/join.md) (method) — Default Join against another table in the database.
- [SelectQueryInterface::leftJoin()](../includes/database/select.inc/SelectQueryInterface/leftJoin.md) (method) — Left Outer Join against another table in the database.
- [SelectQueryInterface::orderBy()](../includes/database/select.inc/SelectQueryInterface/orderBy.md) (method) — Orders the result set by a given field.
- [SelectQueryInterface::orderRandom()](../includes/database/select.inc/SelectQueryInterface/orderRandom.md) (method) — Orders the result set by a random value.
- [SelectQueryInterface::preExecute()](../includes/database/select.inc/SelectQueryInterface/preExecute.md) (method) — Generic preparation and validation for a SELECT query.
- [SelectQueryInterface::range()](../includes/database/select.inc/SelectQueryInterface/range.md) (method) — Restricts a query to a given range in the result set.
- [SelectQueryInterface::rightJoin()](../includes/database/select.inc/SelectQueryInterface/rightJoin.md) (method) — Right Outer Join against another table in the database.
- [SelectQueryInterface::union()](../includes/database/select.inc/SelectQueryInterface/union.md) (method) — Add another Select query to UNION to this one.
- [SelectQuery_pgsql::orderBy()](../includes/database/pgsql/select.inc/SelectQuery_pgsql/orderBy.md) (method) — Overrides SelectQuery::orderBy().
- [SelectQuery_pgsql::orderRandom()](../includes/database/pgsql/select.inc/SelectQuery_pgsql/orderRandom.md) (method)
- [SelectQuery_sqlite::forUpdate()](../includes/database/sqlite/select.inc/SelectQuery_sqlite/forUpdate.md) (method)
- [TruncateQuery::__construct()](../includes/database/query.inc/TruncateQuery/__construct.md) (method) — Constructs a TruncateQuery object.
- [TruncateQuery::__toString()](../includes/database/query.inc/TruncateQuery/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [TruncateQuery::compile()](../includes/database/query.inc/TruncateQuery/compile.md) (method) — Implements QueryConditionInterface::compile().
- [TruncateQuery::compiled()](../includes/database/query.inc/TruncateQuery/compiled.md) (method) — Implements QueryConditionInterface::compiled().
- [TruncateQuery::execute()](../includes/database/query.inc/TruncateQuery/execute.md) (method) — Executes the TRUNCATE query.
- [TruncateQuery_sqlite::__toString()](../includes/database/sqlite/query.inc/TruncateQuery_sqlite/__toString.md) (method)
- [UpdateQuery::__construct()](../includes/database/query.inc/UpdateQuery/__construct.md) (method) — Constructs an UpdateQuery object.
- [UpdateQuery::__toString()](../includes/database/query.inc/UpdateQuery/__toString.md) (method) — Implements PHP magic __toString method to convert the query to a string.
- [UpdateQuery::arguments()](../includes/database/query.inc/UpdateQuery/arguments.md) (method) — Implements QueryConditionInterface::arguments().
- [UpdateQuery::compile()](../includes/database/query.inc/UpdateQuery/compile.md) (method) — Implements QueryConditionInterface::compile().
- [UpdateQuery::compiled()](../includes/database/query.inc/UpdateQuery/compiled.md) (method) — Implements QueryConditionInterface::compiled().
- [UpdateQuery::condition()](../includes/database/query.inc/UpdateQuery/condition.md) (method) — Implements QueryConditionInterface::condition().
- [UpdateQuery::conditions()](../includes/database/query.inc/UpdateQuery/conditions.md) (method) — Implements QueryConditionInterface::conditions().
- [UpdateQuery::execute()](../includes/database/query.inc/UpdateQuery/execute.md) (method) — Executes the UPDATE query.
- [UpdateQuery::exists()](../includes/database/query.inc/UpdateQuery/exists.md) (method) — Implements QueryConditionInterface::exists().
- [UpdateQuery::expression()](../includes/database/query.inc/UpdateQuery/expression.md) (method) — Specifies fields to be updated as an expression.
- [UpdateQuery::fields()](../includes/database/query.inc/UpdateQuery/fields.md) (method) — Adds a set of field->value pairs to be updated.
- [UpdateQuery::isNotNull()](../includes/database/query.inc/UpdateQuery/isNotNull.md) (method) — Implements QueryConditionInterface::isNotNull().
- [UpdateQuery::isNull()](../includes/database/query.inc/UpdateQuery/isNull.md) (method) — Implements QueryConditionInterface::isNull().
- [UpdateQuery::notExists()](../includes/database/query.inc/UpdateQuery/notExists.md) (method) — Implements QueryConditionInterface::notExists().
- [UpdateQuery::where()](../includes/database/query.inc/UpdateQuery/where.md) (method) — Implements QueryConditionInterface::where().
- [UpdateQuery_mysql::__toString()](../includes/database/mysql/query.inc/UpdateQuery_mysql/__toString.md) (method)
- [UpdateQuery_sqlite::execute()](../includes/database/sqlite/query.inc/UpdateQuery_sqlite/execute.md) (method)

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
