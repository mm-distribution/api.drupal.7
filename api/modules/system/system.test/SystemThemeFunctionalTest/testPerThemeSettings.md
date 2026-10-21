# SystemThemeFunctionalTest::testPerThemeSettings()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2022–2040 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2022-L2040)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testPerThemeSettings()
```

## Documentation

```text
Test the individual per-theme settings form.
```

## Code

```php
  function testPerThemeSettings() {
    // Enable the test theme and the module that controls it. Clear caches in
    // between so that the module's hook_system_theme_info() implementation is
    // correctly registered.
    module_enable(array('theme_test'));
    drupal_flush_all_caches();
    theme_enable(array('test_theme'));

    // Test that the theme-specific settings form can be saved and that the
    // theme-specific checkbox is checked and unchecked as appropriate.
    $this->drupalGet('admin/appearance/settings/test_theme');
    $this->assertNoFieldChecked('edit-test-theme-checkbox', 'The test_theme_checkbox setting is unchecked.');
    $this->drupalPost(NULL, array('test_theme_checkbox' => TRUE), t('Save configuration'));
    $this->assertText('The test theme setting was saved.');
    $this->assertFieldChecked('edit-test-theme-checkbox', 'The test_theme_checkbox setting is checked.');
    $this->drupalPost(NULL, array('test_theme_checkbox' => FALSE), t('Save configuration'));
    $this->assertText('The test theme setting was saved.');
    $this->assertNoFieldChecked('edit-test-theme-checkbox', 'The test_theme_checkbox setting is unchecked.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
