# search_embedded_form_preprocess_search_result()

- **Type:** Function
- **File:** [`modules/search/tests/search_embedded_form.module`](_file.md), lines 67–70 · [local source](../../../../../source/modules/search/tests/search_embedded_form.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module#L67-L70)
- **Module/theme:** search_node_tags

## Signature

```php
function search_embedded_form_preprocess_search_result(&$variables)
```

## Documentation

```text
Adds the test form to search results.
```

## Code

```php
function search_embedded_form_preprocess_search_result(&$variables) {
  $form = drupal_get_form('search_embedded_form_form');
  $variables['snippet'] .= drupal_render($form);
}
```

---
_Drupal 7.103 · [modules/search/tests/search_embedded_form.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module) · Licensed GPL-2.0-or-later (see LICENSE)._
