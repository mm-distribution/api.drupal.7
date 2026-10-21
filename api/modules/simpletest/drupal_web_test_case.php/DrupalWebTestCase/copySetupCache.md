# DrupalWebTestCase::copySetupCache()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1621–1653 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1621-L1653)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function copySetupCache($from, $to)
```

## Documentation

```text
Copy the setup cache from/to another table and files directory.

@param string $from
  The prefix_id / cache_key from where to copy.
@param string $to
  The prefix_id / cache_key to where to copy.

@return bool
  TRUE if the setup cache was copied to the current installation, FALSE
  otherwise.
```

## Code

```php
  protected function copySetupCache($from, $to) {
    $from_prefix = 'simpletest' . $from;
    $to_prefix = 'simpletest' . $to;

    try {
       $tables = db_query("SHOW TABLES LIKE :prefix", array(':prefix' => db_like($from_prefix) . '%' ))->fetchCol();

       if (count($tables) == 0) {
         return FALSE;
       }

       foreach ($tables as $from_table) {
         $table = substr($from_table, strlen($from_prefix));
         $to_table = $to_prefix . $table;

         // Remove the table in case the copying process was interrupted.
         db_query('DROP TABLE IF EXISTS ' . $to_table);
         db_query('CREATE TABLE ' . $to_table . ' LIKE ' . $from_table);
         db_query('ALTER TABLE ' . $to_table . ' DISABLE KEYS');
         db_query('INSERT ' . $to_table . ' SELECT * FROM ' . $from_table);
         db_query('ALTER TABLE ' . $to_table . ' ENABLE KEYS');
       }
    }
    catch (Exception $e) {
      return FALSE;
    }

    $from_dir = $this->originalFileDirectory . '/simpletest/' . $from;
    $to_dir = $this->originalFileDirectory . '/simpletest/' . $to;
    $this->recursiveDirectoryCopy($from_dir, $to_dir);

    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
