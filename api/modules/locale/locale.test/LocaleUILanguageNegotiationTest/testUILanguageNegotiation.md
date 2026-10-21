# LocaleUILanguageNegotiationTest::testUILanguageNegotiation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2371–2516 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2371-L2516)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
- **Module/theme:** locale

## Signature

```php
function testUILanguageNegotiation()
```

## Documentation

```text
Tests for language switching by URL path.
```

## Code

```php
  function testUILanguageNegotiation() {
    // A few languages to switch to.
    // This one is unknown, should get the default lang version.
    $language_unknown = 'blah-blah';
    // For testing browser lang preference.
    $language_browser_fallback = 'vi';
    // For testing path prefix.
    $language = 'zh-hans';
    // For setting browser language preference to 'vi'.
    $http_header_browser_fallback = array("Accept-Language: $language_browser_fallback;q=1");
    // For setting browser language preference to some unknown.
    $http_header_blah = array("Accept-Language: blah;q=1");

    // This domain should switch the UI to Chinese.
    $language_domain = 'example.cn';

    // Setup the site languages by installing two languages.
    require_once DRUPAL_ROOT . '/includes/locale.inc';
    locale_add_language($language_browser_fallback);
    locale_add_language($language);

    // We will look for this string in the admin/config screen to see if the
    // corresponding translated string is shown.
    $default_string = 'Configure languages for content and the user interface';

    // Set the default language in order for the translated string to be registered
    // into database when seen by t(). Without doing this, our target string
    // is for some reason not found when doing translate search. This might
    // be some bug.
    drupal_static_reset('language_list');
    $languages = language_list('enabled');
    variable_set('language_default', $languages[1]['vi']);
    // First visit this page to make sure our target string is searchable.
    $this->drupalGet('admin/config');
    // Now the t()'ed string is in db so switch the language back to default.
    variable_del('language_default');

    // Translate the string.
    $language_browser_fallback_string = "In $language_browser_fallback In $language_browser_fallback In $language_browser_fallback";
    $language_string = "In $language In $language In $language";
    // Do a translate search of our target string.
    $edit = array( 'string' => $default_string);
    $this->drupalPost('admin/config/regional/translate/translate', $edit, t('Filter'));
    // Should find the string and now click edit to post translated string.
    $this->clickLink('edit');
    $edit = array(
      "translations[$language_browser_fallback]" => $language_browser_fallback_string,
      "translations[$language]" => $language_string,
    );
    $this->drupalPost(NULL, $edit, t('Save translations'));

    // Configure URL language rewrite.
    variable_set('locale_language_negotiation_url_type', LANGUAGE_TYPE_INTERFACE);

    $tests = array(
      // Default, browser preference should have no influence.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LANGUAGE_NEGOTIATION_DEFAULT),
        'path' => 'admin/config',
        'expect' => $default_string,
        'expected_provider' => LANGUAGE_NEGOTIATION_DEFAULT,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (PATH) > DEFAULT: no language prefix, UI language is default and the browser language preference setting is not used.',
      ),
      // Language prefix.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LANGUAGE_NEGOTIATION_DEFAULT),
        'path' => "$language/admin/config",
        'expect' => $language_string,
        'expected_provider' => LOCALE_LANGUAGE_NEGOTIATION_URL,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (PATH) > DEFAULT: with language prefix, UI language is switched based on path prefix',
      ),
      // Default, go by browser preference.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LOCALE_LANGUAGE_NEGOTIATION_BROWSER),
        'path' => 'admin/config',
        'expect' => $language_browser_fallback_string,
        'expected_provider' => LOCALE_LANGUAGE_NEGOTIATION_BROWSER,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (PATH) > BROWSER: no language prefix, UI language is determined by browser language preference',
      ),
      // Prefix, switch to the language.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LOCALE_LANGUAGE_NEGOTIATION_BROWSER),
        'path' => "$language/admin/config",
        'expect' => $language_string,
        'expected_provider' => LOCALE_LANGUAGE_NEGOTIATION_URL,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (PATH) > BROWSER: with langage prefix, UI language is based on path prefix',
      ),
      // Default, browser language preference is not one of site's lang.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LOCALE_LANGUAGE_NEGOTIATION_BROWSER, LANGUAGE_NEGOTIATION_DEFAULT),
        'path' => 'admin/config',
        'expect' => $default_string,
        'expected_provider' => LANGUAGE_NEGOTIATION_DEFAULT,
        'http_header' => $http_header_blah,
        'message' => 'URL (PATH) > BROWSER > DEFAULT: no language prefix and browser language preference set to unknown language should use default language',
      ),
    );

    foreach ($tests as $test) {
      $this->runTest($test);
    }

    // Unknown language prefix should return 404.
    variable_set('language_negotiation_' . LANGUAGE_TYPE_INTERFACE, locale_language_negotiation_info());
    $this->drupalGet("$language_unknown/admin/config", array(), $http_header_browser_fallback);
    $this->assertResponse(404, "Unknown language path prefix should return 404");

    // Setup for domain negotiation, first configure the language to have domain
    // URL. We use HTTPS and a port to make sure that only the domain name is used.
    $edit = array('prefix' => '', 'domain' => "https://$language_domain:99");
    $this->drupalPost("admin/config/regional/language/edit/$language", $edit, t('Save language'));
    // Set the site to use domain language negotiation.

    $tests = array(
      // Default domain, browser preference should have no influence.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LANGUAGE_NEGOTIATION_DEFAULT),
        'locale_language_negotiation_url_part' => LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN,
        'path' => 'admin/config',
        'expect' => $default_string,
        'expected_provider' => LANGUAGE_NEGOTIATION_DEFAULT,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (DOMAIN) > DEFAULT: default domain should get default language',
      ),
      // Language domain specific URL, we set the $_SERVER['HTTP_HOST'] in
      // locale_test.module hook_boot() to simulate this.
      array(
        'language_negotiation' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LANGUAGE_NEGOTIATION_DEFAULT),
        'locale_language_negotiation_url_part' => LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN,
        'locale_test_domain' => $language_domain . ':88',
        'path' => 'admin/config',
        'expect' => $language_string,
        'expected_provider' => LOCALE_LANGUAGE_NEGOTIATION_URL,
        'http_header' => $http_header_browser_fallback,
        'message' => 'URL (DOMAIN) > DEFAULT: domain example.cn should switch to Chinese',
      ),
    );

    foreach ($tests as $test) {
      $this->runTest($test);
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
