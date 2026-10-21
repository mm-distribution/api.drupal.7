# locale_translate_import_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 928–977 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L928-L977)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translate_import_form($form)
```

## Documentation

```text
User interface for the translation import screen.
```

## Code

```php
function locale_translate_import_form($form) {
  // Get all languages, except English
  drupal_static_reset('language_list');
  $names = locale_language_list('name');
  unset($names['en']);

  if (!count($names)) {
    $languages = _locale_prepare_predefined_list();
    $default = key($languages);
  }
  else {
    $languages = array(
      t('Already added languages') => $names,
      t('Languages not yet added') => _locale_prepare_predefined_list()
    );
    $default = key($names);
  }

  $form['import'] = array('#type' => 'fieldset',
    '#title' => t('Import translation'),
  );
  $form['import']['file'] = array('#type' => 'file',
    '#title' => t('Language file'),
    '#size' => 50,
    '#description' => t('A Gettext Portable Object (<em>.po</em>) file.'),
  );
  $form['import']['langcode'] = array('#type' => 'select',
    '#title' => t('Import into'),
    '#options' => $languages,
    '#default_value' => $default,
    '#description' => t('Choose the language you want to add strings into. If you choose a language which is not yet set up, it will be added.'),
  );
  $form['import']['group'] = array('#type' => 'radios',
    '#title' => t('Text group'),
    '#default_value' => 'default',
    '#options' => module_invoke_all('locale', 'groups'),
    '#description' => t('Imported translations will be added to this text group.'),
  );
  $form['import']['mode'] = array('#type' => 'radios',
    '#title' => t('Mode'),
    '#default_value' => LOCALE_IMPORT_KEEP,
    '#options' => array(
      LOCALE_IMPORT_OVERWRITE => t('Strings in the uploaded file replace existing ones, new ones are added. The plural format is updated.'),
      LOCALE_IMPORT_KEEP => t('Existing strings and the plural format are kept, only new strings are added.')
    ),
  );
  $form['import']['submit'] = array('#type' => 'submit', '#value' => t('Import'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
