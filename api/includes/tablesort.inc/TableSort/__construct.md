# TableSort::__construct()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 24–31 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L24-L31)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
public function __construct(SelectQueryInterface $query, DatabaseConnection $connection)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct(SelectQueryInterface $query, DatabaseConnection $connection) {
    parent::__construct($query, $connection);

    // Add convenience tag to mark that this is an extended query. We have to
    // do this in the constructor to ensure that it is set before preExecute()
    // gets called.
    $this->addTag('tablesort');
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
