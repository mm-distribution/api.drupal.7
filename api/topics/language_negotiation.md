# Language Negotiation API functionality

- **Topic id:** `language_negotiation`
- **Defined in:** [`includes/language.inc`](../includes/language.inc/_file.md), line 15 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L15)

## Documentation

```text
@defgroup language_negotiation Language Negotiation API functionality
@{
Functions to customize the language types and the negotiation process.

The language negotiation API is based on two major concepts:
- Language types: types of translatable data (the types of data that a user
  can view or request).
- Language negotiation providers: functions for determining which language to
  use to present a particular piece of data to the user.
Both language types and language negotiation providers are customizable.

Drupal defines three built-in language types:
- Interface language: The page's main language, used to present translated
  user interface elements such as titles, labels, help text, and messages.
- Content language: The language used to present content that is available
  in more than one language (see
  @link field_language Field Language API @endlink for details).
- URL language: The language associated with URLs. When generating a URL,
  this value will be used by url() as a default if no explicit preference is
  provided.
Modules can define additional language types through
hook_language_types_info(), and alter existing language type definitions
through hook_language_types_info_alter().

Language types may be configurable or fixed. The language negotiation
providers associated with a configurable language type can be explicitly
set through the user interface. A fixed language type has predetermined
(module-defined) language negotiation settings and, thus, does not appear in
the configuration page. Here is a code snippet that makes the content
language (which by default inherits the interface language's values)
configurable:
@code
function mymodule_language_types_info_alter(&$language_types) {
  unset($language_types[LANGUAGE_TYPE_CONTENT]['fixed']);
}
@endcode

Every language type can have a different set of language negotiation
providers assigned to it. Different language types often share the same
language negotiation settings, but they can have independent settings if
needed. If two language types are configured the same way, their language
switcher configuration will be functionally identical and the same settings
will act on both language types.

Drupal defines the following built-in language negotiation providers:
- URL: Determine the language from the URL (path prefix or domain).
- Session: Determine the language from a request/session parameter.
- User: Follow the user's language preference.
- Browser: Determine the language from the browser's language settings.
- Default language: Use the default site language.
Language negotiation providers are simple callback functions that implement a
particular logic to return a language code. For instance, the URL provider
searches for a valid path prefix or domain name in the current request URL.
If a language negotiation provider does not return a valid language code, the
next provider associated to the language type (based on provider weight) is
invoked.

Modules can define additional language negotiation providers through
hook_language_negotiation_info(), and alter existing providers through
hook_language_negotiation_info_alter(). Here is an example snippet that lets
path prefixes be ignored for administrative paths:
@code
function mymodule_language_negotiation_info_alter(&$negotiation_info) {
  // Replace the core function with our own function.
  module_load_include('language', 'inc', 'language.negotiation');
  $negotiation_info[LANGUAGE_NEGOTIATION_URL]['callbacks']['language'] = 'mymodule_from_url';
  $negotiation_info[LANGUAGE_NEGOTIATION_URL]['file'] = drupal_get_path('module', 'mymodule') . '/mymodule.module';
}

function mymodule_from_url($languages) {
  // Use the core URL language negotiation provider to get a valid language
  // code.
  module_load_include('language', 'inc', 'language.negotiation');
  $langcode = language_from_url($languages);

  // If we are on an administrative path, override with the default language.
  if (isset($_GET['q']) && strtok($_GET['q'], '/') == 'admin') {
    return language_default()->langcode;
  }
  return $langcode;
}
@endcode

For more information, see
@link http://drupal.org/node/1497272 Language Negotiation API @endlink
```

## Members (derived, 20)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_language_negotiation_info()](../modules/system/language.api.php/hook_language_negotiation_info.md) (function) — Define language negotiation providers.
- [hook_language_negotiation_info_alter()](../modules/system/language.api.php/hook_language_negotiation_info_alter.md) (function) — Perform alterations on language negoiation providers.
- [hook_language_types_info()](../modules/system/language.api.php/hook_language_types_info.md) (function) — Define language types.
- [hook_language_types_info_alter()](../modules/system/language.api.php/hook_language_types_info_alter.md) (function) — Perform alterations on language types.
- [language_fallback_get_candidates()](../includes/language.inc/language_fallback_get_candidates.md) (function) — Returns the possible fallback languages ordered by language weight.
- [language_from_default()](../includes/language.inc/language_from_default.md) (function) — Returns the default language negotiation provider.
- [language_initialize()](../includes/language.inc/language_initialize.md) (function) — Chooses a language based on language negotiation provider settings.
- [language_negotiation_get()](../includes/language.inc/language_negotiation_get.md) (function) — Checks whether a language negotiation provider is enabled for a language type.
- [language_negotiation_get_any()](../includes/language.inc/language_negotiation_get_any.md) (function) — Checks if the language negotiation provider is enabled for any language type.
- [language_negotiation_get_switch_links()](../includes/language.inc/language_negotiation_get_switch_links.md) (function) — Returns the language switch links for the given language.
- [language_negotiation_info()](../includes/language.inc/language_negotiation_info.md) (function) — Returns all the defined language negotiation providers.
- [language_negotiation_purge()](../includes/language.inc/language_negotiation_purge.md) (function) — Removes any unused language negotiation providers from the configuration.
- [language_negotiation_set()](../includes/language.inc/language_negotiation_set.md) (function) — Saves a list of language negotiation providers.
- [language_provider_invoke()](../includes/language.inc/language_provider_invoke.md) (function) — Helper function used to cache the language negotiation providers results.
- [language_provider_weight()](../includes/language.inc/language_provider_weight.md) (function) — Returns the passed language negotiation provider weight or a default value.
- [language_types_configurable()](../includes/language.inc/language_types_configurable.md) (function) — Returns only the configurable language types.
- [language_types_disable()](../includes/language.inc/language_types_disable.md) (function) — Disables the given language types.
- [language_types_info()](../includes/language.inc/language_types_info.md) (function) — Returns all the defined language types.
- [language_types_set()](../includes/language.inc/language_types_set.md) (function) — Updates the language type configuration.
- [language_url_split_prefix()](../includes/language.inc/language_url_split_prefix.md) (function) — Splits the given path into prefix and actual path.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
