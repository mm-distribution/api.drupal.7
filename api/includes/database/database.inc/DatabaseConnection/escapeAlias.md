# DatabaseConnection::escapeAlias()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1021–1026 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1021-L1026)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function escapeAlias($field)
```

## Documentation

```text
Escapes an alias name string.

Force all alias names to be strictly alphanumeric-plus-underscore. In
contrast to DatabaseConnection::escapeField() /
DatabaseConnection::escapeTable(), this doesn't allow the period (".")
because that is not allowed in aliases.

@return string
  The sanitized field name string.
```

## Code

```php
  public function escapeAlias($field) {
    if (!isset($this->escapedAliases[$field])) {
      $this->escapedAliases[$field] = preg_replace('/[^A-Za-z0-9_]+/', '', $field);
    }
    return $this->escapedAliases[$field];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
