# SystemThemeFunctionalTest::testAdministrationTheme()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2045–2092 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2045-L2092)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testAdministrationTheme()
```

## Documentation

```text
Test the administration theme functionality.
```

## Code

```php
  function testAdministrationTheme() {
    theme_enable(array('stark'));
    variable_set('theme_default', 'stark');
    // Enable an administration theme and show it on the node admin pages.
    $edit = array(
      'admin_theme' => 'seven',
      'node_admin_theme' => TRUE,
    );
    $this->drupalPost('admin/appearance', $edit, t('Save configuration'));

    $this->drupalGet('admin/config');
    $this->assertRaw('themes/seven', 'Administration theme used on an administration page.');

    $this->drupalGet('node/' . $this->node->nid);
    $this->assertRaw('themes/stark', 'Site default theme used on node page.');

    $this->drupalGet('node/add');
    $this->assertRaw('themes/seven', 'Administration theme used on the add content page.');

    $this->drupalGet('node/' . $this->node->nid . '/edit');
    $this->assertRaw('themes/seven', 'Administration theme used on the edit content page.');

    // Disable the admin theme on the node admin pages.
    $edit = array(
      'node_admin_theme' => FALSE,
    );
    $this->drupalPost('admin/appearance', $edit, t('Save configuration'));

    $this->drupalGet('admin/config');
    $this->assertRaw('themes/seven', 'Administration theme used on an administration page.');

    $this->drupalGet('node/add');
    $this->assertRaw('themes/stark', 'Site default theme used on the add content page.');

    // Reset to the default theme settings.
    variable_set('theme_default', 'bartik');
    $edit = array(
      'admin_theme' => '0',
      'node_admin_theme' => FALSE,
    );
    $this->drupalPost('admin/appearance', $edit, t('Save configuration'));

    $this->drupalGet('admin');
    $this->assertRaw('themes/bartik', 'Site default theme used on administration page.');

    $this->drupalGet('node/add');
    $this->assertRaw('themes/bartik', 'Site default theme used on the add content page.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
