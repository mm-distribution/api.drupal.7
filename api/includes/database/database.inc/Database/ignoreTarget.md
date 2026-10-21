# Database::ignoreTarget()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1857–1859 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1857-L1859)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public static function ignoreTarget($key, $target)
```

## Documentation

```text
Instructs the system to temporarily ignore a given key/target.

At times we need to temporarily disable slave queries. To do so, call this
method with the database key and the target to disable. That database key
will then always fall back to 'default' for that key, even if it's defined.

@param $key
  The database connection key.
@param $target
  The target of the specified key to ignore.
```

## Code

```php
  public static function ignoreTarget($key, $target) {
    self::$ignoreTargets[$key][$target] = TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
