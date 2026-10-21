# UpdateCoreTestCase::testModulePageRunCron()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 147–155 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L147-L155)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testModulePageRunCron()
```

## Documentation

```text
Checks that running cron updates the list of available updates.
```

## Code

```php
  function testModulePageRunCron() {
    $this->setSystemInfo7_0();
    variable_set('update_fetch_url', url('update-test', array('absolute' => TRUE)));
    variable_set('update_test_xml_map', array('drupal' => '0'));

    $this->cronRun();
    $this->drupalGet('admin/modules');
    $this->assertNoText(t('No update information available.'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
