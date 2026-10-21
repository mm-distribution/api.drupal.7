# DashboardBlocksTestCase::testDisableEnable()

- **Type:** Method
- **File:** [`modules/dashboard/dashboard.test`](../_file.md), lines 88–115 · [local source](../../../../../source/modules/dashboard/dashboard.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test#L88-L115)
- **Class:** [DashboardBlocksTestCase](../DashboardBlocksTestCase.md)
- **Module/theme:** dashboard

## Signature

```php
function testDisableEnable()
```

## Documentation

```text
Tests that the dashboard module can be re-enabled, retaining its blocks.
```

## Code

```php
  function testDisableEnable() {
    // Add a new custom block to a dashboard region.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $this->randomName(8);
    $custom_block['body[value]'] = $this->randomName(32);
    $custom_block['regions[stark]'] = 'dashboard_main';
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));
    $this->drupalGet('admin/dashboard');
    $this->assertRaw($custom_block['title'], 'Block appears on the dashboard.');

    $edit = array();
    $edit['modules[Core][dashboard][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    $this->assertNoRaw('assigned to the invalid region', 'Dashboard blocks gracefully disabled.');
    module_list(TRUE);
    $this->assertFalse(module_exists('dashboard'), 'Dashboard disabled.');

    $edit['modules[Core][dashboard][enable]'] = 'dashboard';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    module_list(TRUE);
    $this->assertTrue(module_exists('dashboard'), 'Dashboard enabled.');

    $this->drupalGet('admin/dashboard');
    $this->assertRaw($custom_block['title'], 'Block still appears on the dashboard.');
  }
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.test](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.test) · Licensed GPL-2.0-or-later (see LICENSE)._
