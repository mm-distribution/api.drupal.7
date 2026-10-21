# ModuleTestCase::assertModuleTablesDoNotExist()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 62–71 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L62-L71)
- **Class:** [ModuleTestCase](../ModuleTestCase.md)
- **Module/theme:** system

## Signature

```php
function assertModuleTablesDoNotExist($module)
```

## Documentation

```text
Assert that none of the tables defined in a module's hook_schema() exist.

@param $module
  The name of the module.
```

## Code

```php
  function assertModuleTablesDoNotExist($module) {
    $tables = array_keys(drupal_get_schema_unprocessed($module));
    $tables_exist = FALSE;
    foreach ($tables as $table) {
      if (db_table_exists($table)) {
        $tables_exist = TRUE;
      }
    }
    return $this->assertFalse($tables_exist, format_string('None of the database tables defined by the @module module exist.', array('@module' => $module)));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
