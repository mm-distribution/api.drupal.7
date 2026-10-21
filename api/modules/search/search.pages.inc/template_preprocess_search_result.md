# template_preprocess_search_result()

- **Type:** Function
- **File:** [`modules/search/search.pages.inc`](_file.md), lines 106–136 · [local source](../../../../source/modules/search/search.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc#L106-L136)
- **Module/theme:** search

## Signature

```php
function template_preprocess_search_result(&$variables)
```

## Documentation

```text
Process variables for search-result.tpl.php.

The $variables array contains the following arguments:
- $result
- $module

@see search-result.tpl.php
```

## Code

```php
function template_preprocess_search_result(&$variables) {
  global $language;

  $result = $variables['result'];
  $variables['url'] = check_url($result['link']);
  $variables['title'] = check_plain($result['title']);
  if (isset($result['language']) && $result['language'] != $language->language && $result['language'] != LANGUAGE_NONE) {
    $variables['title_attributes_array']['xml:lang'] = $result['language'];
    $variables['content_attributes_array']['xml:lang'] = $result['language'];
  }

  $info = array();
  if (!empty($result['module'])) {
    $info['module'] = check_plain($result['module']);
  }
  if (!empty($result['user'])) {
    $info['user'] = $result['user'];
  }
  if (!empty($result['date'])) {
    $info['date'] = format_date($result['date'], 'short');
  }
  if (isset($result['extra']) && is_array($result['extra'])) {
    $info = array_merge($info, $result['extra']);
  }
  // Check for existence. User search does not include snippets.
  $variables['snippet'] = isset($result['snippet']) ? $result['snippet'] : '';
  // Provide separated and grouped meta information..
  $variables['info_split'] = $info;
  $variables['info'] = implode(' - ', $info);
  $variables['theme_hook_suggestions'][] = 'search_result__' . $variables['module'];
}
```

---
_Drupal 7.103 · [modules/search/search.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
