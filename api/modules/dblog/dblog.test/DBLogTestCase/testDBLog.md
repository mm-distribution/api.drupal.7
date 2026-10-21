# DBLogTestCase::testDBLog()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 52–66 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L52-L66)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
function testDBLog()
```

## Documentation

```text
Tests Database Logging module functionality through interfaces.

First logs in users, then creates database log events, and finally tests
Database Logging module functionality through both the admin and user
interfaces.
```

## Code

```php
  function testDBLog() {
    // Login the admin user.
    $this->drupalLogin($this->big_user);

    $row_limit = 100;
    $this->verifyRowLimit($row_limit);
    $this->verifyCron($row_limit);
    $this->verifyEvents();
    $this->verifyReports();
    $this->testDBLogCorrupted();

    // Login the regular user.
    $this->drupalLogin($this->any_user);
    $this->verifyReports(403);
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
