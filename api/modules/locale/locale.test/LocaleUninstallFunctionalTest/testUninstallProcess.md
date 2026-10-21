# LocaleUninstallFunctionalTest::testUninstallProcess()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1484–1578 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1484-L1578)
- **Class:** [LocaleUninstallFunctionalTest](../LocaleUninstallFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testUninstallProcess()
```

## Documentation

```text
Check if the values of the Locale variables are correct after uninstall.
```

## Code

```php
  function testUninstallProcess() {
    $locale_module = array('locale');

    // Add a new language and optionally set it as default.
    require_once DRUPAL_ROOT . '/includes/locale.inc';
    locale_add_language('fr', 'French', 'Français', LANGUAGE_LTR, '', '', TRUE, $this->language == 'fr');

    // Check the UI language.
    drupal_language_initialize();
    global $language;
    $this->assertEqual($language->language, $this->language, format_string('Current language: %lang', array('%lang' => $language->language)));

    // Enable multilingual workflow option for articles.
    variable_set('language_content_type_article', 1);

    // Change JavaScript translations directory.
    variable_set('locale_js_directory', 'js_translations');

    // Build the JavaScript translation file for French.
    $user = $this->drupalCreateUser(array('translate interface', 'access administration pages'));
    $this->drupalLogin($user);
    $this->drupalGet('admin/config/regional/translate/translate');
    $string = db_query('SELECT min(lid) AS lid FROM {locales_source} WHERE location LIKE :location AND textgroup = :textgroup', array(
      ':location' => '%.js%',
      ':textgroup' => 'default',
    ))->fetchObject();
    $edit = array('translations[fr]' => 'french translation');
    $this->drupalPost('admin/config/regional/translate/edit/' . $string->lid, $edit, t('Save translations'));
    _locale_rebuild_js('fr');
    $file = db_query('SELECT javascript FROM {languages} WHERE language = :language', array(':language' => 'fr'))->fetchObject();
    $js_file = 'public://' . variable_get('locale_js_directory', 'languages') . '/fr_' . $file->javascript . '.js';
    $this->assertTrue($result = file_exists($js_file), format_string('JavaScript file created: %file', array('%file' => $result ? $js_file : 'none')));

    // Disable string caching.
    variable_set('locale_cache_strings', 0);

    // Change language negotiation options.
    drupal_load('module', 'locale');
    variable_set('language_types', drupal_language_types() + array('language_custom' => TRUE));
    variable_set('language_negotiation_' . LANGUAGE_TYPE_INTERFACE, locale_language_negotiation_info());
    variable_set('language_negotiation_' . LANGUAGE_TYPE_CONTENT, locale_language_negotiation_info());
    variable_set('language_negotiation_' . LANGUAGE_TYPE_URL, locale_language_negotiation_info());

    // Change language providers settings.
    variable_set('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX);
    variable_set('locale_language_negotiation_session_param', TRUE);

    // Uninstall Locale.
    module_disable($locale_module);
    drupal_uninstall_modules($locale_module);

    // Visit the front page.
    $this->drupalGet('');

    // Check the init language logic.
    drupal_language_initialize();
    $this->assertEqual($language->language, 'en', format_string('Language after uninstall: %lang', array('%lang' => $language->language)));

    // Check JavaScript files deletion.
    $this->assertTrue($result = !file_exists($js_file), format_string('JavaScript file deleted: %file', array('%file' => $result ? $js_file : 'found')));

    // Check language count.
    $language_count = variable_get('language_count', 1);
    $this->assertEqual($language_count, 1, format_string('Language count: %count', array('%count' => $language_count)));

    // Check language negotiation.
    require_once DRUPAL_ROOT . '/includes/language.inc';
    $this->assertTrue(count(language_types()) == count(drupal_language_types()), 'Language types reset');
    $language_negotiation = language_negotiation_get(LANGUAGE_TYPE_INTERFACE) == LANGUAGE_NEGOTIATION_DEFAULT;
    $this->assertTrue($language_negotiation, format_string('Interface language negotiation: %setting', array('%setting' => $language_negotiation ? 'none' : 'set')));
    $language_negotiation = language_negotiation_get(LANGUAGE_TYPE_CONTENT) == LANGUAGE_NEGOTIATION_DEFAULT;
    $this->assertTrue($language_negotiation, format_string('Content language negotiation: %setting', array('%setting' => $language_negotiation ? 'none' : 'set')));
    $language_negotiation = language_negotiation_get(LANGUAGE_TYPE_URL) == LANGUAGE_NEGOTIATION_DEFAULT;
    $this->assertTrue($language_negotiation, format_string('URL language negotiation: %setting', array('%setting' => $language_negotiation ? 'none' : 'set')));

    // Check language providers settings.
    $this->assertFalse(variable_get('locale_language_negotiation_url_part', FALSE), 'URL language provider indicator settings cleared.');
    $this->assertFalse(variable_get('locale_language_negotiation_session_param', FALSE), 'Visit language provider settings cleared.');

    // Check JavaScript parsed.
    $javascript_parsed_count = count(variable_get('javascript_parsed', array()));
    $this->assertEqual($javascript_parsed_count, 0, format_string('JavaScript parsed count: %count', array('%count' => $javascript_parsed_count)));

    // Check multilingual workflow option for articles.
    $multilingual = variable_get('language_content_type_article', 0);
    $this->assertEqual($multilingual, 0, format_string('Multilingual workflow option: %status', array('%status' => $multilingual ? 'enabled': 'disabled')));

    // Check JavaScript translations directory.
    $locale_js_directory = variable_get('locale_js_directory', 'languages');
    $this->assertEqual($locale_js_directory, 'languages', format_string('JavaScript translations directory: %dir', array('%dir' => $locale_js_directory)));

    // Check string caching.
    $locale_cache_strings = variable_get('locale_cache_strings', 1);
    $this->assertEqual($locale_cache_strings, 1, format_string('String caching: %status', array('%status' => $locale_cache_strings ? 'enabled': 'disabled')));
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
