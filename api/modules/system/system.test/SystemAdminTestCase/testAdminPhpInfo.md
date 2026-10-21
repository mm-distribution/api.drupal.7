# SystemAdminTestCase::testAdminPhpInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2911–2920 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2911-L2920)
- **Class:** [SystemAdminTestCase](../SystemAdminTestCase.md)
- **Module/theme:** system

## Signature

```php
function testAdminPhpInfo()
```

## Documentation

```text
Test the phpinfo() page.
```

## Code

```php
  function testAdminPhpInfo() {
    $this->drupalGet('admin/reports/status/php');
    $this->assertText('PHP');
    $this->assertNoText('_COOKIE[');

    variable_set('sa_core_2023_004_phpinfo_flags', INFO_ALL);
    $this->drupalGet('admin/reports/status/php');
    $this->assertText('PHP');
    $this->assertText('_COOKIE[');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
