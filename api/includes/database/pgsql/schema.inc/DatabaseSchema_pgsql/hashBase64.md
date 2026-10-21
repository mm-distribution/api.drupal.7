# DatabaseSchema_pgsql::hashBase64()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 836–842 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L836-L842)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function hashBase64($data)
```

## Documentation

```text
Calculates a base-64 encoded, PostgreSQL-safe sha-256 hash per PostgreSQL
documentation: 4.1. Lexical Structure.

@param $data
  String to be hashed.

@return string
  A base-64 encoded sha-256 hash, with + and / replaced with _ and any =
  padding characters removed.
```

## Code

```php
  protected function hashBase64($data) {
    // Ensure lowercase as D7's pgsql driver does not quote identifiers
    // consistently, and they are therefore folded to lowercase by PostgreSQL.
    $hash = strtolower(base64_encode(hash('sha256', $data, TRUE)));
    // Modify the hash so it's safe to use in PostgreSQL identifiers.
    return strtr($hash, array('+' => '_', '/' => '_', '=' => ''));
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
