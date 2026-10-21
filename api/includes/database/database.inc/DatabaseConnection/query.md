# DatabaseConnection::query()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 728–777 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L728-L777)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function query($query, array $args = array(), $options = array())
```

## Documentation

```text
Executes a query string against the database.

This method provides a central handler for the actual execution of every
query. All queries executed by Drupal are executed as PDO prepared
statements.

@param $query
  The query to execute. In most cases this will be a string containing
  an SQL query with placeholders. An already-prepared instance of
  DatabaseStatementInterface may also be passed in order to allow calling
  code to manually bind variables to a query. If a
  DatabaseStatementInterface is passed, the $args array will be ignored.
  It is extremely rare that module code will need to pass a statement
  object to this method. It is used primarily for database drivers for
  databases that require special LOB field handling.
@param $args
  An array of arguments for the prepared statement. If the prepared
  statement uses ? placeholders, this array must be an indexed array.
  If it contains named placeholders, it must be an associative array.
@param $options
  An associative array of options to control how the query is run. See
  the documentation for DatabaseConnection::defaultOptions() for details.

@return DatabaseStatementInterface
  This method will return one of: the executed statement, the number of
  rows affected by the query (not the number matched), or the generated
  insert ID of the last query, depending on the value of
  $options['return']. Typically that value will be set by default or a
  query builder and should not be set by a user. If there is an error,
  this method will return NULL and may throw an exception if
  $options['throw_exception'] is TRUE.

@throws PDOException
```

## Code

```php
  public function query($query, array $args = array(), $options = array()) {

    // Use default values if not already set.
    $options += $this->defaultOptions();

    try {
      // We allow either a pre-bound statement object or a literal string.
      // In either case, we want to end up with an executed statement object,
      // which we pass to PDOStatement::execute.
      if ($query instanceof DatabaseStatementInterface) {
        $stmt = $query;
        $stmt->execute(NULL, $options);
      }
      else {
        $this->expandArguments($query, $args);
        $stmt = $this->prepareQuery($query);
        $stmt->execute($args, $options);
      }

      // Depending on the type of query we may need to return a different value.
      // See DatabaseConnection::defaultOptions() for a description of each
      // value.
      switch ($options['return']) {
        case Database::RETURN_STATEMENT:
          return $stmt;
        case Database::RETURN_AFFECTED:
          return $stmt->rowCount();
        case Database::RETURN_INSERT_ID:
          return $this->connection->lastInsertId();
        case Database::RETURN_NULL:
          return;
        default:
          throw new PDOException('Invalid return directive: ' . $options['return']);
      }
    }
    catch (PDOException $e) {
      if ($options['throw_exception']) {
        // Add additional debug information.
        if ($query instanceof DatabaseStatementInterface) {
          $e->errorInfo['query_string'] = $stmt->getQueryString();
        }
        else {
          $e->errorInfo['query_string'] = $query;
        }
        $e->errorInfo['args'] = $args;
        throw $e;
      }
      return NULL;
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
