# LocaleUILanguageNegotiationTest::testUrlLanguageFallback()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2537–2576 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2537-L2576)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
- **Module/theme:** locale

## Signature

```php
function testUrlLanguageFallback()
```

## Documentation

```text
Test URL language detection when the requested URL has no language.
```

## Code

```php
  function testUrlLanguageFallback() {
    // Add the Italian language.
    $language_browser_fallback = 'it';
    locale_add_language($language_browser_fallback);
    $languages = language_list();

    // Enable the path prefix for the default language: this way any unprefixed
    // URL must have a valid fallback value.
    $edit = array('prefix' => 'en');
    $this->drupalPost('admin/config/regional/language/edit/en', $edit, t('Save language'));

    // Enable browser and URL language detection.
    $edit = array(
      'language[enabled][locale-browser]' => TRUE,
      'language[enabled][locale-url]' => TRUE,
      'language[weight][locale-browser]' => -8,
      'language[weight][locale-url]' => -10,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));
    $this->drupalGet('admin/config/regional/language/configure');

    // Enable the language switcher block.
    $edit = array('blocks[locale_language][region]' => 'sidebar_first');
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Access the front page without specifying any valid URL language prefix
    // and having as browser language preference a non-default language.
    $http_header = array("Accept-Language: $language_browser_fallback;q=1");
    $this->drupalGet('', array(), $http_header);

    // Check that the language switcher active link matches the given browser
    // language.
    $args = array(':url' => base_path() . (!empty($GLOBALS['conf']['clean_url']) ? $language_browser_fallback : "?q=$language_browser_fallback"));
    $fields = $this->xpath('//div[@id="block-locale-language"]//a[@class="language-link active" and @href=:url]', $args);
    $this->assertTrue($fields[0] == $languages[$language_browser_fallback]->native, 'The browser language is the URL active language');

    // Check that URLs are rewritten using the given browser language.
    $fields = $this->xpath('//div[@id="site-name"]//a[@rel="home" and @href=:url]//span', $args);
    $this->assertTrue($fields[0] == 'Drupal', 'URLs are rewritten using the browser language.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
