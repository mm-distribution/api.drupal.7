# PathMonolingualTestCase::setUp()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 568–599 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L568-L599)
- **Class:** [PathMonolingualTestCase](../PathMonolingualTestCase.md)
- **Module/theme:** path

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    global $language;
    parent::setUp('path', 'locale', 'translation');

    // Create and login user.
    $web_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    $this->drupalLogin($web_user);

    // Enable French language.
    $edit = array();
    $edit['langcode'] = 'fr';
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Make French the default language.
    $edit = array('site_default' => 'fr');
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));

    // Disable English.
    $edit = array('enabled[en]' => FALSE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));

    // Verify that French is the only language.
    $this->assertFalse(drupal_multilingual(), 'Site is mono-lingual');
    $this->assertEqual(language_default('language'), 'fr', 'French is the default language');

    // Set language detection to URL.
    $edit = array('language[enabled][locale-url]' => TRUE);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Force languages to be initialized.
    drupal_language_initialize();
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
