# ModuleTestCase::assertTableCount()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 30–37 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L30-L37)
- **Class:** [ModuleTestCase](../ModuleTestCase.md)
- **Module/theme:** system

## Signature

```php
function assertTableCount($base_table, $count = TRUE)
```

## Documentation

```text
Assert there are tables that begin with the specified base table name.

@param $base_table
  Beginning of table name to look for.
@param $count
  (optional) Whether or not to assert that there are tables that match the
  specified base table. Defaults to TRUE.
```

## Code

```php
  function assertTableCount($base_table, $count = TRUE) {
    $tables = db_find_tables_d8($base_table . '%');

    if ($count) {
      return $this->assertTrue($tables, format_string('Tables matching "@base_table" found.', array('@base_table' => $base_table)));
    }
    return $this->assertFalse($tables, format_string('Tables matching "@base_table" not found.', array('@base_table' => $base_table)));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
