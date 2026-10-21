# LocaleUrlRewritingTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2643–2672 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2643-L2672)
- **Class:** [LocaleUrlRewritingTest](../LocaleUrlRewritingTest.md)
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

    // Create and login user.
    $this->web_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    $this->drupalLogin($this->web_user);

    // Install French language.
    $edit = array();
    $edit['langcode'] = 'fr';
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Install Italian language.
    $edit = array();
    $edit['langcode'] = 'it';
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Disable Italian language.
    $edit = array('enabled[it]' => FALSE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));

    // Enable URL language detection and selection.
    $edit = array('language[enabled][locale-url]' => 1);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Reset static caching.
    drupal_static_reset('language_list');
    drupal_static_reset('locale_url_outbound_alter');
    drupal_static_reset('locale_language_url_rewrite_url');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
