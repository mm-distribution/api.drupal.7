# locale_translate_export_po_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1040–1057 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1040-L1057)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translate_export_po_form($form, &$form_state, $names)
```

## Documentation

```text
Form to export PO files for the languages provided.

@param $names
  An associate array with localized language names
```

## Code

```php
function locale_translate_export_po_form($form, &$form_state, $names) {
  $form['export_title'] = array('#type' => 'item',
    '#title' => t('Export translation'),
  );
  $form['langcode'] = array('#type' => 'select',
    '#title' => t('Language name'),
    '#options' => $names,
    '#description' => t('Select the language to export in Gettext Portable Object (<em>.po</em>) format.'),
  );
  $form['group'] = array('#type' => 'radios',
    '#title' => t('Text group'),
    '#default_value' => 'default',
    '#options' => module_invoke_all('locale', 'groups'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Export'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
