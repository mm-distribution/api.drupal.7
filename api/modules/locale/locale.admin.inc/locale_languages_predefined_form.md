# locale_languages_predefined_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 190–205 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L190-L205)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_predefined_form($form)
```

## Documentation

```text
Predefined language setup form.
```

## Code

```php
function locale_languages_predefined_form($form) {
  $predefined = _locale_prepare_predefined_list();
  $form['language list'] = array('#type' => 'fieldset',
    '#title' => t('Predefined language'),
    '#collapsible' => TRUE,
  );
  $form['language list']['langcode'] = array('#type' => 'select',
    '#title' => t('Language name'),
    '#default_value' => key($predefined),
    '#options' => $predefined,
    '#description' => t('Use the <em>Custom language</em> section below if your desired language does not appear in this list.'),
  );
  $form['language list']['actions'] = array('#type' => 'actions');
  $form['language list']['actions']['submit'] = array('#type' => 'submit', '#value' => t('Add language'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
