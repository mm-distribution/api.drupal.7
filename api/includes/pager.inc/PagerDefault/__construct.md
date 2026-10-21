# PagerDefault::__construct()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 45–51 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L45-L51)
- **Class:** [PagerDefault](../PagerDefault.md)

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

    // Add pager tag. Do this here to ensure that it is always added before
    // preExecute() is called.
    $this->addTag('pager');
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
