# DatabaseConnection::tablePrefix()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 507–514 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L507-L514)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function tablePrefix($table = 'default')
```

## Documentation

```text
Find the prefix for a table.

This function is for when you want to know the prefix of a table. This
is not used in prefixTables due to performance reasons.
```

## Code

```php
  public function tablePrefix($table = 'default') {
    if (isset($this->prefixes[$table])) {
      return $this->prefixes[$table];
    }
    else {
      return $this->prefixes['default'];
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
