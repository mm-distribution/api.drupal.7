# language_initialize()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 484–501 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L484-L501)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_initialize($type)
```

## Documentation

```text
Chooses a language based on language negotiation provider settings.

@param $type
  The language type key to find the language for.

@return
  The negotiated language object.
```

## Code

```php
function language_initialize($type) {
  // Execute the language negotiation providers in the order they were set up and return the
  // first valid language found.
  $negotiation = variable_get("language_negotiation_$type", array());

  foreach ($negotiation as $provider_id => $provider) {
    $language = language_provider_invoke($provider_id, $provider);
    if ($language) {
      $language->provider = $provider_id;
      return $language;
    }
  }

  // If no other language was found use the default one.
  $language = language_default();
  $language->provider = LANGUAGE_NEGOTIATION_DEFAULT;
  return $language;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
