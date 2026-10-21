# hook_language_fallback_candidates_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 180–182 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L180-L182)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_language_fallback_candidates_alter(array &$fallback_candidates)
```

## Documentation

```text
Perform alterations on the language fallback candidates.

@param $fallback_candidates
  An array of language codes whose order will determine the language fallback
  order.
```

## Code

```php
function hook_language_fallback_candidates_alter(array &$fallback_candidates) {
  $fallback_candidates = array_reverse($fallback_candidates);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_fallback_candidates_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
