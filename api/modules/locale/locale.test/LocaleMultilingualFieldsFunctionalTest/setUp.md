# LocaleMultilingualFieldsFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2794–2819 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2794-L2819)
- **Class:** [LocaleMultilingualFieldsFunctionalTest](../LocaleMultilingualFieldsFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale');
    // Setup users.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'administer content types', 'access administration pages', 'create page content', 'edit own page content'));
    $this->drupalLogin($admin_user);

    // Add a new language.
    require_once DRUPAL_ROOT . '/includes/locale.inc';
    locale_add_language('it', 'Italian', 'Italiano', LANGUAGE_LTR, '', '', TRUE, FALSE);

    // Enable URL language detection and selection.
    $edit = array('language[enabled][locale-url]' => '1');
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Set "Basic page" content type to use multilingual support.
    $edit = array(
      'language_content_type' => 1,
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    $this->assertRaw(t('The content type %type has been updated.', array('%type' => 'Basic page')), 'Basic page content type has been updated.');

    // Make node body translatable.
    $field = field_info_field('body');
    $field['translatable'] = TRUE;
    field_update_field($field);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
