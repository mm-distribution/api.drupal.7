# UpdateCoreTestCase::testServiceUnavailable()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 229–236 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L229-L236)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testServiceUnavailable()
```

## Documentation

```text
Tests the Update Manager module when the update server returns 503 errors.
```

## Code

```php
  function testServiceUnavailable() {
    $this->refreshUpdateStatus(array(), '503-error');
    // Ensure that no "Warning: SimpleXMLElement..." parse errors are found.
    $this->assertNoText('SimpleXMLElement');
    $this->assertUniqueText(t('Failed to get available update data for one project.'));
    $update_log = db_query_range('SELECT message FROM {watchdog} WHERE type = :type ORDER BY wid DESC', 0, 1, array(':type' => 'update'))->fetchField();
    $this->assertEqual('Error %errorcode (%message) occurred when trying to fetch available update data for the project %project.', $update_log, 'Failed update logged');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
