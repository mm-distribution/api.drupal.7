# TranslationTestCase::setUp()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 24–63 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L24-L63)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale', 'translation', 'translation_test');

    // Setup users.
    $this->admin_user = $this->drupalCreateUser(array('bypass node access', 'administer nodes', 'administer languages', 'administer content types', 'administer blocks', 'access administration pages', 'translate content'));
    $this->translator = $this->drupalCreateUser(array('create page content', 'edit own page content', 'translate content'));

    $this->drupalLogin($this->admin_user);

    // Add languages.
    $this->addLanguage('en');
    $this->addLanguage('es');
    $this->addLanguage('it');

    // Disable Italian to test the translation behavior with disabled languages.
    $edit = array('enabled[it]' => FALSE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));

    // Set "Basic page" content type to use multilingual support with
    // translation.
    $this->drupalGet('admin/structure/types/manage/page');
    $edit = array();
    $edit['language_content_type'] = 2;
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    $this->assertRaw(t('The content type %type has been updated.', array('%type' => 'Basic page')), 'Basic page content type has been updated.');

    // Enable the language switcher block.
    $language_type = LANGUAGE_TYPE_INTERFACE;
    $edit = array("blocks[locale_$language_type][region]" => 'sidebar_first');
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Enable URL language detection and selection to make the language switcher
    // block appear.
    $edit = array('language[enabled][locale-url]' => TRUE);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));
    $this->assertRaw(t('Language negotiation configuration saved.'), 'URL language detection enabled.');
    $this->resetCaches();

    $this->drupalLogin($this->translator);
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
