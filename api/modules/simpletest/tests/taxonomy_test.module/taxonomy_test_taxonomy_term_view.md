# taxonomy_test_taxonomy_term_view()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 62–71 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L62-L71)
- **Module/theme:** batch_test
- **Implements:** [hook_taxonomy_term_view()](../../../taxonomy/taxonomy.api.php/hook_taxonomy_term_view.md)

## Signature

```php
function taxonomy_test_taxonomy_term_view($term, $view_mode, $langcode)
```

## Documentation

```text
Implements hook_taxonomy_term_view().
```

## Code

```php
function taxonomy_test_taxonomy_term_view($term, $view_mode, $langcode) {
  if ($view_mode == 'full') {
    $term->content['taxonomy_test_term_view_check'] = array(
      '#prefix' => '<div>',
      '#markup' => t('The antonym is %antonym', array('%antonym' => $term->antonym)),
      '#suffix' => '</div>',
      '#weight' => 10,
    );
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
