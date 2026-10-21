# LocaleBrowserDetectionTest::testLanguageFromBrowser()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1706–1807 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1706-L1807)
- **Class:** [LocaleBrowserDetectionTest](../LocaleBrowserDetectionTest.md)
- **Module/theme:** locale

## Signature

```php
function testLanguageFromBrowser()
```

## Documentation

```text
Unit tests for the locale_language_from_browser() function.
```

## Code

```php
  function testLanguageFromBrowser() {
    // Load the required functions.
    require_once DRUPAL_ROOT . '/includes/locale.inc';

    $languages = array(
      // In our test case, 'en' has priority over 'en-US'.
      'en' => (object) array(
        'language' => 'en',
      ),
      'en-US' => (object) array(
        'language' => 'en-US',
      ),
      // But 'fr-CA' has priority over 'fr'.
      'fr-CA' => (object) array(
        'language' => 'fr-CA',
      ),
      'fr' => (object) array(
        'language' => 'fr',
      ),
      // 'es-MX' is alone.
      'es-MX' => (object) array(
        'language' => 'es-MX',
      ),
      // 'pt' is alone.
      'pt' => (object) array(
        'language' => 'pt',
      ),
      // Language codes with more then one dash are actually valid.
      // eh-oh-laa-laa is the official language code of the Teletubbies.
      'eh-oh-laa-laa' => (object) array(
        'language' => 'eh-oh-laa-laa',
      ),
    );

    $test_cases = array(
      // Equal qvalue for each language, choose the site preferred one.
      'en,en-US,fr-CA,fr,es-MX' => 'en',
      'en-US,en,fr-CA,fr,es-MX' => 'en',
      'fr,en' => 'en',
      'en,fr' => 'en',
      'en-US,fr' => 'en',
      'fr,en-US' => 'en',
      'fr,fr-CA' => 'fr-CA',
      'fr-CA,fr' => 'fr-CA',
      'fr' => 'fr-CA',
      'fr;q=1' => 'fr-CA',
      'fr,es-MX' => 'fr-CA',
      'fr,es' => 'fr-CA',
      'es,fr' => 'fr-CA',
      'es-MX,de' => 'es-MX',
      'de,es-MX' => 'es-MX',

      // Different cases and whitespace.
      'en' => 'en',
      'En' => 'en',
      'EN' => 'en',
      ' en' => 'en',
      'en ' => 'en',
      'en, fr' => 'en',

      // A less specific language from the browser matches a more specific one
      // from the website, and the other way around for compatibility with
      // some versions of Internet Explorer.
      'es' => 'es-MX',
      'es-MX' => 'es-MX',
      'pt' => 'pt',
      'pt-PT' => 'pt',
      'pt-PT;q=0.5,pt-BR;q=1,en;q=0.7' => 'en',
      'pt-PT;q=1,pt-BR;q=0.5,en;q=0.7' => 'en',
      'pt-PT;q=0.4,pt-BR;q=0.1,en;q=0.7' => 'en',
      'pt-PT;q=0.1,pt-BR;q=0.4,en;q=0.7' => 'en',

      // Language code with several dashes are valid. The less specific language
      // from the browser matches the more specific one from the website.
      'eh-oh-laa-laa' => 'eh-oh-laa-laa',
      'eh-oh-laa' => 'eh-oh-laa-laa',
      'eh-oh' => 'eh-oh-laa-laa',
      'eh' => 'eh-oh-laa-laa',

      // Different qvalues.
      'fr,en;q=0.5' => 'fr-CA',
      'fr,en;q=0.5,fr-CA;q=0.25' => 'fr',

      // Silly wildcards are also valid.
      '*,fr-CA;q=0.5' => 'en',
      '*,en;q=0.25' => 'fr-CA',
      'en,en-US;q=0.5,fr;q=0.25' => 'en',
      'en-US,en;q=0.5,fr;q=0.25' => 'en-US',

      // Unresolvable cases.
      '' => FALSE,
      'de,pl' => FALSE,
      'iecRswK4eh' => FALSE,
      $this->randomName(10) => FALSE,
    );

    foreach ($test_cases as $accept_language => $expected_result) {
      $_SERVER['HTTP_ACCEPT_LANGUAGE'] = $accept_language;
      $result = locale_language_from_browser($languages);
      $this->assertIdentical($result, $expected_result, format_string("Language selection '@accept-language' selects '@result', result = '@actual'", array('@accept-language' => $accept_language, '@result' => $expected_result, '@actual' => isset($result) ? $result : 'none')));
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
