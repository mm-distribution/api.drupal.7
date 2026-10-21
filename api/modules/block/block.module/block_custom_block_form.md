# block_custom_block_form()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 517–544 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L517-L544)
- **Module/theme:** block
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function block_custom_block_form($edit = array())
```

## Documentation

```text
Form constructor for the custom block form.

@param $edit
  (optional) An associative array of information retrieved by
  block_custom_get_block() if an existing block is being edited, or an empty
  array otherwise. Defaults to array().

@ingroup forms
```

## Code

```php
function block_custom_block_form($edit = array()) {
  $edit += array(
    'info' => '',
    'body' => '',
  );
  $form['info'] = array(
    '#type' => 'textfield',
    '#title' => t('Block description'),
    '#default_value' => $edit['info'],
    '#maxlength' => 64,
    '#description' => t('A brief description of your block. Used on the <a href="@overview">Blocks administration page</a>.', array('@overview' => url('admin/structure/block'))),
    '#required' => TRUE,
    '#weight' => -18,
  );
  $form['body_field']['#weight'] = -17;
  $form['body_field']['body'] = array(
    '#type' => 'text_format',
    '#title' => t('Block body'),
    '#default_value' => $edit['body'],
    '#format' => isset($edit['format']) ? $edit['format'] : NULL,
    '#rows' => 15,
    '#description' => t('The content of the block as shown to the user.'),
    '#required' => TRUE,
    '#weight' => -17,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
