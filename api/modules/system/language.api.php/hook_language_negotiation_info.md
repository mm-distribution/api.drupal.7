# hook_language_negotiation_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 140–156 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L140-L156)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [language_negotiation](../../../topics/language_negotiation.md)

## Signature

```php
function hook_language_negotiation_info()
```

## Documentation

```text
Define language negotiation providers.

@return
  An associative array of language negotiation provider definitions. The keys
  are provider identifiers, and the values are associative arrays defining
  each provider, with the following elements:
  - types: An array of allowed language types. If a language negotiation
    provider does not specify which language types it should be used with, it
    will be available for all the configurable language types.
  - callbacks: An associative array of functions that will be called to
    perform various tasks. Possible elements are:
    - language: (required) Name of the callback function that determines the
      language value.
    - switcher: (optional) Name of the callback function that determines
      links for a language switcher block associated with this provider. See
      language_switcher_url() for an example.
    - url_rewrite: (optional) Name of the callback function that provides URL
      rewriting, if needed by this provider.
  - file: The file where callback functions are defined (this file will be
    included before the callbacks are invoked).
  - weight: The default weight of the provider.
  - name: The translated human-readable name for the provider.
  - description: A translated longer description of the provider.
  - config: An internal path pointing to the provider's configuration page.
  - cache: The value Drupal's page cache should be set to for the current
    provider to be invoked.

@see hook_language_negotiation_info_alter()
@ingroup language_negotiation
```

## Code

```php
function hook_language_negotiation_info() {
  return array(
    'custom_language_provider' => array(
      'callbacks' => array(
        'language' => 'custom_language_provider_callback',
        'switcher' => 'custom_language_switcher_callback',
        'url_rewrite' => 'custom_language_url_rewrite_callback',
      ),
      'file' => drupal_get_path('module', 'custom') . '/custom.module',
      'weight' => -4,
      'types' => array('custom_language_type'),
      'name' => t('Custom language negotiation provider'),
      'description' => t('This is a custom language negotiation provider.'),
      'cache' => 0,
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_negotiation_info()".

- [locale_language_negotiation_info()](../../locale/locale.module/locale_language_negotiation_info.md) — `modules/locale/locale.module`
- [locale_test_language_negotiation_info()](../../locale/tests/locale_test.module/locale_test_language_negotiation_info.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
