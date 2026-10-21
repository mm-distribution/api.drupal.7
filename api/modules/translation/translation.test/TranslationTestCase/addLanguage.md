# TranslationTestCase::addLanguage()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 286–315 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L286-L315)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function addLanguage($language_code)
```

## Documentation

```text
Installs the specified language, or enables it if it is already installed.

@param $language_code
  The language code to check.
```

## Code

```php
  function addLanguage($language_code) {
    // Check to make sure that language has not already been installed.
    $this->drupalGet('admin/config/regional/language');

    if (strpos($this->drupalGetContent(), 'enabled[' . $language_code . ']') === FALSE) {
      // Doesn't have language installed so add it.
      $edit = array();
      $edit['langcode'] = $language_code;
      $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

      // Make sure we are not using a stale list.
      drupal_static_reset('language_list');
      $languages = language_list('language');
      $this->assertTrue(array_key_exists($language_code, $languages), 'Language was installed successfully.');

      if (array_key_exists($language_code, $languages)) {
        $this->assertRaw(t('The language %language has been created and can now be used. More information is available on the <a href="@locale-help">help screen</a>.', array('%language' => $languages[$language_code]->name, '@locale-help' => url('admin/help/locale'))), 'Language has been created.');
      }
    }
    elseif ($this->xpath('//input[@type="checkbox" and @name=:name and @checked="checked"]', array(':name' => 'enabled[' . $language_code . ']'))) {
      // It's installed and enabled. No need to do anything.
      $this->assertTrue(true, 'Language [' . $language_code . '] already installed and enabled.');
    }
    else {
      // It's installed but not enabled. Enable it.
      $this->assertTrue(true, 'Language [' . $language_code . '] already installed.');
      $this->drupalPost(NULL, array('enabled[' . $language_code . ']' => TRUE), t('Save configuration'));
      $this->assertRaw(t('Configuration saved.'), 'Language successfully enabled.');
    }
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
