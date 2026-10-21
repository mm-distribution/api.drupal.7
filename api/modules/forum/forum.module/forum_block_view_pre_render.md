# forum_block_view_pre_render()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 719–726 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L719-L726)
- **Module/theme:** forum

## Signature

```php
function forum_block_view_pre_render($elements)
```

## Documentation

```text
Render API callback: Lists nodes based on the element's #query property.

This function can be used as a #pre_render callback.

@see forum_block_view()
```

## Code

```php
function forum_block_view_pre_render($elements) {
  $result = $elements['#query']->execute();
  if ($node_title_list = node_title_list($result)) {
    $elements['forum_list'] = $node_title_list;
    $elements['forum_more'] = array('#theme' => 'more_link', '#url' => 'forum', '#title' => t('Read the latest forum topics.'));
  }
  return $elements;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
