# DatabaseTasks_mysql

- **Type:** Class
- **File:** [`includes/database/mysql/install.inc`](_file.md), lines 11–32 · [local source](../../../../../source/includes/database/mysql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc#L11-L32)

## Signature

```php
class DatabaseTasks_mysql extends DatabaseTasks
```

## Documentation

```text
Specifies installation tasks for MySQL and equivalent databases.
```

## Properties

### $pdoDriver

```php
protected $pdoDriver = 'mysql';
```

```text
The PDO driver name for MySQL and equivalent databases.

@var string
```

## Methods (derived index)

- [name()](DatabaseTasks_mysql/name.md) — Returns a human-readable name string for MySQL and equivalent databases.
- [minimumVersion()](DatabaseTasks_mysql/minimumVersion.md) — Returns the minimum version for MySQL.

---
_Drupal 7.103 · [includes/database/mysql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
