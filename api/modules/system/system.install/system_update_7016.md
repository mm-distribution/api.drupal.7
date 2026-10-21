# system_update_7016()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2200–2227 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2200-L2227)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7016()
```

## Documentation

```text
Remove custom datatype *_unsigned in PostgreSQL.
```

## Code

```php
function system_update_7016() {
  // Only run these queries if the driver used is pgsql.
  if (db_driver() == 'pgsql') {
    $result = db_query("SELECT c.relname AS table, a.attname AS field,
                        pg_catalog.format_type(a.atttypid, a.atttypmod) AS type
                        FROM pg_catalog.pg_attribute a
                        LEFT JOIN pg_class c ON (c.oid =  a.attrelid)
                        WHERE pg_catalog.pg_table_is_visible(c.oid) AND c.relkind = 'r'
                        AND pg_catalog.format_type(a.atttypid, a.atttypmod) LIKE '%unsigned%'");
    foreach ($result as $row) {
      switch ($row->type) {
        case 'smallint_unsigned':
          $datatype = 'int';
          break;
        case 'int_unsigned':
        case 'bigint_unsigned':
        default:
          $datatype = 'bigint';
          break;
      }
      db_query('ALTER TABLE ' . $row->table . ' ALTER COLUMN "' . $row->field . '" TYPE ' . $datatype);
      db_query('ALTER TABLE ' . $row->table . ' ADD CHECK ("' . $row->field . '" >= 0)');
    }
    db_query('DROP DOMAIN IF EXISTS smallint_unsigned');
    db_query('DROP DOMAIN IF EXISTS int_unsigned');
    db_query('DROP DOMAIN IF EXISTS bigint_unsigned');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
