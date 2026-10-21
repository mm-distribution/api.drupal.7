# block_custom_block_delete()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 621–628 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L621-L628)
- **Module/theme:** block

## Signature

```php
function block_custom_block_delete($form, &$form_state, $module, $delta)
```

## Documentation

```text
Form constructor for the custom block deletion form.

@param $module
  The name of the module that implements the block to be deleted. This should
  always equal 'block' since it only allows custom blocks to be deleted.
@param $delta
  The unique ID of the block within the context of $module.

@see block_custom_block_delete_submit()
```

## Code

```php
function block_custom_block_delete($form, &$form_state, $module, $delta) {
  $block = block_load($module, $delta);
  $custom_block = block_custom_block_get($block->delta);
  $form['info'] = array('#type' => 'hidden', '#value' => $custom_block['info'] ? $custom_block['info'] : $custom_block['title']);
  $form['bid'] = array('#type' => 'hidden', '#value' => $block->delta);

  return confirm_form($form, t('Are you sure you want to delete the block %name?', array('%name' => $custom_block['info'])), 'admin/structure/block', '', t('Delete'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
