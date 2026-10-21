# LocaleTranslationFunctionalTest::testStringSearch()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 619–779 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L619-L779)
- **Class:** [LocaleTranslationFunctionalTest](../LocaleTranslationFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testStringSearch()
```

## Documentation

```text
Tests translation search form.
```

## Code

```php
  function testStringSearch() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    // User to translate and delete string.
    $translate_user = $this->drupalCreateUser(array('translate interface', 'access administration pages'));

    // Code for the language.
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
    // This will be the translation of $name.
    $translation = $this->randomName(16);

    // Add custom language.
    $this->drupalLogin($admin_user);
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
    locale_reset();
    $this->drupalLogout();

    // Search for the name.
    $this->drupalLogin($translate_user);
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // assertText() seems to remove the input field where $name always could be
    // found, so this is not a false assert. See how assertNoText succeeds
    // later.
    $this->assertText($name, 'Search found the string.');

    // Ensure untranslated string doesn't appear if searching on 'only
    // translated strings'.
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'translated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), "Search didn't find the string.");

    // Ensure untranslated string appears if searching on 'only untranslated
    // strings' in "all" (hasn't been translated to any language).
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'untranslated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'Search found the string.');

    // Ensure untranslated string appears if searching on 'only untranslated
    // strings' in the custom language (hasn't been translated to that specific language).
    $search = array(
      'string' => $name,
      'language' => $langcode,
      'translation' => 'untranslated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'Search found the string.');

    // Add translation.
    // Assume this is the only result, given the random name.
    $this->clickLink(t('edit'));
    // We save the lid from the path.
    $matches = array();
    preg_match('!admin/config/regional/translate/edit/(\d)+!', $this->getUrl(), $matches);
    $lid = $matches[1];
    $edit = array(
      "translations[$langcode]" => $translation,
    );
    $this->drupalPost(NULL, $edit, t('Save translations'));

    // Ensure translated string does appear if searching on 'only
    // translated strings'.
    $search = array(
      'string' => $translation,
      'language' => 'all',
      'translation' => 'translated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'Search found the translation.');

    // Ensure translated source string doesn't appear if searching on 'only
    // untranslated strings'.
    $search = array(
      'string' => $name,
      'language' => 'all',
      'translation' => 'untranslated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), "Search didn't find the source string.");

    // Ensure translated string doesn't appear if searching on 'only
    // untranslated strings'.
    $search = array(
      'string' => $translation,
      'language' => 'all',
      'translation' => 'untranslated',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), "Search didn't find the translation.");

    // Ensure translated string does appear if searching on the custom language.
    $search = array(
      'string' => $translation,
      'language' => $langcode,
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertNoText(t('No strings available.'), 'Search found the translation.');

    // Ensure translated string doesn't appear if searching on English.
    $search = array(
      'string' => $translation,
      'language' => 'en',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), "Search didn't find the translation.");

    // Search for a string that isn't in the system.
    $unavailable_string = $this->randomName(16);
    $search = array(
      'string' => $unavailable_string,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    $this->assertText(t('No strings available.'), "Search didn't find the invalid string.");
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
