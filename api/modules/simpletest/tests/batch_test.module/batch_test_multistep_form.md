# batch_test_multistep_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 134–148 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L134-L148)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_multistep_form($form, &$form_state)
```

## Documentation

```text
Multistep form.
```

## Code

```php
function batch_test_multistep_form($form, &$form_state) {
  if (empty($form_state['storage']['step'])) {
    $form_state['storage']['step'] = 1;
  }

  $form['step_display'] = array(
    '#markup' => 'step ' . $form_state['storage']['step'] . '<br/>',
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
