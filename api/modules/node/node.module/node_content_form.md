# node_content_form()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3752–3770 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3752-L3770)
- **Module/theme:** node
- **Topics:** [node_content](../../../topics/node_content.md)
- **Implements:** [hook_form()](../node.api.php/hook_form.md)

## Signature

```php
function node_content_form($node, $form_state)
```

## Documentation

```text
Implements hook_form().
```

## Code

```php
function node_content_form($node, $form_state) {
  // It is impossible to define a content type without implementing hook_form()
  // @todo: remove this requirement.
  $form = array();
  $type = node_type_get_type($node);

  if ($type->has_title) {
    $form['title'] = array(
      '#type' => 'textfield',
      '#title' => check_plain($type->title_label),
      '#required' => TRUE,
      '#default_value' => $node->title,
      '#maxlength' => 255,
      '#weight' => -5,
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
