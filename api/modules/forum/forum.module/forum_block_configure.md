# forum_block_configure()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 662–670 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L662-L670)
- **Module/theme:** forum
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function forum_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function forum_block_configure($delta = '') {
  $form['forum_block_num_' . $delta] = array(
    '#type' => 'select',
    '#title' => t('Number of topics'),
    '#default_value' => variable_get('forum_block_num_' . $delta, '5'),
    '#options' => drupal_map_assoc(range(2, 20))
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
