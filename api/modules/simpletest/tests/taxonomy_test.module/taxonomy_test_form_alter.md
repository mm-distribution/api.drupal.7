# taxonomy_test_form_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 90–100 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L90-L100)
- **Module/theme:** batch_test
- **Implements:** [hook_form_alter()](../../../system/system.api.php/hook_form_alter.md)

## Signature

```php
function taxonomy_test_form_alter(&$form, $form_state, $form_id)
```

## Documentation

```text
Implements hook_form_alter().
```

## Code

```php
function taxonomy_test_form_alter(&$form, $form_state, $form_id) {
  if ($form_id == 'taxonomy_form_term') {
    $antonym = taxonomy_test_get_antonym($form['#term']['tid']);
    $form['advanced']['antonym'] = array(
      '#type' => 'textfield',
      '#title' => t('Antonym'),
      '#default_value' => !empty($antonym) ? $antonym : '',
      '#description' => t('Antonym of this term.')
    );
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
