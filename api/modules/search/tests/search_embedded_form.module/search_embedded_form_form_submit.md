# search_embedded_form_form_submit()

- **Type:** Function
- **File:** [`modules/search/tests/search_embedded_form.module`](_file.md), lines 58–62 · [local source](../../../../../source/modules/search/tests/search_embedded_form.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module#L58-L62)
- **Module/theme:** search_node_tags

## Signature

```php
function search_embedded_form_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for search_embedded_form_form().
```

## Code

```php
function search_embedded_form_form_submit($form, &$form_state) {
  $count = variable_get('search_embedded_form_submitted', 0) + 1;
  variable_set('search_embedded_form_submitted', $count);
  drupal_set_message(t('Test form was submitted'));
}
```

---
_Drupal 7.103 · [modules/search/tests/search_embedded_form.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module) · Licensed GPL-2.0-or-later (see LICENSE)._
