# DeleteQuery::__construct()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 761–767 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L761-L767)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(DatabaseConnection $connection, $table, array $options = array())
```

## Documentation

```text
Constructs a DeleteQuery object.

@param DatabaseConnection $connection
  A DatabaseConnection object.
@param string $table
  Name of the table to associate with this query.
@param array $options
  Array of database options.
```

## Code

```php
  public function __construct(DatabaseConnection $connection, $table, array $options = array()) {
    $options['return'] = Database::RETURN_AFFECTED;
    parent::__construct($connection, $options);
    $this->table = $table;

    $this->condition = new DatabaseCondition('AND');
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
