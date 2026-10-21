# search_embedded_form_form()

- **Type:** Function
- **File:** [`modules/search/tests/search_embedded_form.module`](_file.md), lines 32–53 · [local source](../../../../../source/modules/search/tests/search_embedded_form.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module#L32-L53)
- **Module/theme:** search_node_tags

## Signature

```php
function search_embedded_form_form($form, &$form_state)
```

## Documentation

```text
Builds a form for embedding in search results for testing.

@see search_embedded_form_form_submit().
```

## Code

```php
function search_embedded_form_form($form, &$form_state) {
  $count = variable_get('search_embedded_form_submitted', 0);

  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Your name'),
    '#maxlength' => 255,
    '#default_value' => '',
    '#required' => TRUE,
    '#description' => t('Times form has been submitted: %count', array('%count' => $count)),
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Send away'),
  );

  $form['#submit'][] = 'search_embedded_form_form_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/search/tests/search_embedded_form.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module) · Licensed GPL-2.0-or-later (see LICENSE)._
