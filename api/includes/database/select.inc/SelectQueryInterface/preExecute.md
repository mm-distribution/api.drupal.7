# SelectQueryInterface::preExecute()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 482–482 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L482)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function preExecute(SelectQueryInterface $query = NULL);
```

## Documentation

```text
Generic preparation and validation for a SELECT query.

@return
  TRUE if the validation was successful, FALSE if not.
```

## Code

```php
  public function preExecute(SelectQueryInterface $query = NULL);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
