# search_theme()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 102–119 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L102-L119)
- **Module/theme:** search
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function search_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function search_theme() {
  return array(
    'search_block_form' => array(
      'render element' => 'form',
      'template' => 'search-block-form',
    ),
    'search_result' => array(
      'variables' => array('result' => NULL, 'module' => NULL),
      'file' => 'search.pages.inc',
      'template' => 'search-result',
    ),
    'search_results' => array(
      'variables' => array('results' => NULL, 'module' => NULL),
      'file' => 'search.pages.inc',
      'template' => 'search-results',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
