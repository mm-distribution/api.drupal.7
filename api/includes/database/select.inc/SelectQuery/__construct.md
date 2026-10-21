# SelectQuery::__construct()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 985–991 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L985-L991)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct($table, $alias, DatabaseConnection $connection, $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($table, $alias, DatabaseConnection $connection, $options = array()) {
    $options['return'] = Database::RETURN_STATEMENT;
    parent::__construct($connection, $options);
    $this->where = new DatabaseCondition('AND');
    $this->having = new DatabaseCondition('AND');
    $this->addJoin(NULL, $table, $alias);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
