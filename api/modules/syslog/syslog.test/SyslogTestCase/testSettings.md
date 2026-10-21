# SyslogTestCase::testSettings()

- **Type:** Method
- **File:** [`modules/syslog/syslog.test`](../_file.md), lines 27–43 · [local source](../../../../../source/modules/syslog/syslog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.test#L27-L43)
- **Class:** [SyslogTestCase](../SyslogTestCase.md)
- **Module/theme:** syslog

## Signature

```php
function testSettings()
```

## Documentation

```text
Tests the syslog settings page.
```

## Code

```php
  function testSettings() {
    $admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($admin_user);

    $edit = array();
    // If we're on Windows, there is no configuration form.
    if (defined('LOG_LOCAL6')) {
      $this->drupalPost('admin/config/development/logging', array('syslog_facility' => LOG_LOCAL6), t('Save configuration'));
      $this->assertText(t('The configuration options have been saved.'));

      $this->drupalGet('admin/config/development/logging');
      if ($this->parse()) {
        $field = $this->xpath('//option[@value=:value]', array(':value' => LOG_LOCAL6)); // Should be one field.
        $this->assertTrue($field[0]['selected'] == 'selected', 'Facility value saved.');
      }
    }
  }
```

---
_Drupal 7.103 · [modules/syslog/syslog.test](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
