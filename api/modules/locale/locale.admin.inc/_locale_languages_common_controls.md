# _locale_languages_common_controls()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 260–319 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L260-L319)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function _locale_languages_common_controls(&$form, $language = NULL)
```

## Documentation

```text
Common elements of the language addition and editing form.

@param $form
  A parent form item (or empty array) to add items below.
@param $language
  Language object to edit.
```

## Code

```php
function _locale_languages_common_controls(&$form, $language = NULL) {
  if (!is_object($language)) {
    $language = new stdClass();
  }
  if (isset($language->language)) {
    $form['langcode_view'] = array(
      '#type' => 'item',
      '#title' => t('Language code'),
      '#markup' => $language->language
    );
    $form['langcode'] = array(
      '#type' => 'value',
      '#value' => $language->language
    );
  }
  else {
    $form['langcode'] = array('#type' => 'textfield',
      '#title' => t('Language code'),
      '#maxlength' => 12,
      '#required' => TRUE,
      '#default_value' => @$language->language,
      '#disabled' => (isset($language->language)),
      '#description' => t('Use language codes as <a href="@w3ctags">defined by the W3C</a> for interoperability. <em>Examples: "en", "en-gb" and "zh-hant".</em>', array('@w3ctags' => 'http://www.w3.org/International/articles/language-tags/')),
    );
  }
  $form['name'] = array('#type' => 'textfield',
    '#title' => t('Language name in English'),
    '#maxlength' => 64,
    '#default_value' => @$language->name,
    '#required' => TRUE,
    '#description' => t('Name of the language in English. Will be available for translation in all languages.'),
  );
  $form['native'] = array('#type' => 'textfield',
    '#title' => t('Native language name'),
    '#maxlength' => 64,
    '#default_value' => @$language->native,
    '#required' => TRUE,
    '#description' => t('Name of the language in the language being added.'),
  );
  $form['prefix'] = array('#type' => 'textfield',
    '#title' => t('Path prefix language code'),
    '#maxlength' => 64,
    '#default_value' => @$language->prefix,
    '#description' => t('Language code or other custom text to use as a path prefix for URL language detection, if your <em>Detection and selection</em> settings use URL path prefixes. For the default language, this value may be left blank. <strong>Modifying this value may break existing URLs. Use with caution in a production environment.</strong> Example: Specifying "deutsch" as the path prefix code for German results in URLs like "example.com/deutsch/contact".')
  );
  $form['domain'] = array('#type' => 'textfield',
    '#title' => t('Language domain'),
    '#maxlength' => 128,
    '#default_value' => @$language->domain,
    '#description' => t('The domain name to use for this language if URL domains are used for <em>Detection and selection</em>. Leave blank for the default language. <strong>Changing this value may break existing URLs.</strong> Example: Specifying "de.example.com" as language domain for German will result in an URL like "http://de.example.com/contact".'),
  );
  $form['direction'] = array('#type' => 'radios',
    '#title' => t('Direction'),
    '#required' => TRUE,
    '#description' => t('Direction that text in this language is presented.'),
    '#default_value' => @$language->direction,
    '#options' => array(LANGUAGE_LTR => t('Left to right'), LANGUAGE_RTL => t('Right to left'))
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
