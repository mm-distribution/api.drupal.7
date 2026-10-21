# SystemThemeFunctionalTest::testSwitchDefaultTheme()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2097–2112 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2097-L2112)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testSwitchDefaultTheme()
```

## Documentation

```text
Test switching the default theme.
```

## Code

```php
  function testSwitchDefaultTheme() {
    // Enable "stark" and set it as the default theme.
    theme_enable(array('stark'));
    $this->drupalGet('admin/appearance');
    $this->clickLink(t('Set default'), 1);
    $this->assertTrue(variable_get('theme_default', '') == 'stark', 'Site default theme switched successfully.');

    // Test the default theme on the secondary links (blocks admin page).
    $this->drupalGet('admin/structure/block');
    $this->assertText('Stark(' . t('active tab') . ')', 'Default local task on blocks admin page is the default theme.');
    // Switch back to Bartik and test again to test that the menu cache is cleared.
    $this->drupalGet('admin/appearance');
    $this->clickLink(t('Set default'), 0);
    $this->drupalGet('admin/structure/block');
    $this->assertText('Bartik(' . t('active tab') . ')', 'Default local task on blocks admin page has changed.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
