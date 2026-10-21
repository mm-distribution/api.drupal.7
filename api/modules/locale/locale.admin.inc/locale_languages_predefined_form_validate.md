# locale_languages_predefined_form_validate()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 324–343 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L324-L343)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_predefined_form_validate($form, &$form_state)
```

## Documentation

```text
Validate the language addition form.
```

## Code

```php
function locale_languages_predefined_form_validate($form, &$form_state) {
  $langcode = $form_state['values']['langcode'];

  if (($duplicate = db_query("SELECT COUNT(*) FROM {languages} WHERE language = :language", array(':language' => $langcode))->fetchField()) != 0) {
    form_set_error('langcode', t('The language %language (%code) already exists.', array('%language' => $form_state['values']['name'], '%code' => $langcode)));
  }

  if (!isset($form_state['values']['name'])) {
    // Predefined language selection.
    include_once DRUPAL_ROOT . '/includes/iso.inc';
    $predefined = _locale_get_predefined_list();
    if (!isset($predefined[$langcode])) {
      form_set_error('langcode', t('Invalid language code.'));
    }
  }
  else {
    // Reuse the editing form validation routine if we add a custom language.
    locale_languages_edit_form_validate($form, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
