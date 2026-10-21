# language_negotiation_info()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 392–412 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L392-L412)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_info()
```

## Documentation

```text
Returns all the defined language negotiation providers.

@return
  An array of language negotiation providers.
```

## Code

```php
function language_negotiation_info() {
  $language_providers = &drupal_static(__FUNCTION__);

  if (!isset($language_providers)) {
    // Collect all the module-defined language negotiation providers.
    $language_providers = module_invoke_all('language_negotiation_info');

    // Add the default language negotiation provider.
    $language_providers[LANGUAGE_NEGOTIATION_DEFAULT] = array(
      'callbacks' => array('language' => 'language_from_default'),
      'weight' => 10,
      'name' => t('Default'),
      'description' => t('Use the default site language (@language_name).', array('@language_name' => language_default()->native)),
    );

    // Let other modules alter the list of language negotiation providers.
    drupal_alter('language_negotiation_info', $language_providers);
  }

  return $language_providers;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
