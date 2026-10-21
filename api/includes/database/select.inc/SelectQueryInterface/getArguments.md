# SelectQueryInterface::getArguments()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 162–162 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L162)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getArguments(QueryPlaceholderInterface $queryPlaceholder = NULL);
```

## Documentation

```text
Compiles and returns an associative array of the arguments for this prepared statement.

@param $queryPlaceholder
  When collecting the arguments of a subquery, the main placeholder
  object should be passed as this parameter.

@return
  An associative array of all placeholder arguments for this query.
```

## Code

```php
  public function getArguments(QueryPlaceholderInterface $queryPlaceholder = NULL);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
