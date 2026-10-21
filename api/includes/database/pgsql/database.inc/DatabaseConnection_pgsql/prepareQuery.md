# DatabaseConnection_pgsql::prepareQuery()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 77–86 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L77-L86)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function prepareQuery($query)
```

## Documentation

_No docblock in source._

## Code

```php
  public function prepareQuery($query) {
    // mapConditionOperator converts LIKE operations to ILIKE for consistency
    // with MySQL. However, Postgres does not support ILIKE on bytea (blobs)
    // fields.
    // To make the ILIKE operator work, we type-cast bytea fields into text.
    // @todo This workaround only affects bytea fields, but the involved field
    //   types involved in the query are unknown, so there is no way to
    //   conditionally execute this for affected queries only.
    return parent::prepareQuery(preg_replace('/ ([^ ]+) +(I*LIKE|NOT +I*LIKE) /i', ' ${1}::text ${2} ', $query));
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
