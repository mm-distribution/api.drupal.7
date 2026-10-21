# LocaleUILanguageNegotiationTest::runTest()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2518–2532 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2518-L2532)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
- **Module/theme:** locale

## Signature

```php
private function runTest($test)
```

## Documentation

_No docblock in source._

## Code

```php
  private function runTest($test) {
    if (!empty($test['language_negotiation'])) {
      $negotiation = array_flip($test['language_negotiation']);
      language_negotiation_set(LANGUAGE_TYPE_INTERFACE, $negotiation);
    }
    if (!empty($test['locale_language_negotiation_url_part'])) {
      variable_set('locale_language_negotiation_url_part', $test['locale_language_negotiation_url_part']);
    }
    if (!empty($test['locale_test_domain'])) {
      variable_set('locale_test_domain', $test['locale_test_domain']);
    }
    $this->drupalGet($test['path'], array(), $test['http_header']);
    $this->assertText($test['expect'], $test['message']);
    $this->assertText(t('Language negotiation provider: @name', array('@name' => $test['expected_provider'])));
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
