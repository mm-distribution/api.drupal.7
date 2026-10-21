# template_preprocess_search_block_form()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1065–1082 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1065-L1082)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function template_preprocess_search_block_form(&$variables)
```

## Documentation

```text
Process variables for search-block-form.tpl.php.

The $variables array contains the following arguments:
- $form

@see search-block-form.tpl.php
```

## Code

```php
function template_preprocess_search_block_form(&$variables) {
  $variables['search'] = array();
  $hidden = array();
  // Provide variables named after form keys so themers can print each element independently.
  foreach (element_children($variables['form']) as $key) {
    $type = isset($variables['form'][$key]['#type']) ? $variables['form'][$key]['#type'] : '';
    if ($type == 'hidden' || $type == 'token') {
      $hidden[] = drupal_render($variables['form'][$key]);
    }
    else {
      $variables['search'][$key] = drupal_render($variables['form'][$key]);
    }
  }
  // Hidden form elements have no value to themers. No need for separation.
  $variables['search']['hidden'] = implode($hidden);
  // Collect all form elements to make it easier to print the whole form.
  $variables['search_form'] = implode($variables['search']);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
