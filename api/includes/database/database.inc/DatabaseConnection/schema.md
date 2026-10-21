# DatabaseConnection::schema()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 966–974 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L966-L974)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function schema()
```

## Documentation

```text
Returns a DatabaseSchema object for manipulating the schema.

This method will lazy-load the appropriate schema library file.

@return DatabaseSchema
  The DatabaseSchema object for this connection.
```

## Code

```php
  public function schema() {
    if (empty($this->schema)) {
      $class = $this->getDriverClass('DatabaseSchema', array('schema.inc'));
      if (class_exists($class)) {
        $this->schema = new $class($this);
      }
    }
    return $this->schema;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
