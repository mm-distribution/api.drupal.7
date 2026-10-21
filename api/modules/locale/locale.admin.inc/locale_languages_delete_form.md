# locale_languages_delete_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 432–456 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L432-L456)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_delete_form($form, &$form_state, $langcode)
```

## Documentation

```text
User interface for the language deletion confirmation screen.
```

## Code

```php
function locale_languages_delete_form($form, &$form_state, $langcode) {

  // Do not allow deletion of English locale.
  if ($langcode == 'en') {
    drupal_set_message(t('The English language cannot be deleted.'));
    drupal_goto('admin/config/regional/language');
  }

  if (language_default('language') == $langcode) {
    drupal_set_message(t('The default language cannot be deleted.'));
    drupal_goto('admin/config/regional/language');
  }

  // For other languages, warn user that data loss is ahead.
  $languages = language_list();

  if (!isset($languages[$langcode])) {
    drupal_not_found();
    drupal_exit();
  }
  else {
    $form['langcode'] = array('#type' => 'value', '#value' => $langcode);
    return confirm_form($form, t('Are you sure you want to delete the language %name?', array('%name' => t($languages[$langcode]->name))), 'admin/config/regional/language', t('Deleting a language will remove all interface translations associated with it, and posts in this language will be set to be language neutral. This action cannot be undone.'), t('Delete'), t('Cancel'));
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
