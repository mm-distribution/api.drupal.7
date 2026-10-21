# DatabaseTasks_pgsql::checkPHPVersion()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 76–80 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L76-L80)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
function checkPHPVersion()
```

## Documentation

```text
Check PHP version.

There are two bugs in PDO_pgsql affecting Drupal:

- in versions < 5.2.7, PDO_pgsql refuses to insert an empty string into
  a NOT NULL BLOB column. See: http://bugs.php.net/bug.php?id=46249
- in versions < 5.2.11 and < 5.3.1 that prevents inserting integer values
  into numeric columns that exceed the PHP_INT_MAX value.
  See: http://bugs.php.net/bug.php?id=48924
```

## Code

```php
  function checkPHPVersion() {
    if (!version_compare(PHP_VERSION, '5.2.11', '>=') || (version_compare(PHP_VERSION, '5.3.0', '>=') && !version_compare(PHP_VERSION, '5.3.1', '>='))) {
      $this->fail(st('The version of PHP you are using has known issues with PostgreSQL. You need to upgrade PHP to 5.2.11, 5.3.1 or greater.'));
    };
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
