# DatabaseSchema_pgsql::getTempNamespaceName()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 171–176 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L171-L176)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function getTempNamespaceName()
```

## Documentation

```text
Gets PostgreSQL's temporary namespace name.

@return string
  PostgreSQL's temporary namespace anme.
```

## Code

```php
  protected function getTempNamespaceName() {
    if (!isset($this->tempNamespaceName)) {
      $this->tempNamespaceName = $this->connection->query('SELECT nspname FROM pg_namespace WHERE oid = pg_my_temp_schema()')->fetchField();
    }
    return $this->tempNamespaceName;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
