# taxonomy_test_entity_view()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 76–85 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L76-L85)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_view()](../../../system/system.api.php/hook_entity_view.md)

## Signature

```php
function taxonomy_test_entity_view($entity, $type, $view_mode, $langcode)
```

## Documentation

```text
Implements hook_entity_view().
```

## Code

```php
function taxonomy_test_entity_view($entity, $type, $view_mode, $langcode) {
  if ($type == 'taxonomy_term' && $view_mode == 'full') {
    $entity->content['taxonomy_test_entity_view_check'] = array(
      '#prefix' => '<div>',
      '#markup' => t('The antonym is %antonym', array('%antonym' => $entity->antonym)),
      '#suffix' => '</div>',
      '#weight' => 20,
    );
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
