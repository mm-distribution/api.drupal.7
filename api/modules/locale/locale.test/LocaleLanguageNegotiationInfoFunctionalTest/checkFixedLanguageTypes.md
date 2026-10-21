# LocaleLanguageNegotiationInfoFunctionalTest::checkFixedLanguageTypes()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3231–3240 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3231-L3240)
- **Class:** [LocaleLanguageNegotiationInfoFunctionalTest](../LocaleLanguageNegotiationInfoFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
private function checkFixedLanguageTypes()
```

## Documentation

```text
Check that language negotiation for fixed types matches the stored one.
```

## Code

```php
  private function checkFixedLanguageTypes() {
    drupal_static_reset('language_types_info');
    foreach (language_types_info() as $type => $info) {
      if (isset($info['fixed'])) {
        $negotiation = variable_get("language_negotiation_$type", array());
        $equal = array_keys($negotiation) === array_values($info['fixed']);
        $this->assertTrue($equal, format_string('language negotiation for %type is properly set up', array('%type' => $type)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
