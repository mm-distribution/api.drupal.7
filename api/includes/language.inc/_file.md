# includes/language.inc

- **Source:** [local](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · 581 lines

## File documentation

```text
@file
Language Negotiation API.

@see http://drupal.org/node/1497272
```

## Functions (derived index)

- [language_types_info()](language_types_info.md) — Returns all the defined language types.
- [language_types_configurable()](language_types_configurable.md) — Returns only the configurable language types.
- [language_types_disable()](language_types_disable.md) — Disables the given language types.
- [language_types_set()](language_types_set.md) — Updates the language type configuration.
- [language_negotiation_get()](language_negotiation_get.md) — Checks whether a language negotiation provider is enabled for a language type.
- [language_negotiation_get_any()](language_negotiation_get_any.md) — Checks if the language negotiation provider is enabled for any language type.
- [language_negotiation_get_switch_links()](language_negotiation_get_switch_links.md) — Returns the language switch links for the given language.
- [language_negotiation_purge()](language_negotiation_purge.md) — Removes any unused language negotiation providers from the configuration.
- [language_negotiation_set()](language_negotiation_set.md) — Saves a list of language negotiation providers.
- [language_negotiation_info()](language_negotiation_info.md) — Returns all the defined language negotiation providers.
- [language_provider_invoke()](language_provider_invoke.md) — Helper function used to cache the language negotiation providers results.
- [language_provider_weight()](language_provider_weight.md) — Returns the passed language negotiation provider weight or a default value.
- [language_initialize()](language_initialize.md) — Chooses a language based on language negotiation provider settings.
- [language_from_default()](language_from_default.md) — Returns the default language negotiation provider.
- [language_url_split_prefix()](language_url_split_prefix.md) — Splits the given path into prefix and actual path.
- [language_fallback_get_candidates()](language_fallback_get_candidates.md) — Returns the possible fallback languages ordered by language weight.

## Constants

### LANGUAGE_NEGOTIATION_DEFAULT

- Line 13

```php
define('LANGUAGE_NEGOTIATION_DEFAULT', 'language-default');
```

```text
No language negotiation. The default language is used.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
