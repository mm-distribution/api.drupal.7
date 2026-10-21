# locale_languages_custom_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 210–226 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L210-L226)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_custom_form($form)
```

## Documentation

```text
Custom language addition form.
```

## Code

```php
function locale_languages_custom_form($form) {
  $form['custom language'] = array('#type' => 'fieldset',
    '#title' => t('Custom language'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
  );
  _locale_languages_common_controls($form['custom language']);
  $form['custom language']['actions'] = array('#type' => 'actions');
  $form['custom language']['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Add custom language')
  );
  // Reuse the validation and submit functions of the predefined language setup form.
  $form['#submit'][] = 'locale_languages_predefined_form_submit';
  $form['#validate'][] = 'locale_languages_predefined_form_validate';
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
