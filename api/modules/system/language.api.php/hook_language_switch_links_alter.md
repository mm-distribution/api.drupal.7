# hook_language_switch_links_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/language.api.php`](_file.md), lines 54–62 · [local source](../../../../source/modules/system/language.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php#L54-L62)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_language_switch_links_alter(array &$links, $type, $path)
```

## Documentation

```text
Perform alterations on language switcher links.

A language switcher link may need to point to a different path or use a
translated link text before going through l(), which will just handle the
path aliases.

@param $links
  Nested array of links keyed by language code.
@param $type
  The language type the links will switch.
@param $path
  The current path.
```

## Code

```php
function hook_language_switch_links_alter(array &$links, $type, $path) {
  global $language;

  if ($type == LANGUAGE_TYPE_CONTENT && isset($links[$language->language])) {
    foreach ($links[$language->language] as $link) {
      $link['attributes']['class'][] = 'active-language';
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_language_switch_links_alter()".

- [translation_language_switch_links_alter()](../../translation/translation.module/translation_language_switch_links_alter.md) — `modules/translation/translation.module`

---
_Drupal 7.103 · [modules/system/language.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/language.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
