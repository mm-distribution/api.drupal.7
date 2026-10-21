# simpletest_clean_database()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 565–584 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L565-L584)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_clean_database()
```

## Documentation

```text
Removed prefixed tables from the database that are left over from crashed tests.
```

## Code

```php
function simpletest_clean_database() {
  $tables = db_find_tables_d8(Database::getConnection()->prefixTables('{simpletest}') . '%');
  $schema = drupal_get_schema_unprocessed('simpletest');
  $count = 0;
  foreach (array_diff_key($tables, $schema) as $table) {
    // Strip the prefix and skip tables without digits following "simpletest",
    // e.g. {simpletest_test_id}.
    if (preg_match('/simpletest\d+.*/', $table, $matches)) {
      db_drop_table($matches[0]);
      $count++;
    }
  }

  if ($count > 0) {
    drupal_set_message(format_plural($count, 'Removed 1 leftover table.', 'Removed @count leftover tables.'));
  }
  else {
    drupal_set_message(t('No leftover tables to remove.'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
