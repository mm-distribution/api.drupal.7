# DatabaseTasks::connect()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 431–444 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L431-L444)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function connect()
```

## Documentation

```text
Check if we can connect to the database.
```

## Code

```php
  protected function connect() {
    try {
      // This doesn't actually test the connection.
      db_set_active();
      // Now actually do a check.
      Database::getConnection();
      $this->pass('Drupal can CONNECT to the database ok.');
    }
    catch (Exception $e) {
      $this->fail(st('Failed to connect to your database server. The server reports the following message: %error.<ul><li>Is the database server running?</li><li>Does the database exist, and have you entered the correct database name?</li><li>Have you entered the correct username and password?</li><li>Have you entered the correct database hostname?</li></ul>', array('%error' => $e->getMessage())));
      return FALSE;
    }
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
