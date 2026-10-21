# UpdateTestUploadCase::testUpdateManagerCoreSecurityUpdateMessages()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 757–792 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L757-L792)
- **Class:** [UpdateTestUploadCase](../UpdateTestUploadCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateManagerCoreSecurityUpdateMessages()
```

## Documentation

```text
Checks the messages on update manager pages when missing a security update.
```

## Code

```php
  function testUpdateManagerCoreSecurityUpdateMessages() {
    $setting = array(
      '#all' => array(
        'version' => '7.0',
      ),
    );
    variable_set('update_test_system_info', $setting);
    variable_set('update_fetch_url', url('update-test', array('absolute' => TRUE)));
    variable_set('update_test_xml_map', array('drupal' => '2-sec'));
    // Initialize the update status.
    $this->drupalGet('admin/reports/updates');

    // Now, make sure none of the Update manager pages have duplicate messages
    // about core missing a security update.

    $this->drupalGet('admin/modules/install');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/modules/update');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/appearance/install');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/appearance/update');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/reports/updates/install');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/reports/updates/update');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));

    $this->drupalGet('admin/update/ready');
    $this->assertNoText(t('There is a security update available for your version of Drupal.'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
