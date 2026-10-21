# DatabaseStatementPrefetch::execute()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 144–199 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L144-L199)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute($args = array(), $options = array())
```

## Documentation

```text
Executes a prepared statement.

@param $args
  An array of values with as many elements as there are bound parameters in the SQL statement being executed.
@param $options
  An array of options for this query.
@return
  TRUE on success, or FALSE on failure.
```

## Code

```php
  public function execute($args = array(), $options = array()) {
    if (isset($options['fetch'])) {
      if (is_string($options['fetch'])) {
        // Default to an object. Note: db fields will be added to the object
        // before the constructor is run. If you need to assign fields after
        // the constructor is run, see http://drupal.org/node/315092.
        $this->setFetchMode(PDO::FETCH_CLASS, $options['fetch']);
      }
      else {
        $this->setFetchMode($options['fetch']);
      }
    }

    $logger = $this->dbh->getLogger();
    if (!empty($logger)) {
      $query_start = microtime(TRUE);
    }

    // Prepare the query.
    $statement = $this->getStatement($this->queryString, $args);
    if (!$statement) {
      $this->throwPDOException();
    }

    $return = $statement->execute($args);
    if (!$return) {
      $this->throwPDOException();
    }

    // Fetch all the data from the reply, in order to release any lock
    // as soon as possible.
    $this->rowCount = $statement->rowCount();
    $this->data = $statement->fetchAll(PDO::FETCH_ASSOC);
    // Destroy the statement as soon as possible. See
    // DatabaseConnection_sqlite::PDOPrepare() for explanation.
    unset($statement);

    $this->resultRowCount = count($this->data);

    if ($this->resultRowCount) {
      $this->columnNames = array_keys($this->data[0]);
    }
    else {
      $this->columnNames = array();
    }

    if (!empty($logger)) {
      $query_end = microtime(TRUE);
      $logger->log($this, $args, $query_end - $query_start);
    }

    // Initialize the first row in $this->currentRow.
    $this->next();

    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
