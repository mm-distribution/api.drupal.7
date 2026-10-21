# LocaleCSSAlterTest::testCSSFilesOrderInRTLMode()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3262–3286 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3262-L3286)
- **Class:** [LocaleCSSAlterTest](../LocaleCSSAlterTest.md)
- **Module/theme:** locale

## Signature

```php
function testCSSFilesOrderInRTLMode()
```

## Documentation

```text
Verifies that -rtl.css file is added directly after LTR .css file.
```

## Code

```php
  function testCSSFilesOrderInRTLMode() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'administer content types', 'access administration pages'));

    // Log in as admin.
    $this->drupalLogin($admin_user);

    // Install the Arabic language (which is RTL) and configure as the default.
    $edit = array();
    $edit['langcode'] = 'ar';
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    $edit = array();
    $edit['site_default'] = 'ar';
    $this->drupalPost(NULL, $edit, t('Save configuration'));

    // Verify that the -rtl.css file is added directly after LTR file.
    $this->drupalGet('');
    $query_string = '?' . variable_get('css_js_query_string', '0');
    $this->assertRaw('@import url("' . $base_url . '/modules/system/system.base.css' . $query_string . '");' . "\n" . '@import url("' . $base_url . '/modules/system/system.base-rtl.css' . $query_string . '");' . "\n", 'CSS: system.base-rtl.css is added directly after system.base.css.');
    $this->assertRaw('@import url("' . $base_url . '/modules/system/system.menus.css' . $query_string . '");' . "\n" . '@import url("' . $base_url . '/modules/system/system.menus-rtl.css' . $query_string . '");' . "\n", 'CSS: system.menus-rtl.css is added directly after system.menus.css.');
    $this->assertRaw('@import url("' . $base_url . '/modules/system/system.messages.css' . $query_string . '");' . "\n" . '@import url("' . $base_url . '/modules/system/system.messages-rtl.css' . $query_string . '");' . "\n", 'CSS: system.messages-rtl.css is added directly after system.messages.css.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
