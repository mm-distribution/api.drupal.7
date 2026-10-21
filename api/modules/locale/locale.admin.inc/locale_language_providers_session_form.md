# locale_language_providers_session_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 727–738 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L727-L738)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_language_providers_session_form($form, &$form_state)
```

## Documentation

```text
The URL language provider configuration form.
```

## Code

```php
function locale_language_providers_session_form($form, &$form_state) {
  $form['locale_language_negotiation_session_param'] = array(
    '#title' => t('Request/session parameter'),
    '#type' => 'textfield',
    '#default_value' => variable_get('locale_language_negotiation_session_param', 'language'),
    '#description' => t('Name of the request/session parameter used to determine the desired language.'),
  );

  $form_state['redirect'] = 'admin/config/regional/language/configure';

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
