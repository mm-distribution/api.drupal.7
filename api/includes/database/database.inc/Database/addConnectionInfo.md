# Database::addConnectionInfo()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1687–1691 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1687-L1691)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public static function addConnectionInfo($key, $target, $info)
```

## Documentation

```text
Adds database connection information for a given key/target.

This method allows the addition of new connection credentials at runtime.
Under normal circumstances the preferred way to specify database
credentials is via settings.php. However, this method allows them to be
added at arbitrary times, such as during unit tests, when connecting to
admin-defined third party databases, etc.

If the given key/target pair already exists, this method will be ignored.

@param $key
  The database key.
@param $target
  The database target name.
@param $info
  The database connection information, as it would be defined in
  settings.php. Note that the structure of this array will depend on the
  database driver it is connecting to.
```

## Code

```php
  public static function addConnectionInfo($key, $target, $info) {
    if (empty(self::$databaseInfo[$key][$target])) {
      self::$databaseInfo[$key][$target] = $info;
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
