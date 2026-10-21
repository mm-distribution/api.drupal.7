# UpdateCoreTestCase::testModulePageUpToDate()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 160–172 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L160-L172)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testModulePageUpToDate()
```

## Documentation

```text
Checks the messages at admin/modules when the site is up to date.
```

## Code

```php
  function testModulePageUpToDate() {
    $this->setSystemInfo7_0();
    // Instead of using refreshUpdateStatus(), set these manually.
    variable_set('update_fetch_url', url('update-test', array('absolute' => TRUE)));
    variable_set('update_test_xml_map', array('drupal' => '0'));

    $this->drupalGet('admin/reports/updates');
    $this->clickLink(t('Check manually'));
    $this->assertText(t('Checked available update data for one project.'));
    $this->drupalGet('admin/modules');
    $this->assertNoText(t('There are updates available for your version of Drupal.'));
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
