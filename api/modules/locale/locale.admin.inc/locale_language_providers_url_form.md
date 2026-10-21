# locale_language_providers_url_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 707–722 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L707-L722)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_language_providers_url_form($form, &$form_state)
```

## Documentation

```text
The URL language provider configuration form.
```

## Code

```php
function locale_language_providers_url_form($form, &$form_state) {
  $form['locale_language_negotiation_url_part'] = array(
    '#title' => t('Part of the URL that determines language'),
    '#type' => 'radios',
    '#options' => array(
      LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX => t('Path prefix'),
      LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN => t('Domain'),
    ),
    '#default_value' => variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX),
    '#description' => t('<em>Path prefix</em>: URLs like http://example.com/de/contact set language to German (de). <em>Domain</em>: URLs like http://de.example.com/contact set the language to German. <strong>Warning: Changing this setting may break incoming URLs. Use with caution on a production site.</strong>'),
  );

  $form_state['redirect'] = 'admin/config/regional/language/configure';

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
