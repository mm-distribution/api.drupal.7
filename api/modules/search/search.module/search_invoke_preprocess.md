# search_invoke_preprocess()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 535–539 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L535-L539)
- **Module/theme:** search

## Signature

```php
function search_invoke_preprocess(&$text)
```

## Documentation

```text
Invokes hook_search_preprocess() in modules.
```

## Code

```php
function search_invoke_preprocess(&$text) {
  foreach (module_implements('search_preprocess') as $module) {
    $text = module_invoke($module, 'search_preprocess', $text);
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
