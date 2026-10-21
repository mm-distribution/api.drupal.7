# _locale_languages_configure_form_language_table()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 525–603 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L525-L603)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function _locale_languages_configure_form_language_table(&$form, $type)
```

## Documentation

```text
Helper function to build a language provider table.
```

## Code

```php
function _locale_languages_configure_form_language_table(&$form, $type) {
  $info = $form['#language_types_info'][$type];

  $table_form = array(
    '#title' => t('@type language detection', array('@type' => $info['name'])),
    '#tree' => TRUE,
    '#description' => $info['description'],
    '#language_providers' => array(),
    '#show_operations' => FALSE,
    'weight' => array('#tree' => TRUE),
    'enabled' => array('#tree' => TRUE),
  );

  $language_providers = $form['#language_providers'];
  $enabled_providers = variable_get("language_negotiation_$type", array());
  $providers_weight = variable_get("locale_language_providers_weight_$type", array());

  // Add missing data to the providers lists.
  foreach ($language_providers as $id => $provider) {
    if (!isset($providers_weight[$id])) {
      $providers_weight[$id] = language_provider_weight($provider);
    }
  }

  // Order providers list by weight.
  asort($providers_weight);

  foreach ($providers_weight as $id => $weight) {
    // A language provider might be no more available if the defining module has
    // been disabled after the last configuration saving.
    if (!isset($language_providers[$id])) {
      continue;
    }

    $enabled = isset($enabled_providers[$id]);
    $provider = $language_providers[$id];

    // List the provider only if the current type is defined in its 'types' key.
    // If it is not defined default to all the configurable language types.
    $types = array_flip(isset($provider['types']) ? $provider['types'] : $form['#language_types']);

    if (isset($types[$type])) {
      $table_form['#language_providers'][$id] = $provider;

      $table_form['weight'][$id] = array(
        '#type' => 'weight',
        '#title' => t('Weight for @title', array('@title' => $provider['name'])),
        '#title_display' => 'invisible',
        '#default_value' => $weight,
        '#attributes' => array('class' => array("language-provider-weight-$type")),
      );

      $table_form['title'][$id] = array('#markup' => check_plain($provider['name']));

      $table_form['enabled'][$id] = array(
        '#type' => 'checkbox',
        '#title' => t('@title language provider', array('@title' => $provider['name'])),
        '#title_display' => 'invisible',
        '#default_value' => $enabled,
      );
      if ($id === LANGUAGE_NEGOTIATION_DEFAULT) {
        $table_form['enabled'][$id]['#default_value'] = TRUE;
        $table_form['enabled'][$id]['#attributes'] = array('disabled' => 'disabled');
      }

      $table_form['description'][$id] = array('#markup' => filter_xss_admin($provider['description']));

      $config_op = array();
      if (isset($provider['config'])) {
        $config_op = array('#type' => 'link', '#title' => t('Configure'), '#href' => $provider['config']);
        // If there is at least one operation enabled show the operation column.
        $table_form['#show_operations'] = TRUE;
      }
      $table_form['operation'][$id] = $config_op;
    }
  }

  $form[$type] = $table_form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
