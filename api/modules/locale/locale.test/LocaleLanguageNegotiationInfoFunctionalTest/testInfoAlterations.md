# LocaleLanguageNegotiationInfoFunctionalTest::testInfoAlterations()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3116–3197 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3116-L3197)
- **Class:** [LocaleLanguageNegotiationInfoFunctionalTest](../LocaleLanguageNegotiationInfoFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testInfoAlterations()
```

## Documentation

```text
Tests alterations to language types/negotiation info.
```

## Code

```php
  function testInfoAlterations() {
    // Enable language type/negotiation info alterations.
    variable_set('locale_test_language_types', TRUE);
    variable_set('locale_test_language_negotiation_info', TRUE);
    $this->languageNegotiationUpdate();

    // Check that fixed language types are properly configured without the need
    // of saving the language negotiation settings.
    $this->checkFixedLanguageTypes();

    // Make the content language type configurable by updating the language
    // negotiation settings with the proper flag enabled.
    variable_set('locale_test_content_language_type', TRUE);
    $this->languageNegotiationUpdate();
    $type = LANGUAGE_TYPE_CONTENT;
    $language_types = variable_get('language_types', drupal_language_types());
    $this->assertTrue($language_types[$type], 'Content language type is configurable.');

    // Enable some core and custom language providers. The test language type is
    // supposed to be configurable.
    $test_type = 'test_language_type';
    $provider = LOCALE_LANGUAGE_NEGOTIATION_INTERFACE;
    $test_provider = 'test_language_provider';
    $form_field = $type . '[enabled]['. $provider .']';
    $edit = array(
      $form_field => TRUE,
      $type . '[enabled][' . $test_provider . ']' => TRUE,
      $test_type . '[enabled][' . $test_provider . ']' => TRUE,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Remove the interface language provider by updating the language
    // negotiation settings with the proper flag enabled.
    variable_set('locale_test_language_negotiation_info_alter', TRUE);
    $this->languageNegotiationUpdate();
    $negotiation = variable_get("language_negotiation_$type", array());
    $this->assertFalse(isset($negotiation[$provider]), 'Interface language provider removed from the stored settings.');
    $this->assertNoFieldByXPath("//input[@name=\"$form_field\"]", NULL, 'Interface language provider unavailable.');

    // Check that type-specific language providers can be assigned only to the
    // corresponding language types.
    foreach (language_types_configurable() as $type) {
      $form_field = $type . '[enabled][test_language_provider_ts]';
      if ($type == $test_type) {
        $this->assertFieldByXPath("//input[@name=\"$form_field\"]", NULL, format_string('Type-specific test language provider available for %type.', array('%type' => $type)));
      }
      else {
        $this->assertNoFieldByXPath("//input[@name=\"$form_field\"]", NULL, format_string('Type-specific test language provider unavailable for %type.', array('%type' => $type)));
      }
    }

    // Check language negotiation results.
    $this->drupalGet('');
    $last = variable_get('locale_test_language_negotiation_last', array());
    foreach (language_types() as $type) {
      $langcode = $last[$type];
      $value = $type == LANGUAGE_TYPE_CONTENT || strpos($type, 'test') !== FALSE ? 'it' : 'en';
      $this->assertEqual($langcode, $value, format_string('The negotiated language for %type is %language', array('%type' => $type, '%language' => $langcode)));
    }

    // Disable locale_test and check that everything is set back to the original
    // status.
    $this->languageNegotiationUpdate('disable');

    // Check that only the core language types are available.
    foreach (language_types() as $type) {
      $this->assertTrue(strpos($type, 'test') === FALSE, format_string('The %type language is still available', array('%type' => $type)));
    }

    // Check that fixed language types are properly configured, even those
    // previously set to configurable.
    $this->checkFixedLanguageTypes();

    // Check that unavailable language providers are not present in the
    // negotiation settings.
    $negotiation = variable_get("language_negotiation_$type", array());
    $this->assertFalse(isset($negotiation[$test_provider]), 'The disabled test language provider is not part of the content language negotiation settings.');

    // Check that configuration page presents the correct options and settings.
    $this->assertNoRaw(t('Test language detection'), 'No test language type configuration available.');
    $this->assertNoRaw(t('This is a test language provider'), 'No test language provider available.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
