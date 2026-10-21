# hook_language_types_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 82–92 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L82-L92)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [language_negotiation](../../../topics/language_negotiation.md)

## Signature

```php
function hook_language_types_info()
```

## Documentation

```text
Define language types.

@return
  An associative array of language type definitions. The keys are the
  identifiers, which are also used as names for global variables representing
  the types in the bootstrap phase. The values are associative arrays that
  may contain the following elements:
  - name: The human-readable language type identifier.
  - description: A description of the language type.
  - fixed: A fixed array of language negotiation provider identifiers to use
    to initialize this language. Defining this key makes the language type
    non-configurable, so it will always use the specified providers in the
    given priority order. Omit to make the language type configurable.

@see hook_language_types_info_alter()
@ingroup language_negotiation
```

## Code

```php
function hook_language_types_info() {
  return array(
    'custom_language_type' => array(
      'name' => t('Custom language'),
      'description' => t('A custom language type.'),
    ),
    'fixed_custom_language_type' => array(
      'fixed' => array('custom_language_provider'),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_types_info()".

- [locale_language_types_info()](../../locale/locale.module/locale_language_types_info.md) — `modules/locale/locale.module`
- [locale_test_language_types_info()](../../locale/tests/locale_test.module/locale_test_language_types_info.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
