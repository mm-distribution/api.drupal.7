# locale_languages_configure_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 675–702 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L675-L702)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_configure_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for language negotiation settings.
```

## Code

```php
function locale_languages_configure_form_submit($form, &$form_state) {
  $configurable_types = $form['#language_types'];

  foreach ($configurable_types as $type) {
    $negotiation = array();
    $enabled_providers = $form_state['values'][$type]['enabled'];
    $enabled_providers[LANGUAGE_NEGOTIATION_DEFAULT] = TRUE;
    $providers_weight = $form_state['values'][$type]['weight'];

    foreach ($providers_weight as $id => $weight) {
      if ($enabled_providers[$id]) {
        $provider = $form[$type]['#language_providers'][$id];
        $provider['weight'] = $weight;
        $negotiation[$id] = $provider;
      }
    }

    language_negotiation_set($type, $negotiation);
    variable_set("locale_language_providers_weight_$type", $providers_weight);
  }

  // Update non-configurable language types and the related language negotiation
  // configuration.
  language_types_set();

  $form_state['redirect'] = 'admin/config/regional/language/configure';
  drupal_set_message(t('Language negotiation configuration saved.'));
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
