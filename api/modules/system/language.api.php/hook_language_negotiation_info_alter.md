# hook_language_negotiation_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 167–171 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L167-L171)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [language_negotiation](../../../topics/language_negotiation.md)

## Signature

```php
function hook_language_negotiation_info_alter(array &$language_providers)
```

## Documentation

```text
Perform alterations on language negoiation providers.

@param $language_providers
  Array of language negotiation provider definitions.

@see hook_language_negotiation_info()
@ingroup language_negotiation
```

## Code

```php
function hook_language_negotiation_info_alter(array &$language_providers) {
  if (isset($language_providers['custom_language_provider'])) {
    $language_providers['custom_language_provider']['config'] = 'admin/config/regional/language/configure/custom-language-provider';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_negotiation_info_alter()".

- [locale_test_language_negotiation_info_alter()](../../locale/tests/locale_test.module/locale_test_language_negotiation_info_alter.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
