# DatabaseConnection::defaultOptions()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 419–426 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L419-L426)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function defaultOptions()
```

## Documentation

```text
Returns the default query options for any given query.

A given query can be customized with a number of option flags in an
associative array:
- target: The database "target" against which to execute a query. Valid
  values are "default" or "slave". The system will first try to open a
  connection to a database specified with the user-supplied key. If one
  is not available, it will silently fall back to the "default" target.
  If multiple databases connections are specified with the same target,
  one will be selected at random for the duration of the request.
- fetch: This element controls how rows from a result set will be
  returned. Legal values include PDO::FETCH_ASSOC, PDO::FETCH_BOTH,
  PDO::FETCH_OBJ, PDO::FETCH_NUM, or a string representing the name of a
  class. If a string is specified, each record will be fetched into a new
  object of that class. The behavior of all other values is defined by PDO.
  See http://php.net/manual/pdostatement.fetch.php
- return: Depending on the type of query, different return values may be
  meaningful. This directive instructs the system which type of return
  value is desired. The system will generally set the correct value
  automatically, so it is extremely rare that a module developer will ever
  need to specify this value. Setting it incorrectly will likely lead to
  unpredictable results or fatal errors. Legal values include:
  - Database::RETURN_STATEMENT: Return the prepared statement object for
    the query. This is usually only meaningful for SELECT queries, where
    the statement object is how one accesses the result set returned by the
    query.
  - Database::RETURN_AFFECTED: Return the number of rows affected by an
    UPDATE or DELETE query. Be aware that means the number of rows actually
    changed, not the number of rows matched by the WHERE clause.
  - Database::RETURN_INSERT_ID: Return the sequence ID (primary key)
    created by an INSERT statement on a table that contains a serial
    column.
  - Database::RETURN_NULL: Do not return anything, as there is no
    meaningful value to return. That is the case for INSERT queries on
    tables that do not contain a serial column.
- throw_exception: By default, the database system will catch any errors
  on a query as an Exception, log it, and then rethrow it so that code
  further up the call chain can take an appropriate action. To suppress
  that behavior and simply return NULL on failure, set this option to
  FALSE.

@return
  An array of default query options.
```

## Code

```php
  protected function defaultOptions() {
    return array(
      'target' => 'default',
      'fetch' => PDO::FETCH_OBJ,
      'return' => Database::RETURN_STATEMENT,
      'throw_exception' => TRUE,
    );
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
