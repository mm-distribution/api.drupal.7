# SystemMainContentFallback::testMainContentFallback()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1846–1892 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1846-L1892)
- **Class:** [SystemMainContentFallback](../SystemMainContentFallback.md)
- **Module/theme:** system

## Signature

```php
function testMainContentFallback()
```

## Documentation

```text
Test availability of main content.
```

## Code

```php
  function testMainContentFallback() {
    $edit = array();
    // Disable the dashboard module, which depends on the block module.
    $edit['modules[Core][dashboard][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    // Disable the block module.
    $edit['modules[Core][block][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    module_list(TRUE);
    $this->assertFalse(module_exists('block'), 'Block module disabled.');

    // At this point, no region is filled and fallback should be triggered.
    $this->drupalGet('admin/config/system/site-information');
    $this->assertField('site_name', 'Admin interface still available.');

    // Fallback should not trigger when another module is handling content.
    $this->drupalGet('system-test/main-content-handling');
    $this->assertRaw('id="system-test-content"', 'Content handled by another module');
    $this->assertText(t('Content to test main content fallback'), 'Main content still displayed.');

    // Fallback should trigger when another module
    // indicates that it is not handling the content.
    $this->drupalGet('system-test/main-content-fallback');
    $this->assertText(t('Content to test main content fallback'), 'Main content fallback properly triggers.');

    // Fallback should not trigger when another module is handling content.
    // Note that this test ensures that no duplicate
    // content gets created by the fallback.
    $this->drupalGet('system-test/main-content-duplication');
    $this->assertNoText(t('Content to test main content fallback'), 'Main content not duplicated.');

    // Request a user* page and see if it is displayed.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('user/' . $this->web_user->uid . '/edit');
    $this->assertField('mail', 'User interface still available.');

    // Enable the block module again.
    $this->drupalLogin($this->admin_user);
    $edit = array();
    $edit['modules[Core][block][enable]'] = 'block';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    module_list(TRUE);
    $this->assertTrue(module_exists('block'), 'Block module re-enabled.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
