# DatabaseStatementPrefetch::current()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 272–329 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L272-L329)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function current()
```

## Documentation

_No docblock in source._

## Code

```php
  public function current() {
    if (isset($this->currentRow)) {
      switch ($this->fetchStyle) {
        case PDO::FETCH_ASSOC:
          return $this->currentRow;
        case PDO::FETCH_BOTH:
          // PDO::FETCH_BOTH returns an array indexed by both the column name
          // and the column number.
          return $this->currentRow + array_values($this->currentRow);
        case PDO::FETCH_NUM:
          return array_values($this->currentRow);
        case PDO::FETCH_LAZY:
          // We do not do lazy as everything is fetched already. Fallback to
          // PDO::FETCH_OBJ.
        case PDO::FETCH_OBJ:
          return (object) $this->currentRow;
        case PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE:
          $class_name = array_shift($this->currentRow);
          // Deliberate no break.
        case PDO::FETCH_CLASS:
          if (!isset($class_name)) {
            $class_name = $this->fetchOptions['class'];
          }
          if (count($this->fetchOptions['constructor_args'])) {
            // Verify the current db connection to avoid this code being called
            // in an inappropriate context.
            $db_connection_options = Database::getConnection()->getConnectionOptions();
            $defaults = array('sqlite', 'oracle');
            $extras = variable_get('database_statement_prefetch_valid_db_drivers', array());
            $valid_db_drivers = array_merge($defaults, $extras);
            if (!in_array($db_connection_options['driver'], $valid_db_drivers)) {
              throw new BadMethodCallException();
            }
            $reflector = new ReflectionClass($class_name);
            $result = $reflector->newInstanceArgs($this->fetchOptions['constructor_args']);
          }
          else {
            $result = new $class_name();
          }
          foreach ($this->currentRow as $k => $v) {
            $result->$k = $v;
          }
          return $result;
        case PDO::FETCH_INTO:
          foreach ($this->currentRow as $k => $v) {
            $this->fetchOptions['object']->$k = $v;
          }
          return $this->fetchOptions['object'];
        case PDO::FETCH_COLUMN:
          if (isset($this->columnNames[$this->fetchOptions['column']])) {
            return $this->currentRow[$k][$this->columnNames[$this->fetchOptions['column']]];
          }
          else {
            return;
          }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
