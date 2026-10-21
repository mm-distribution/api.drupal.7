# includes/database/pgsql/database.inc

- **Source:** [local](../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · 233 lines

## File documentation

```text
@file
Database interface code for PostgreSQL database servers.
```

## Classes and interfaces (derived index)

- [DatabaseConnection_pgsql](DatabaseConnection_pgsql.md)

## Constants

### POSTGRESQL_NEXTID_LOCK

- Line 16; topics: database

```php
define('POSTGRESQL_NEXTID_LOCK', 1000);
```

```text
The name by which to obtain a lock for retrieving the next insert id.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
