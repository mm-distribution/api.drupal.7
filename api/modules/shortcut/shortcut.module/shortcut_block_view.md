# shortcut_block_view()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 200–207 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L200-L207)
- **Module/theme:** shortcut
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function shortcut_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function shortcut_block_view($delta = '') {
  if ($delta == 'shortcuts') {
    $shortcut_set = shortcut_current_displayed_set();
    $data['subject'] = t('@shortcut_set shortcuts', array('@shortcut_set' => $shortcut_set->title));
    $data['content'] = shortcut_renderable_links($shortcut_set);
    return $data;
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
