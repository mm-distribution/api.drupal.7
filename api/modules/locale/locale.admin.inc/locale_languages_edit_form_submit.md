# locale_languages_edit_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 404–427 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L404-L427)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Process the language editing form submission.
```

## Code

```php
function locale_languages_edit_form_submit($form, &$form_state) {
  db_update('languages')
    ->fields(array(
      'name' => $form_state['values']['name'],
      'native' => $form_state['values']['native'],
      'domain' => $form_state['values']['domain'],
      'prefix' => $form_state['values']['prefix'],
      'direction' => $form_state['values']['direction'],
    ))
    ->condition('language',  $form_state['values']['langcode'])
    ->execute();
  $default = language_default();
  if ($default->language == $form_state['values']['langcode']) {
    $properties = array('name', 'native', 'direction', 'enabled', 'plurals', 'formula', 'domain', 'prefix', 'weight');
    foreach ($properties as $keyname) {
      if (isset($form_state['values'][$keyname])) {
        $default->$keyname = $form_state['values'][$keyname];
      }
    }
    variable_set('language_default', $default);
  }
  $form_state['redirect'] = 'admin/config/regional/language';
  return;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
