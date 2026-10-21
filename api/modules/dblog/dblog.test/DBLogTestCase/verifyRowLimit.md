# DBLogTestCase::verifyRowLimit()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 103–116 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L103-L116)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function verifyRowLimit($row_limit)
```

## Documentation

```text
Verifies setting of the database log row limit.

@param int $row_limit
  The row limit.
```

## Code

```php
  private function verifyRowLimit($row_limit) {
    // Change the database log row limit.
    $edit = array();
    $edit['dblog_row_limit'] = $row_limit;
    $this->drupalPost('admin/config/development/logging', $edit, t('Save configuration'));
    $this->assertResponse(200);

    // Check row limit variable.
    $current_limit = variable_get('dblog_row_limit', 1000);
    $this->assertTrue($current_limit == $row_limit, format_string('[Cache] Row limit variable of @count equals row limit of @limit', array('@count' => $current_limit, '@limit' => $row_limit)));
    // Verify dblog row limit equals specified row limit.
    $current_limit = unserialize(db_query("SELECT value FROM {variable} WHERE name = :dblog_limit", array(':dblog_limit' => 'dblog_row_limit'))->fetchField());
    $this->assertTrue($current_limit == $row_limit, format_string('[Variable table] Row limit variable of @count equals row limit of @limit', array('@count' => $current_limit, '@limit' => $row_limit)));
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
