# locale_multilingual_node_type()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 343–345 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L343-L345)
- **Module/theme:** locale

## Signature

```php
function locale_multilingual_node_type($type_name)
```

## Documentation

```text
Return whether the given content type has multilingual support.

@return
  True if multilingual support is enabled.
```

## Code

```php
function locale_multilingual_node_type($type_name) {
  return (bool) variable_get('language_content_type_' . $type_name, 0);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
