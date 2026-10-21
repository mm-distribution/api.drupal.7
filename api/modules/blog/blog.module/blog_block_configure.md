# blog_block_configure()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 206–216 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L206-L216)
- **Module/theme:** blog
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function blog_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function blog_block_configure($delta = '') {
  if ($delta == 'recent') {
    $form['blog_block_count'] = array(
      '#type' => 'select',
      '#title' => t('Number of recent blog posts to display'),
      '#default_value' => variable_get('blog_block_count', 10),
      '#options' => drupal_map_assoc(array(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30)),
    );
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
