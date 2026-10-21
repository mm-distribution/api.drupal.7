# locale_translate_export_pot_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1062–1078 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1062-L1078)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translate_export_pot_form()
```

## Documentation

```text
Translation template export form.
```

## Code

```php
function locale_translate_export_pot_form() {
  // Complete template export of the strings
  $form['export_title'] = array('#type' => 'item',
    '#title' => t('Export template'),
    '#description' => t('Generate a Gettext Portable Object Template (<em>.pot</em>) file with all strings from the Drupal locale database.'),
  );
  $form['group'] = array('#type' => 'radios',
    '#title' => t('Text group'),
    '#default_value' => 'default',
    '#options' => module_invoke_all('locale', 'groups'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Export'));
  // Reuse PO export submission callback.
  $form['#submit'][] = 'locale_translate_export_po_form_submit';
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
