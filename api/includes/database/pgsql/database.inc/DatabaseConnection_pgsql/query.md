# DatabaseConnection_pgsql::query()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 88–142 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L88-L142)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function query($query, array $args = array(), $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function query($query, array $args = array(), $options = array()) {

    $options += $this->defaultOptions();

    // The PDO PostgreSQL driver has a bug which
    // doesn't type cast booleans correctly when
    // parameters are bound using associative
    // arrays.
    // See http://bugs.php.net/bug.php?id=48383
    foreach ($args as &$value) {
      if (is_bool($value)) {
        $value = (int) $value;
      }
    }

    try {
      if ($query instanceof DatabaseStatementInterface) {
        $stmt = $query;
        $stmt->execute(NULL, $options);
      }
      else {
        $this->expandArguments($query, $args);
        $stmt = $this->prepareQuery($query);
        $stmt->execute($args, $options);
      }

      switch ($options['return']) {
        case Database::RETURN_STATEMENT:
          return $stmt;
        case Database::RETURN_AFFECTED:
          return $stmt->rowCount();
        case Database::RETURN_INSERT_ID:
          $sequence_name = isset($options['sequence_name']) ? $options['sequence_name'] : NULL;
          return $this->connection->lastInsertId($sequence_name);
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
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
