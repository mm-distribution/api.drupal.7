# translation_supported_type()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 513–515 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L513-L515)
- **Module/theme:** translation

## Signature

```php
function translation_supported_type($type)
```

## Documentation

```text
Returns whether the given content type has support for translations.

@return
  TRUE if translation is supported, and FALSE if not.
```

## Code

```php
function translation_supported_type($type) {
  return variable_get('language_content_type_' . $type, 0) == TRANSLATION_ENABLED;
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
