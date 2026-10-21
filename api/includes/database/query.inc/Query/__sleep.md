# Query::__sleep()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 343–347 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L343-L347)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __sleep()
```

## Documentation

```text
Implements the magic __sleep function to disconnect from the database.
```

## Code

```php
  public function __sleep() {
    $keys = get_object_vars($this);
    unset($keys['connection']);
    return array_keys($keys);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
