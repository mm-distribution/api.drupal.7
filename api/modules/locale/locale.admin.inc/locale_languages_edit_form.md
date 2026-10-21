# locale_languages_edit_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 234–250 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L234-L250)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_edit_form($form, &$form_state, $langcode)
```

## Documentation

```text
Editing screen for a particular language.

@param $langcode
  Language code of the language to edit.
```

## Code

```php
function locale_languages_edit_form($form, &$form_state, $langcode) {
  if ($language = db_query("SELECT * FROM {languages} WHERE language = :language", array(':language' => $langcode))->fetchObject()) {
    _locale_languages_common_controls($form, $language);
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Save language')
    );
    $form['#submit'][] = 'locale_languages_edit_form_submit';
    $form['#validate'][] = 'locale_languages_edit_form_validate';
    return $form;
  }
  else {
    drupal_not_found();
    drupal_exit();
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
