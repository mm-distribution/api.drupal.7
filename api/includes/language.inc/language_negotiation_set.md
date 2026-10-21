# language_negotiation_set()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 347–384 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L347-L384)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_set($type, $language_providers)
```

## Documentation

```text
Saves a list of language negotiation providers.

@param $type
  The language negotiation type.
@param $language_providers
  An array of language negotiation provider weights keyed by provider ID.
  @see language_provider_weight()
```

## Code

```php
function language_negotiation_set($type, $language_providers) {
  // Save only the necessary fields.
  $provider_fields = array('callbacks', 'file', 'cache');

  $negotiation = array();
  $providers_weight = array();
  $defined_providers = language_negotiation_info();
  $default_types = language_types_configurable(FALSE);

  // Initialize the providers weight list.
  foreach ($language_providers as $id => $provider) {
    $providers_weight[$id] = language_provider_weight($provider);
  }

  // Order providers list by weight.
  asort($providers_weight);

  foreach ($providers_weight as $id => $weight) {
    if (isset($defined_providers[$id])) {
      $provider = $defined_providers[$id];
      // If the provider does not express any preference about types, make it
      // available for any configurable type.
      $types = array_flip(isset($provider['types']) ? $provider['types'] : $default_types);
      // Check whether the provider is defined and has the right type.
      if (isset($types[$type])) {
        $provider_data = array();
        foreach ($provider_fields as $field) {
          if (isset($provider[$field])) {
            $provider_data[$field] = $provider[$field];
          }
        }
        $negotiation[$id] = $provider_data;
      }
    }
  }

  variable_set("language_negotiation_$type", $negotiation);
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
