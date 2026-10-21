# SystemAdminTestCase::testTrustedHostSettingsMessage()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2944–2953 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2944-L2953)
- **Class:** [SystemAdminTestCase](../SystemAdminTestCase.md)
- **Module/theme:** system

## Signature

```php
function testTrustedHostSettingsMessage()
```

## Documentation

```text
Test Trusted Host Settings message on the status report page.
```

## Code

```php
  function testTrustedHostSettingsMessage() {
    $this->drupalGet('admin/reports/status');
    $this->assertText('The trusted_host_patterns setting is not configured in settings.php.');
    $this->assertNoText('The trusted_host_patterns setting is set to allow');

    variable_set('trusted_host_patterns', array('a_trusted_pattern', 'another_trusted_pattern'));
    $this->drupalGet('admin/reports/status');
    $this->assertNoText('The trusted_host_patterns setting is not configured in settings.php.');
    $this->assertText('The trusted_host_patterns setting is set to allow a_trusted_pattern, another_trusted_pattern');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
