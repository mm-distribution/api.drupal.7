# DatabaseConnection::setTarget()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 559–563 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L559-L563)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function setTarget($target = NULL)
```

## Documentation

```text
Tells this connection object what its target value is.

This is needed for logging and auditing. It's sloppy to do in the
constructor because the constructor for child classes has a different
signature. We therefore also ensure that this function is only ever
called once.

@param $target
  The target this connection is for. Set to NULL (default) to disable
  logging entirely.
```

## Code

```php
  public function setTarget($target = NULL) {
    if (!isset($this->target)) {
      $this->target = $target;
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
