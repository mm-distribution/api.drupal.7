# DatabaseSchema_pgsql::ensureIdentifiersLength()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 67–89 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L67-L89)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function ensureIdentifiersLength($table_identifier_part, $column_identifier_part, $tag)
```

## Documentation

```text
Make sure to limit identifiers according to PostgreSQL compiled in length.

PostgreSQL allows in standard configuration identifiers no longer than 63
chars for table/relation names, indexes, primary keys, and constraints. So
we map all identifiers that are too long to drupal_base64hash_tag, where
tag is one of:
  - idx for indexes
  - key for constraints
  - pkey for primary keys
  - seq for sequences

@param string $table_identifier_part
  The first argument used to build the identifier string. This usually
  refers to a table/relation name.
@param string $column_identifier_part
  The second argument used to build the identifier string. This usually
  refers to one or more column names.
@param string $tag
  The identifier tag. It can be one of 'idx', 'key', 'pkey' or 'seq'.

@return string
  The index/constraint/pkey identifier.
```

## Code

```php
  protected function ensureIdentifiersLength($table_identifier_part, $column_identifier_part, $tag) {
    $info = $this->getPrefixInfo($table_identifier_part);
    $table_identifier_part = $info['table'];

    // Filters out potentially empty $column_identifier_part to ensure
    // compatibility with old naming convention (see prefixNonTable()).
    $identifiers = array_filter(array($table_identifier_part, $column_identifier_part, $tag));
    $identifierName = implode('_', $identifiers);

    // Retrieve the max identifier length which is usually 63 characters
    // but can be altered before PostgreSQL is compiled so we need to check.
    if (empty($this->maxIdentifierLength)) {
      $this->maxIdentifierLength = $this->connection->query("SHOW max_identifier_length")->fetchField();
    }

    if (strlen($identifierName) > $this->maxIdentifierLength) {
      $saveIdentifier = 'drupal_' . $this->hashBase64($identifierName) . '_' . $tag;
    }
    else {
      $saveIdentifier = $identifierName;
    }
    return $saveIdentifier;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
