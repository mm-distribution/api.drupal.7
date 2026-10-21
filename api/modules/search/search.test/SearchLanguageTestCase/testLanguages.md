# SearchLanguageTestCase::testLanguages()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2001–2040 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2001-L2040)
- **Class:** [SearchLanguageTestCase](../SearchLanguageTestCase.md)
- **Module/theme:** search

## Signature

```php
function testLanguages()
```

## Documentation

_No docblock in source._

## Code

```php
  function testLanguages() {
    // Check that there are initially no languages displayed.
    $this->drupalGet('search/node');
    $this->assertNoText(t('Languages'), 'No languages to choose from.');

    // Add predefined language.
    $edit = array('langcode' => 'fr');
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));
    $this->assertText('fr', 'Language added successfully.');

    // Now we should have languages displayed.
    $this->drupalGet('search/node');
    $this->assertText(t('Languages'), 'Languages displayed to choose from.');
    $this->assertText(t('English'), 'English is a possible choice.');
    $this->assertText(t('French'), 'French is a possible choice.');

    // Ensure selecting no language does not make the query different.
    $this->drupalPost('search/node', array(), t('Advanced search'));
    $this->assertEqual($this->getUrl(), url('search/node/', array('absolute' => TRUE)), 'Correct page redirection, no language filtering.');

    // Pick French and ensure it is selected.
    $edit = array('language[fr]' => TRUE);
    $this->drupalPost('search/node', $edit, t('Advanced search'));
    $this->assertFieldByXPath('//input[@name="keys"]', 'language:fr', 'Language filter added to query.');

    // Change the default language and disable English.
    $path = 'admin/config/regional/language';
    $this->drupalGet($path);
    $this->assertFieldChecked('edit-site-default-en', 'English is the default language.');
    $edit = array('site_default' => 'fr');
    $this->drupalPost(NULL, $edit, t('Save configuration'));
    $this->assertNoFieldChecked('edit-site-default-en', 'Default language updated.');
    $edit = array('enabled[en]' => FALSE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));
    $this->assertNoFieldChecked('edit-enabled-en', 'Language disabled.');

    // Check that there are again no languages displayed.
    $this->drupalGet('search/node');
    $this->assertNoText(t('Languages'), 'No languages to choose from.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
