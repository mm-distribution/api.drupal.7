# locale_form_path_admin_form_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 311–320 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L311-L320)
- **Module/theme:** locale
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function locale_form_path_admin_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function locale_form_path_admin_form_alter(&$form, &$form_state) {
  $form['language'] = array(
    '#type' => 'select',
    '#title' => t('Language'),
    '#options' => array(LANGUAGE_NONE => t('All languages')) + locale_language_list('name'),
    '#default_value' => $form['language']['#value'],
    '#weight' => -10,
    '#description' => t('A path alias set for a specific language will always be used when displaying this page in that language, and takes precedence over path aliases set for <em>All languages</em>.'),
  );
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
