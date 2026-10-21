# LocaleTranslationFunctionalTest::testStringValidation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 555–614 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L555-L614)
- **Class:** [LocaleTranslationFunctionalTest](../LocaleTranslationFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testStringValidation()
```

## Documentation

```text
Tests the validation of the translation input.
```

## Code

```php
  function testStringValidation() {
    global $base_url;

    // User to add language and strings.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages', 'translate interface'));
    $this->drupalLogin($admin_user);
    $langcode = 'xx';
    // The English name for the language. This will be translated.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = $langcode;
    // This is the language indicator on the translation search screen for
    // untranslated strings. Copied straight from locale.inc.
    $language_indicator = "<em class=\"locale-untranslated\">$langcode</em> ";
    // These will be the invalid translations of $name.
    $key = $this->randomName(16);
    $bad_translations[$key] = "<script>alert('xss');</script>" . $key;
    $key = $this->randomName(16);
    $bad_translations[$key] = '<img SRC="javascript:alert(\'xss\');">' . $key;
    $key = $this->randomName(16);
    $bad_translations[$key] = '<<SCRIPT>alert("xss");//<</SCRIPT>' . $key;
    $key = $this->randomName(16);
    $bad_translations[$key] ="<BODY ONLOAD=alert('xss')>" . $key;

    // Add custom language.
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));
    // Add string.
    t($name, array(), array('langcode' => $langcode));
    // Reset locale cache.
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // Find the edit path.
    $content = $this->drupalGetContent();
    $this->assertTrue(preg_match('@(admin/config/regional/translate/edit/[0-9]+)@', $content, $matches), 'Found the edit path.');
    $path = $matches[0];
    foreach ($bad_translations as $key => $translation) {
      $edit = array(
        "translations[$langcode]" => $translation,
      );
      $this->drupalPost($path, $edit, t('Save translations'));
      // Check for a form error on the textarea.
      $form_class = $this->xpath('//form[@id="locale-translate-edit-form"]//textarea/@class');
      $this->assertNotIdentical(FALSE, strpos($form_class[0], 'error'), 'The string was rejected as unsafe.');
      $this->assertNoText(t('The string has been saved.'), 'The string was not saved.');
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
