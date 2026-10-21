# dashboard_show_block_content()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 520–538 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L520-L538)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_show_block_content($module, $delta)
```

## Documentation

```text
Ajax callback: Displays the rendered contents of a specific block.

@param $module
  The block's module name.
@param $delta
  The block's delta.
```

## Code

```php
function dashboard_show_block_content($module, $delta) {
  drupal_theme_initialize();
  global $theme_key;

  $blocks = array();
  $block_object = db_query("SELECT * FROM {block} WHERE theme = :theme AND module = :module AND delta = :delta", array(
    ":theme" => $theme_key,
    ":module" => $module,
    ":delta" => $delta,
    ))
    ->fetchObject();
  $block_object->enabled = $block_object->page_match = TRUE;
  $blocks[$module . "_" . $delta] = $block_object;
  $block_content = _block_render_blocks($blocks);
  $build = _block_get_renderable_array($block_content);
  $rendered_block = drupal_render($build);
  print $rendered_block;
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
