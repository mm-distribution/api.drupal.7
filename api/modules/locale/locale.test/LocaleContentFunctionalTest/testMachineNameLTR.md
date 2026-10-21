# LocaleContentFunctionalTest::testMachineNameLTR()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2165–2188 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2165-L2188)
- **Class:** [LocaleContentFunctionalTest](../LocaleContentFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testMachineNameLTR()
```

## Documentation

```text
Verifies that machine name fields are always LTR.
```

## Code

```php
  function testMachineNameLTR() {
    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'administer content types', 'access administration pages'));

    // Log in as admin.
    $this->drupalLogin($admin_user);

    // Verify that the machine name field is LTR for a new content type.
    $this->drupalGet('admin/structure/types/add');
    $this->assertFieldByXpath('//input[@name="type" and @dir="ltr"]', NULL, 'The machine name field is LTR when no additional language is configured.');

    // Install the Arabic language (which is RTL) and configure as the default.
    $edit = array();
    $edit['langcode'] = 'ar';
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    $edit = array();
    $edit['site_default'] = 'ar';
    $this->drupalPost(NULL, $edit, t('Save configuration'));

    // Verify that the machine name field is still LTR for a new content type.
    $this->drupalGet('admin/structure/types/add');
    $this->assertFieldByXpath('//input[@name="type" and @dir="ltr"]', NULL, 'The machine name field is LTR when the default language is RTL.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
