# LocaleTranslationFunctionalTest::testJavaScriptTranslation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 480–550 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L480-L550)
- **Class:** [LocaleTranslationFunctionalTest](../LocaleTranslationFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testJavaScriptTranslation()
```

## Documentation

_No docblock in source._

## Code

```php
  function testJavaScriptTranslation() {
    $user = $this->drupalCreateUser(array('translate interface', 'administer languages', 'access administration pages'));
    $this->drupalLogin($user);

    $langcode = 'xx';
    // The English name for the language. This will be translated.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = $langcode;

    // Add custom language.
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));
    drupal_static_reset('language_list');

    // Build the JavaScript translation file.
    $this->drupalGet('admin/config/regional/translate/translate');

    // Retrieve the id of the first string available in the {locales_source}
    // table and translate it.
    $query = db_select('locales_source', 'l');
    $query->addExpression('min(l.lid)', 'lid');
    $result = $query->condition('l.location', '%.js%', 'LIKE')
      ->condition('l.textgroup', 'default')
      ->execute();
    $url = 'admin/config/regional/translate/edit/' . $result->fetchObject()->lid;
    $edit = array('translations['. $langcode .']' => $this->randomName());
    $this->drupalPost($url, $edit, t('Save translations'));

    // Trigger JavaScript translation parsing and building.
    require_once DRUPAL_ROOT . '/includes/locale.inc';
    _locale_rebuild_js($langcode);

    // Retrieve the JavaScript translation hash code for the custom language to
    // check that the translation file has been properly built.
    $file = db_select('languages', 'l')
      ->fields('l', array('javascript'))
      ->condition('language', $langcode)
      ->execute()
      ->fetchObject();
    $js_file = 'public://' . variable_get('locale_js_directory', 'languages') . '/' . $langcode . '_' . $file->javascript . '.js';
    $this->assertTrue($result = file_exists($js_file), format_string('JavaScript file created: %file', array('%file' => $result ? $js_file : 'not found')));

    // Test JavaScript translation rebuilding.
    file_unmanaged_delete($js_file);
    $this->assertTrue($result = !file_exists($js_file), format_string('JavaScript file deleted: %file', array('%file' => $result ? $js_file : 'found')));
    cache_clear_all();
    _locale_rebuild_js($langcode);
    $this->assertTrue($result = file_exists($js_file), format_string('JavaScript file rebuilt: %file', array('%file' => $result ? $js_file : 'not found')));

    // Test if JavaScript translation contains a custom string override.
    $string_override = $this->randomName();
    variable_set('locale_custom_strings_' . $langcode, array('' => array($string_override => $string_override)));
    _locale_rebuild_js($langcode);
    $file = db_select('languages', 'l')
      ->fields('l', array('javascript'))
      ->condition('language', $langcode)
      ->execute()
      ->fetchObject();
    $js_file = 'public://' . variable_get('locale_js_directory', 'languages') . '/' . $langcode . '_' . $file->javascript . '.js';
    $content = file_get_contents($js_file);
    $this->assertTrue(strpos($content, '"' . $string_override . '":"' . $string_override . '"') > 0);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
