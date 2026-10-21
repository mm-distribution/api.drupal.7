# locale_languages_edit_form_validate()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 375–399 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L375-L399)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_edit_form_validate($form, &$form_state)
```

## Documentation

```text
Validate the language editing form. Reused for custom language addition too.
```

## Code

```php
function locale_languages_edit_form_validate($form, &$form_state) {
  // Ensure sane field values for langcode, name, and native.
  if (!isset($form['langcode_view']) && preg_match('@[^a-zA-Z_-]@', $form_state['values']['langcode'])) {
    form_set_error('langcode', t('%field may only contain characters a-z, underscores, or hyphens.', array('%field' => $form['langcode']['#title'])));
  }
  if ($form_state['values']['name'] != check_plain($form_state['values']['name'])) {
    form_set_error('name', t('%field cannot contain any markup.', array('%field' => $form['name']['#title'])));
  }
  if ($form_state['values']['native'] != check_plain($form_state['values']['native'])) {
    form_set_error('native', t('%field cannot contain any markup.', array('%field' => $form['native']['#title'])));
  }

  if (!empty($form_state['values']['domain']) && !empty($form_state['values']['prefix'])) {
    form_set_error('prefix', t('Domain and path prefix values should not be set at the same time.'));
  }
  if (!empty($form_state['values']['domain']) && $duplicate = db_query("SELECT language FROM {languages} WHERE domain = :domain AND language <> :language", array(':domain' => $form_state['values']['domain'], ':language' => $form_state['values']['langcode']))->fetchField()) {
    form_set_error('domain', t('The domain (%domain) is already tied to a language (%language).', array('%domain' => $form_state['values']['domain'], '%language' => $duplicate)));
  }
  if (empty($form_state['values']['prefix']) && language_default('language') != $form_state['values']['langcode'] && empty($form_state['values']['domain'])) {
    form_set_error('prefix', t('Only the default language can have both the domain and prefix empty.'));
  }
  if (!empty($form_state['values']['prefix']) && $duplicate = db_query("SELECT language FROM {languages} WHERE prefix = :prefix AND language <> :language", array(':prefix' => $form_state['values']['prefix'], ':language' => $form_state['values']['langcode']))->fetchField()) {
    form_set_error('prefix', t('The prefix (%prefix) is already tied to a language (%language).', array('%prefix' => $form_state['values']['prefix'], '%language' => $duplicate)));
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
