# DatabaseTasks_pgsql

- **Type:** Class
- **File:** [`includes/database/pgsql/install.inc`](_file.md), lines 11–196 · [local source](../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L11-L196)

## Signature

```php
class DatabaseTasks_pgsql extends DatabaseTasks
```

## Documentation

_No docblock in source._

## Properties

### $pdoDriver

```php
protected $pdoDriver = 'pgsql';
```

## Methods (derived index)

- [__construct()](DatabaseTasks_pgsql/__construct.md)
- [name()](DatabaseTasks_pgsql/name.md)
- [minimumVersion()](DatabaseTasks_pgsql/minimumVersion.md)
- [checkEncoding()](DatabaseTasks_pgsql/checkEncoding.md) — Check encoding is UTF8.
- [checkPHPVersion()](DatabaseTasks_pgsql/checkPHPVersion.md) — Check PHP version.
- [checkBinaryOutput()](DatabaseTasks_pgsql/checkBinaryOutput.md) — Check Binary Output.
- [checkBinaryOutputSuccess()](DatabaseTasks_pgsql/checkBinaryOutputSuccess.md) — Verify that a binary data roundtrip returns the original string.
- [initializeDatabase()](DatabaseTasks_pgsql/initializeDatabase.md) — Make PostgreSQL Drupal friendly.

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
