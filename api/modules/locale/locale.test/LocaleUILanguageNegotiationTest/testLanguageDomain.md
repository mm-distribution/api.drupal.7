# LocaleUILanguageNegotiationTest::testLanguageDomain()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2581–2626 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2581-L2626)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
- **Module/theme:** locale

## Signature

```php
function testLanguageDomain()
```

## Documentation

```text
Tests url() when separate domains are used for multiple languages.
```

## Code

```php
  function testLanguageDomain() {
    // Add the Italian language, without protocol.
    $langcode = 'it';
    locale_add_language($langcode, 'Italian', 'Italian', LANGUAGE_LTR, 'it.example.com', '', TRUE, FALSE);

    // Add the French language, with protocol.
    $langcode = 'fr';
    locale_add_language($langcode, 'French', 'French', LANGUAGE_LTR, 'http://fr.example.com', '', TRUE, FALSE);

    // Enable language URL detection.
    $negotiation = array_flip(array(LOCALE_LANGUAGE_NEGOTIATION_URL, LANGUAGE_NEGOTIATION_DEFAULT));
    language_negotiation_set(LANGUAGE_TYPE_INTERFACE, $negotiation);

    variable_set('locale_language_negotiation_url_part', 1);

    global $is_https;
    $languages = language_list();

    foreach (array('it', 'fr') as $langcode) {
      // Build the link we're going to test based on the clean URL setting.
      $link = (!empty($GLOBALS['conf']['clean_url'])) ? $langcode . '.example.com/admin' : $langcode . '.example.com/?q=admin';

      // Test URL in another language.
      // Base path gives problems on the testbot, so $correct_link is hard-coded.
      // @see UrlAlterFunctionalTest::assertUrlOutboundAlter (path.test).
      $url = url('admin', array('language' => $languages[$langcode]));
      $url_scheme = ($is_https) ? 'https://' : 'http://';
      $correct_link = $url_scheme . $link;
      $this->assertTrue($url == $correct_link, format_string('The url() function returns the right url (@url) in accordance with the chosen language', array('@url' => $url . " == " . $correct_link)));

      // Test HTTPS via options.
      variable_set('https', TRUE);
      $url = url('admin', array('https' => TRUE, 'language' => $languages[$langcode]));
      $correct_link = 'https://' . $link;
      $this->assertTrue($url == $correct_link, format_string('The url() function returns the right https url (via options) (@url) in accordance with the chosen language', array('@url' => $url . " == " . $correct_link)));
      variable_set('https', FALSE);

      // Test HTTPS via current URL scheme.
      $temp_https = $is_https;
      $is_https = TRUE;
      $url = url('admin', array('language' => $languages[$langcode]));
      $correct_link = 'https://' . $link;
      $this->assertTrue($url == $correct_link, format_string('The url() function returns the right url (via current url scheme) (@url) in accordance with the chosen language', array('@url' => $url . " == " . $correct_link)));
      $is_https = $temp_https;
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
