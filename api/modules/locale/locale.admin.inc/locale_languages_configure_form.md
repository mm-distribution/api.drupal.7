# locale_languages_configure_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 498–520 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L498-L520)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_configure_form()
```

## Documentation

```text
Setting for language negotiation options
```

## Code

```php
function locale_languages_configure_form() {
  include_once DRUPAL_ROOT . '/includes/language.inc';

  $form = array(
    '#submit' => array('locale_languages_configure_form_submit'),
    '#theme' => 'locale_languages_configure_form',
    '#language_types' => language_types_configurable(FALSE),
    '#language_types_info' => language_types_info(),
    '#language_providers' => language_negotiation_info(),
  );

  foreach ($form['#language_types'] as $type) {
    _locale_languages_configure_form_language_table($form, $type);
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save settings'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
