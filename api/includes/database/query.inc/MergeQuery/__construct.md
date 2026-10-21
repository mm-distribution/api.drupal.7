# MergeQuery::__construct()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1370–1376 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1370-L1376)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(DatabaseConnection $connection, $table, array $options = array())
```

## Documentation

```text
Constructs a MergeQuery object.

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
    $this->conditionTable = $table;
    $this->condition = new DatabaseCondition('AND');
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
