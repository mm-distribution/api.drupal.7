# hook_language_types_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 103–107 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L103-L107)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [language_negotiation](../../../topics/language_negotiation.md)

## Signature

```php
function hook_language_types_info_alter(array &$language_types)
```

## Documentation

```text
Perform alterations on language types.

@param $language_types
  Array of language type definitions.

@see hook_language_types_info()
@ingroup language_negotiation
```

## Code

```php
function hook_language_types_info_alter(array &$language_types) {
  if (isset($language_types['custom_language_type'])) {
    $language_types['custom_language_type_custom']['description'] = t('A far better description.');
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_types_info_alter()".

- [locale_test_language_types_info_alter()](../../locale/tests/locale_test.module/locale_test_language_types_info_alter.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
