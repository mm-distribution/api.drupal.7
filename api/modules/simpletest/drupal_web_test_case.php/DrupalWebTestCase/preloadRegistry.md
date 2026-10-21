# DrupalWebTestCase::preloadRegistry()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1868–1895 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1868-L1895)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function preloadRegistry()
```

## Documentation

```text
Preload the registry from the testing site.

This method is called by DrupalWebTestCase::setUp(), and preloads the
registry from the testing site to cut down on the time it takes to
set up a clean environment for the current test run.
```

## Code

```php
  protected function preloadRegistry() {
    // Use two separate queries, each with their own connections: copy the
    // {registry} and {registry_file} tables over from the parent installation
    // to the child installation.
    $original_connection = Database::getConnection('default', 'simpletest_original_default');
    $test_connection = Database::getConnection();

    foreach (array('registry', 'registry_file') as $table) {
      // Find the records from the parent database.
      $source_query = $original_connection
        ->select($table, array(), array('fetch' => PDO::FETCH_ASSOC))
        ->fields($table);

      $dest_query = $test_connection->insert($table);

      $first = TRUE;
      foreach ($source_query->execute() as $row) {
        if ($first) {
          $dest_query->fields(array_keys($row));
          $first = FALSE;
        }
        // Insert the records into the child database.
        $dest_query->values($row);
      }

      $dest_query->execute();
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
