# hook_language_init()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 26–38 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L26-L38)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_language_init()
```

## Documentation

```text
Allows modules to act after language initialization has been performed.

This is primarily needed to provide translation for configuration variables
in the proper bootstrap phase. Variables are user-defined strings and
therefore should not be translated via t(), since the source string can
change without notice and any previous translation would be lost. Moreover,
since variables can be used in the bootstrap phase, we need a bootstrap hook
to provide a translation early enough to avoid misalignments between code
using the original values and code using the translated values. However
modules implementing hook_boot() should be aware that language initialization
did not happen yet and thus they cannot rely on translated variables.
```

## Code

```php
function hook_language_init() {
  global $language, $conf;

  switch ($language->language) {
    case 'it':
      $conf['site_name'] = 'Il mio sito Drupal';
      break;

    case 'fr':
      $conf['site_name'] = 'Mon site Drupal';
      break;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_init()".

_None found._

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
