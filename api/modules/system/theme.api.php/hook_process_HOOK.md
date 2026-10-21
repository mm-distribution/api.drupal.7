# hook_process_HOOK()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 207–213 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L207-L213)
- **Module/theme:** system

## Signature

```php
function hook_process_HOOK(&$variables)
```

## Documentation

```text
Process theme variables for a specific theme hook.

This hook allows modules to process theme variables for a specific theme
hook. It should only be used if a module needs to override or add to the
theme processing for a theme hook it didn't define.

For more detailed information, see theme().

@param $variables
  The variables array (modify in place).
```

## Code

```php
function hook_process_HOOK(&$variables) {
  // @todo There are no use-cases in Drupal core for this hook. Find one from a
  //   contributed module, or come up with a good example. Coming up with a good
  //   example might be tough, since the intent is for nearly everything to be
  //   achievable via preprocess functions, and for process functions to only be
  //   used when requiring the later execution time.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_process_HOOK()".

_None found._

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
