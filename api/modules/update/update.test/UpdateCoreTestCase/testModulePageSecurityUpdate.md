# UpdateCoreTestCase::testModulePageSecurityUpdate()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 194–224 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L194-L224)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testModulePageSecurityUpdate()
```

## Documentation

```text
Checks the messages at admin/modules when a security update is missing.
```

## Code

```php
  function testModulePageSecurityUpdate() {
    $this->setSystemInfo7_0();
    // Instead of using refreshUpdateStatus(), set these manually.
    variable_set('update_fetch_url', url('update-test', array('absolute' => TRUE)));
    variable_set('update_test_xml_map', array('drupal' => '2-sec'));

    $this->drupalGet('admin/reports/updates');
    $this->clickLink(t('Check manually'));
    $this->assertText(t('Checked available update data for one project.'));
    $this->drupalGet('admin/modules');
    $this->assertNoText(t('There are updates available for your version of Drupal.'));
    $this->assertText(t('There is a security update available for your version of Drupal.'));

    // Make sure admin/appearance warns you you're missing a security update.
    $this->drupalGet('admin/appearance');
    $this->assertNoText(t('There are updates available for your version of Drupal.'));
    $this->assertText(t('There is a security update available for your version of Drupal.'));

    // Make sure duplicate messages don't appear on Update status pages.
    $this->drupalGet('admin/reports/status');
    // We're expecting "There is a security update..." inside the status report
    // itself, but the drupal_set_message() appears as an li so we can prefix
    // with that and search for the raw HTML.
    $this->assertNoRaw('<li>' . t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/reports/updates');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/reports/updates/settings');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
