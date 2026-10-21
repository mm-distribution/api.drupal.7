# InsertQuery::__construct()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 498–504 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L498-L504)
- **Class:** [InsertQuery](../InsertQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct($connection, $table, array $options = array())
```

## Documentation

```text
Constructs an InsertQuery object.

@param DatabaseConnection $connection
  A DatabaseConnection object.
@param string $table
  Name of the table to associate with this query.
@param array $options
  Array of database options.
```

## Code

```php
  public function __construct($connection, $table, array $options = array()) {
    if (!isset($options['return'])) {
      $options['return'] = Database::RETURN_INSERT_ID;
    }
    parent::__construct($connection, $options);
    $this->table = $table;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
