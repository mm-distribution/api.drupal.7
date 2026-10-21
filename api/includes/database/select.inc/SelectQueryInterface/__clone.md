# SelectQueryInterface::__clone()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 514–514 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L514)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __clone();
```

## Documentation

```text
Clone magic method.

Select queries have dependent objects that must be deep-cloned.  The
connection object itself, however, should not be cloned as that would
duplicate the connection itself.
```

## Code

```php
  public function __clone();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
