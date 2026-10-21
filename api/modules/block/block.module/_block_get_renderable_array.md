# _block_get_renderable_array()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 333–360 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L333-L360)
- **Module/theme:** block

## Signature

```php
function _block_get_renderable_array($list = array())
```

## Documentation

```text
Gets an array of blocks suitable for drupal_render().

@param $list
  A list of blocks such as that returned by block_list().

@return
  A renderable array.
```

## Code

```php
function _block_get_renderable_array($list = array()) {
  $weight = 0;
  $build = array();
  foreach ($list as $key => $block) {
    $build[$key] = $block->content;
    unset($block->content);

    // Add contextual links for this block; skip the main content block, since
    // contextual links are basically output as tabs/local tasks already. Also
    // skip the help block, since we assume that most users do not need or want
    // to perform contextual actions on the help block, and the links needlessly
    // draw attention on it.
    if ($key != 'system_main' && $key != 'system_help') {
      $build[$key]['#contextual_links']['block'] = array(
        'admin/structure/block/manage',
        array($block->module, $block->delta),
      );
    }

    $build[$key] += array(
      '#block' => $block,
      '#weight' => ++$weight,
    );
    $build[$key]['#theme_wrappers'][] = 'block';
  }
  $build['#sorted'] = TRUE;
  return $build;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
