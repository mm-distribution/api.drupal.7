# DatabaseConnection::escapeField()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1003–1008 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1003-L1008)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function escapeField($field)
```

## Documentation

```text
Escapes a field name string.

Force all field names to be strictly alphanumeric-plus-underscore.
For some database drivers, it may also wrap the field name in
database-specific escape characters.

@return string
  The sanitized field name string.
```

## Code

```php
  public function escapeField($field) {
    if (!isset($this->escapedNames[$field])) {
      $this->escapedNames[$field] = preg_replace('/[^A-Za-z0-9_.]+/', '', $field);
    }
    return $this->escapedNames[$field];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
