# DatabaseConnection_mysql::utf8mb4IsSupported()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 634–660 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L634-L660)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsSupported()
```

## Documentation

_No docblock in source._

## Code

```php
  public function utf8mb4IsSupported() {
    // Ensure that the MySQL driver supports utf8mb4 encoding.
    $version = $this->connection->getAttribute(PDO::ATTR_CLIENT_VERSION);
    if (strpos($version, 'mysqlnd') !== FALSE) {
      // The mysqlnd driver supports utf8mb4 starting at version 5.0.9.
      $version = preg_replace('/^\D+([\d.]+).*/', '$1', $version);
      if (version_compare($version, '5.0.9', '<')) {
        return FALSE;
      }
    }
    else {
      // The libmysqlclient driver supports utf8mb4 starting at version 5.5.3.
      if (version_compare($version, '5.5.3', '<')) {
        return FALSE;
      }
    }

    // Ensure that the MySQL server supports large prefixes and utf8mb4.
    try {
      $this->query("CREATE TABLE {drupal_utf8mb4_test} (id VARCHAR(255), PRIMARY KEY(id(255))) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci ROW_FORMAT=DYNAMIC ENGINE=INNODB");
    }
    catch (Exception $e) {
      return FALSE;
    }
    $this->query("DROP TABLE {drupal_utf8mb4_test}");
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
